/* 閾值化 */
// 閾值可以被視為最簡單的影像分割方法。
// 如，從一幅影像中利用閾值分割出我們需要的物體部分(這裡的物體可以是一部分或者整體)，也可以用來去除雜訊。
// 這樣的影像分割方法基於影像中物體與背景之間的灰階差異，而且此分割屬於像素級的分割。
// 為了從一幅影像中提取出我們需要的部分，應該用影像中的每一個樣素點的灰階值與選取的閾值進行比較，並做出相應的判斷。
// 一旦找到了需要分割的物體的像素點，可以對這些像素點設定一些特定的值來表示。
// 如，可以將該物體的像素點的灰階值設定為"0"(黑色)，其他的像素點的灰階值設定為"255"(白色)。
// 當然像素點的灰階值可以任意，但最好設定的兩種顏色對比度較強，以方便觀察其結果。
// 在OpenCV中，Threshold()和adaptiveThreshold()(自我調整閾值操作)可以完成這些要求。
// 它們的基本思想是：給定一個陣列和一個閾值，然後根據陣列中的每個元素的值是高於還是低於閾值而進行一些處理。

# include "opencv2/imgproc/imgproc.hpp"
# include "opencv2/highgui/highgui.hpp"
# include <iostream>

# define WINDOW_NAME "Programming"

// Declaration for the global variable
int g_nThresholdValue = 100;
int g_nThresholdType = 3;
cv::Mat g_srcImage, g_grayImage, g_dstImage;

// Declaration for the global function
static void ShowHelpText(); 
void on_Threshold(int, void*);  // callback function

int main(){

    // 1. Load the image
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");

    if(!g_srcImage.data){
        std::cout << "Load the image faild!" << std::endl;
        return false;
    }

    // 2. 存留一份原圖的灰階圖
    cv::cvtColor(g_srcImage, g_grayImage, cv::COLOR_RGB2GRAY);

    // 3. 建立視窗並且顯示原圖
    cv::namedWindow(WINDOW_NAME, cv::WINDOW_AUTOSIZE);

    // 4. 建立滑動條來控制閾值
    cv::createTrackbar("Mode: ", WINDOW_NAME, &g_nThresholdType, 4, on_Threshold);

    cv::createTrackbar("Param: ", WINDOW_NAME, &g_nThresholdValue, 255, on_Threshold);

    // 5. 初始化自訂的閾值回呼函數
    on_Threshold(0, 0);

    // 6. 輪詢等待使用者按鍵，如果ESC鍵按下則退出程式
    while(1){
        int key;
        key = cv::waitKey(20);
        if((char)key == 27){ break; }
    }

    return 0;
}

void on_Threshold(int, void *){

    // Use the threshold function
    cv::threshold(g_grayImage, g_dstImage, g_nThresholdValue, 255, g_nThresholdType);
    // param 1: 輸入陣列，填單色板，8或32位浮點類型的cv::Mat
    // param 2: 函式呼叫的運算結果存放處，且和param 1中的cv::Mat有一樣的尺寸和類型。
    // param 3: double 類型的thresh，閾值的具體值。
    // param 4: double 類型的maxval。當param 5參數閾值型別為CV_THRESH_BINARY or CV_THRESH_BINARY_INV時，公式裡會用到的參數
    // param 5: 閾值型別。
    //        0, cv::THRESH_BINARY, (二進制閾值)
    //            dst(x, y) = {maxval, if src(x, y) > thresh.   0, otherwise.
    //        1, cv::THRESH_BINARY_INV, (返二進制閾值)
    //            dst(x, y) = {0, if src(x, y) > thresh.   maxval, otherwise.
    //        2, cv::THRESH_TRUNC, (截斷閾值)
    //            dst(x, y) = {threshold, if src(x, y) > thresh.   src(x, y), otherwise.
    //        3, cv::THRESH_TOZERO, (閾值化)
    //            dst(x, y) = {src(x, y), if src(x, y) > thresh.   0, otherwise.
    //        4, cv::THRESH_TOZERO_INV, (反閾值化)
    //            dst(x, y) = {0, if src(x, y) > thresh.   src(x, y), otherwise.

    // Update the processed plot.
    cv::imshow(WINDOW_NAME, g_dstImage);
}