# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <iostream>

/* Global Function Declaration */
static void on_ContrastAndBright(int, void *);
static void ShowHelpText();

/* Globla Variable Declaration */
int g_nContrastValue; // 對比度值
int g_nBrightValue;  // 亮度值
cv::Mat g_srcImage, g_dstImage;


int main(){

    // 1. Load the image
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");
    if (!g_srcImage.data){
        std::cout << "Load the image failed! " << std::endl;
        return false;
    }
    g_dstImage = cv::Mat::zeros(g_srcImage.size(), g_srcImage.type());

    // 2. Set the initial value of the contrast and the brightness.
    g_nContrastValue = 80;
    g_nBrightValue = 80;

    // 3. 建立效果視窗圖
    cv::namedWindow("Processed Image", 1);

    // 4. 建立軌跡條
    cv::createTrackbar("Contrast: ", "Processed Image", &g_nContrastValue, 300, on_ContrastAndBright);
    cv::createTrackbar("Brightness: ", "Processed Image", &g_nBrightValue, 200, on_ContrastAndBright);

    // 5. 進行回呼函數初始化
    on_ContrastAndBright(g_nContrastValue, 0);
    on_ContrastAndBright(g_nBrightValue, 0);

    // 6. 按下"q"鍵時，程式退出
    while(char(cv::waitKey(1)) != 'q') {}

    return 0;
}

static void on_ContrastAndBright(int, void *){
    // 建立視窗
    cv::namedWindow("Original", 1);

    /* 影像對比度、亮度值調整 */
    // 一般的影像處理運算元都是一個函數，他接受一個或多個匯入影像，並產生出匯出影像。
    // 影像亮度和對比度的調整操作屬於影像處理變換中比較簡單的一種(點操作 pointoperators)
    // 點操作有一個特點：僅僅根據輸入像素值(有時可以加上全域資訊或參數)，來計算相應的輸出像素值。
    // 這類運算元包括亮度(brightness)和對比度(contrast)調整、顏色校正(coorcorrection)和變換(transformation)。
    // 其中，最常用的點操作(或者說點運算元)是乘上一個常數(對應對比度的調整)以及加上一個常數(對應亮度值的調整)。
    // 公式為  g(x) = a*f(x) + b,  ( or g(i, j) = a*f(i, j) + b , 第i列和第j行 )
    // 其中，f(x) 表示來源影像像素
    //       g(x) 表示輸出影像像素
    //       a ( a > 0 ) 被稱為增益( gain )，常常被用來控制影像的對比度。
    //       b 通常被稱為偏置( bias )，常常被用來控制影像的亮度。

    for (int y = 0; y < g_srcImage.rows; y++){
        for (int x = 0; x < g_srcImage.cols; x++){
            for (int c = 0; c < 3; c++){
                g_dstImage.at<cv::Vec3b>(y, x)[c] = cv::saturate_cast<uchar>((g_nContrastValue*0.01)*(g_srcImage.at<cv::Vec3b>(y, x)[c] ) + g_nBrightValue);
                // 為了存取每一個像素，使用這樣的語法: img.at<cv::Vec3b>(y, x)[c]。 y是像素所在的行，x是像素所在的列，c是R、G、B其中之1。
                // 
                // 因為運算結果可能會超出像素取值範圍(溢出)，還可能是非整數(如果是浮點數的話)，所以要用saturate_cast對結果進行轉換，以確保它為有效值。
                // cv::saturate_cast模板函數其大致原理如下：
                // if (data < 0){
                //     data = 0;
                // }else if (data > 255){
                //     data = 255;
                // }
                // 
                // 對比度 a = g_nContrastValue * 0.01，一般為了觀察的效果，它的取值為0.0到3.0的浮點值，但是軌跡條一般取值都會取整數，因此我們會將
                // g_nContrastValue設到0~300間的整數型，並且在後面乘以一個0.01，這樣就完成了軌跡條中300個不同取值的變化。

            }
        }
    }

    // 顯示影像
    cv::imshow("Original", g_srcImage);
    cv::imshow("Processed Image", g_dstImage);
}