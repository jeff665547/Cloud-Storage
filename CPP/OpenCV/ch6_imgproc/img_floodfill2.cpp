/* 漫水填充 floodfill */
// 漫水填充
# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <iostream>

/* Global Variable Declaration */
cv::Mat g_srcImage, g_dstImage, g_grayImage, g_maskImage;  // 定義原始圖、目標影像、灰階圖、遮罩圖
int g_nFillMode = 1; // 漫水填充的模式
int g_nLowDifference = 20, g_nUpDifference = 20;  // 負差最大值、正差最大值
int g_nConnectivity = 4; // 表示floodFill函數識別字低八位元的連通值
int g_bIsColor = true;  // 是否為彩色圖的識別字布林值
bool g_bUseMask = false;  // 是否顯示遮罩視窗的布林值
int g_nNewMaskVal = 255;  // 新的重新繪製的像素值

// onMouse()
static void onMouse(int event, int x, int y, int, void*){
    // 若滑鼠左鍵沒有按下，便返回
    // OpenCV2: if (event != CV_EVENT_LBUTTONDOWN)
    if (event != cv::EVENT_LBUTTONDOWN)
        return;

    /* <1> 使用 floodFill 函數之前的參數準備部分 */
    cv::Point seed = cv::Point(x, y);
    int LowDifference = g_nFillMode == 0 ? 0 : g_nLowDifference;  // 空範圍的漫水填充，此值設為0，否則設為全域的g_nLowDifference
    int UpDifference = g_nFillMode == 0 ? 0 : g_nUpDifference;  // 空範圍的漫水填充，此值設為0，否則設為全域的g_nUpDifference
    // variable = Expression 1 ? Expression 2 : Expression 3
    // If Expression 1 is true, then variable = Expression 2.
    // If Expression 1 is false, then variable = Expression 3.
    // if(Expression1){
    //     variable = Expression 2;
    // }else{
    //     variable = Expression 3;
    // }

    // 識別字的0~7位為g_nConnectivity，8~15位為g_nNewMaskVal左移8位的值，16~23位為cv::FLOOSFILL_FIXED_RANGE或者0。
    // OpenCV2:
    // int flags = g_nConnectivity + (g_nNewMaskVal << 8) + (g_nFillMode == 1 ? CV_FLOODFILL_FIXED_RANGE : 0);
    // OpenCV3:
    int flags = g_nConnectivity + (g_nNewMaskVal << 8) + (g_nFillMode == 1 ? cv::FLOODFILL_FIXED_RANGE : 0);

    // 隨機產生bgr值
    int b = (unsigned)cv::theRNG() & 255; // 隨機返回一個0~255之間的值
    int g = (unsigned)cv::theRNG() & 255; // 隨機返回一個0~255之間的值
    int r = (unsigned)cv::theRNG() & 255; // 隨機返回一個0~255之間的值
    cv::Rect ccomp; // 定義重繪區域的最小邊界矩形區域

    cv::Scalar newVal = g_bIsColor ? cv::Scalar(b, g, r) : cv::Scalar(r*0.299 + g*0.587 + b*0.114); 
    // 在重繪區域像素的新值，若是彩色圖模式，取cv::Scalar(b, g, r); 若是灰階圖模式，取Scalar(r*0.299 + g*0.587 + b*0.114)

    cv::Mat dst = g_bIsColor ? g_dstImage : g_grayImage; // 目標影像的賦值
    int area;

    /* <2> 正式使用 floodFill 函數 */
    if ( g_bUseMask ){
        // OpenCV2: cv::threshold(g_maskImage, g_maskImage, 1, 128, CV_THRESH_BINARY);
        // OpenCV3
        cv::threshold(g_maskImage, g_maskImage, 1, 128, cv::THRESH_BINARY);

        area = cv::floodFill(dst, g_maskImage, seed, newVal, &ccomp, 
                             cv::Scalar(LowDifference, LowDifference, LowDifference),
                             cv::Scalar(UpDifference, UpDifference, UpDifference), flags);
    }else{
        area = cv::floodFill(dst, seed, newVal, &ccomp, 
                             cv::Scalar(LowDifference, LowDifference, LowDifference),
                             cv::Scalar(UpDifference, UpDifference, UpDifference), flags);
    }

    cv::imshow("Processed", dst);
    std::cout << area << " pixel is repainted." << std::endl;

}

