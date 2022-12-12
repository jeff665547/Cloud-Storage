// 分水嶺演算法
# include <opencv2/imgproc/imgproc.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <iostream>
# define WINDOW_NAME "program"  

/* Global Variable Declaration */
cv::Mat g_maskImage, g_srcImage;
cv::Point prevPt(-1, -1);

// static void ShowHelpText();
static void on_Mouse( int event, int x, int y, int flags, void*);

int main(int argc, char** argv){

    std::cout << std::endl;
    std::cout << "\tPress 1 to show the effect of this algorithm." << std::endl;
    std::cout << "\tPress 2 to restore the original image." << std::endl;
    std::cout << std::endl;

    // 1. Load the image and show the image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch8_imgcontour_inpaint/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);
    cv::imshow(WINDOW_NAME, g_srcImage);
    cv::Mat srcImage, grayImage;
    g_srcImage.copyTo(srcImage);
    cv::cvtColor(g_srcImage, g_maskImage, cv::COLOR_BGR2GRAY);
    cv::cvtColor(g_maskImage, grayImage, cv::COLOR_GRAY2BGR);
    g_maskImage = cv::Scalar::all(0);

    // 2. 設定滑鼠回呼函數
    cv::setMouseCallback(WINDOW_NAME, on_Mouse, 0);

    // 3. 輪詢按鍵，進行處理
    while(1){
        // get the keypad
        int c = cv::waitKey(0);

        // if the keypad is ESC, then quit.
        if((char)c == 27)
            break;

        if((char)c == '2'){
            g_maskImage = cv::Scalar::all(0);
            srcImage.copyTo(g_srcImage);
            cv::imshow("image", g_srcImage);
        }

        // 若檢測到按鍵值為1或者空格，則進行處理
        if((char)c == '1' || (char)c == ' '){
            // Define some parameter
            int i, j, compCount = 0;
            std::vector<std::vector<cv::Point>> contours;
            std::vector<cv::Vec4i> hierarchy;

            // Find the contour
            cv::findContours(g_maskImage, contours, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE);

            // 輪廓為空的處理
            if(contours.empty())
                continue;

            // 複製遮罩
            cv::Mat maskImage(g_maskImage.size(), CV_32S);
            maskImage = cv::Scalar::all(0);

            // 迴圈繪製出輪廓
            for(int index = 0; index >= 0; index = hierarchy[index][0], compCount++)
                drawContours(maskImage, contours, index, cv::Scalar::all(compCount+1), -1, 8, hierarchy, INT_MAX);

            // compCount為零時的處理
            if(compCount == 0)
                continue;

            // 產生隨機顏色
            std::vector<cv::Vec3b> colorTab;
            for(i = 0; i < compCount; i++){
                
                int b = cv::theRNG().uniform(0, 255);
                int g = cv::theRNG().uniform(0, 255);
                int r = cv::theRNG().uniform(0, 255);

                colorTab.push_back(cv::Vec3b((uchar)b, (uchar)g, (uchar)r));
            }

            // 計算處理時間並輸出到視窗中
            double dTime = (double)cv::getTickCount();
            watershed(srcImage, maskImage);
            dTime = (double)cv::getTickCount() - dTime;
            printf("\tProcessing time = %gms\n", dTime*1000./cv::getTickFrequency());

            // 雙層迴圈，將分水嶺影像瀏覽存入watershedImage中
            cv::Mat watershedImage(maskImage.size(), CV_8UC3);
            for(i = 0; i < maskImage.rows; i++){
                for(j = 0; j < maskImage.cols; j++){
                    int index = maskImage.at<int>(i, j);
                    if(index == -1){
                        watershedImage.at<cv::Vec3b>(i, j) = cv::Vec3b(255, 255, 255);
                    }else if(index <= 0 || index >= compCount){
                        watershedImage.at<cv::Vec3b>(i, j) = cv::Vec3b(0, 0, 0);
                    }else{
                        watershedImage.at<cv::Vec3b>(i, j) = colorTab[index - i];
                    }
                }
            }

            // 混合灰階圖和分水嶺效果圖並顯示最終的視窗
            watershedImage = watershedImage*0.5 + grayImage*0.5;
            cv::imshow("watershed transform", watershedImage);

        }
    }

    return 0;
}

static void on_Mouse(int event, int x, int y, int flags, void *){
    // 處理滑鼠不再視窗中的情況
    if(x < 0 || x >= g_srcImage.cols || y < 0 || y >= g_srcImage.rows)
        return;
    // 處理滑鼠左鍵相關訊息
    if(event == cv::EVENT_LBUTTONUP || !(flags & cv::EVENT_FLAG_LBUTTON)){
        prevPt = cv::Point(-1, -1);
    }else if(event == cv::EVENT_LBUTTONDOWN){
        prevPt = cv::Point(x, y);
    }else if(event == cv::EVENT_MOUSEMOVE && (flags & cv::EVENT_FLAG_LBUTTON)){
    // 滑鼠左鍵按下並且移動，繪製出白色線條
        cv::Point pt(x, y);
        if(prevPt.x < 0){
            prevPt = pt;
        }
        cv::line(g_maskImage, prevPt, pt, cv::Scalar::all(255), 5, 8, 0);
        cv::line(g_srcImage, prevPt, pt, cv::Scalar::all(255), 5, 8, 0);
        prevPt = pt;
        cv::imshow(WINDOW_NAME, g_srcImage);
    }

}