int main(int argc, char* argv[]){

    // Load the raw image
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);

    if(!g_srcImage.data){
        std::cout << "Load the image failed!" << std::endl;
        return false;
    }

    g_srcImage.copyTo(g_dstImage);  // 複製來源圖到目標影像
    cv::cvtColor(g_srcImage, g_grayImage, cv::COLOR_BGR2GRAY); // 轉換三色版的image0到灰階圖
    g_maskImage.create(g_srcImage.rows + 2, g_srcImage.cols + 2, CV_8UC1);  // 利用image0的尺寸來初始化遮罩mask

    // OpenCV2:
    // cv::namedWindow("Processed", CV_WINDOW_AUTOSIZE);
    // OpenCV3:
    cv::namedWindow("Processed", cv::WINDOW_AUTOSIZE);

    // Create the trackbar
    cv::createTrackbar("Negative margin maximum", "Processed", &g_nLowDifference, 255, 0);
    cv::createTrackbar("Positive margin maximum", "Processed", &g_nUpDifference, 255, 0);

    // Mouse callback function
    cv::setMouseCallback("Processed", onMouse, 0);

    // 迴圈輪詢按鍵
    while(1){

        // Show the processed image
        cv::imshow("Processed", g_bIsColor ? g_dstImage : g_grayImage);

        // Get the keybad.
        int c = cv::waitKey(0);
        // 判斷ESC是否按下，若按下便退出
        if((c & 255) == 27){
            std::cout << "Program exiting ..." << std::endl;
            break;
        }

        // 根據按鍵的不同，進行各種操作
        switch((char) c){
            // 如果按鍵"1"被按下，效果圖在灰階圖，彩色圖之間互換
            case '1':
            // 若原為彩色，轉為灰階圖，並且將遮罩mask所有元素設定為0。
                if(g_bIsColor){
                    std::cout << "Keypad '1' is pressed，switch to the color/gray mode, the operation will lead to gray mode." << std::endl;
                    cv::cvtColor(g_srcImage, g_grayImage, cv::COLOR_BGR2GRAY);
                    g_maskImage = cv::Scalar::all(0);
                    g_bIsColor = false; // 將識別字置為false，表示現在影像不為彩色，而是灰階
                }else{ // 若原為灰階圖，便將原來的彩色圖image0再次複製給image，並且將遮罩mask所有元素設定為0。
                    std::cout << "Keypad '1' is pressed，switch to the color/gray mode, the operation will lead to gray mode." << std::endl; 
                    g_srcImage.copyTo(g_dstImage);
                    g_maskImage = cv::Scalar::all(0);
                    g_bIsColor = true;  // 將識別字置為true，表示現在影像模式為彩色。
                }
                break;
            
            // 如果按鍵"2"被按下，顯示/隱藏遮罩視窗
            case '2':
                if(g_bUseMask){
                    cv::destroyWindow("mask");
                    g_bUseMask = false;
                }else{
                    cv::namedWindow("mask", 0);
                    g_maskImage = cv::Scalar::all(0);
                    cv::imshow("mask", g_maskImage);
                    g_bUseMask = true;
                }
                break;

            // 如果按鍵"3"被按下，恢復原始影像
            case '3':
                std::cout << "Keypad '3' is pressed, restore the original image." << std::endl;
                g_srcImage.copyTo(g_dstImage);
                cv::cvtColor(g_dstImage, g_grayImage, cv::COLOR_BGR2GRAY);
                g_maskImage = cv::Scalar::all(0);
                break;

            // 如果按鍵"4"被按下，使用空範圍的漫水填充
            case '4':
                std::cout << "Keypad '4' is pressed, 使用空範圍的漫水填充." << std::endl;
                g_nFillMode = 0;
                break;
            
            // 如果按鍵"5"被按下，使用漸變、固定範圍的漫水填充
            case '5':
                std::cout << "Keypad '5' is pressed, 使用漸變、固定範圍的漫水填充." << std::endl;
                g_nFillMode = 1;
                break;
            
            // 如果按鍵"6"被按下，使用漸變、浮動範圍的漫水填充
            case '6':
                std::cout << "Keypad '6' is pressed, 使用漸變、浮動範圍的漫水填充." << std::endl;
                g_nFillMode = 2;
                break;

            // 如果按鍵"7"被按下，操作標誌符號的第八位元使用4位元的連續模式
            case '7':
                std::cout << "Keypad '7' is pressed, 操作標誌符號的第八位元使用4位元的連續模式." << std::endl;
                g_nConnectivity = 4;
                break;

            // 如果按鍵"8"被按下，操作標誌符號的第八位元使用8位元的連續模式
            case '8':
                std::cout << "Keypad '8' is pressed, 操作標誌符號的第八位元使用8位元的連接模式." << std::endl;
                g_nConnectivity = 8;
                break;
            
        }
    }

    return 0;
}