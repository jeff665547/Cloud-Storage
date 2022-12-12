// createTrackbar() 用於建立一個可以調整數值的滑動軸(常常也被稱軌跡條)，
// 並將滑動軸附加到指定的視窗上，使用起來很方便。
// 它往往會和一個回呼函數配合來使用。
// int createTrackbar(const string& trackbarname, const string& winname, 
// int* value, int count, TrackbarCallback onChange = 0, void* userdata = 0);
// param 1: trackbar，軌跡條的名字，用來代表我們建立的軌跡條。
// param 2: winname，視窗的名字，表示這個軌跡條會依附到哪個視窗上，
//          即對應namedWindow()建立視窗時填的某一個視窗名稱。
// param 3: value，一個指向整數型的指標，表示滑桿的位置。
//          在建立時，滑桿的初始位置就是該變數現在的值。
// param 4: count，表示滑桿可以達到的最大位置的值。
// param 5: TrackbarCallback 類型的 onChange，它有預設值0。這是一個指向回呼函數的指標，
//          每次滑桿位置改變時，這個函數都會進行回檔。並且這個函數的原型必須是
//          void XXXX(int, void*);，其中第一個參數是軌跡條的位置，第二個參數代表任何類型
//          的資料的指針都可以賦值給void*，此處存放使用者資料(看param 6)。如果回檔是NULL指標，
//          則表示沒有回呼函數的使用，僅第三個參數value有變化。
// param 6: userdata，預設值為0。這個參數是使用者傳給回呼函數的資料，用來處理軌跡條事件。
//          如果使用的第三個參數value參數是全域變數的話，完全可以不去管這個userdata參數。

// getTrackbarpos()，它用於取得現在軌跡條的位置。
// int getTrackbarPos(conststring& trackbarname, conststring& winname);
// trackbarname表示軌跡條的名字。
// winname表示父視窗的名稱。

# include <opencv2/opencv.hpp>
# include "opencv2/highgui/highgui.hpp"
# include <iostream>
using namespace cv;

# define WINDOW_NAME "Linear Mixture" // 為視窗標題定義的巨集


/* Declare Global Variable */
const int g_nMaxAlphaValue = 100; // Maximum of Alpha.
int g_nAlphaValueSlider; // Corresponding Slider value.
double g_dAlphaValue;
double g_dBetaValue;

// Declare image variable
cv::Mat g_srcImage1;
cv::Mat g_srcImage2;
cv::Mat g_dstImage;

/* on_Trackbar() */
void on_Trackbar(int aa, void* bb){

    std::cout << aa << std::endl;
    std::cout << bb << std::endl;

    // 求出現在alpha值相對於最大值的比例
    g_dAlphaValue = (double) g_nAlphaValueSlider / g_nMaxAlphaValue;
    // 則beta值為1減去alpha值
    g_dBetaValue = ( 1.0 - g_dAlphaValue );

    // 根據alpha和beta值進行線性混合
    cv::addWeighted(g_srcImage1, g_dAlphaValue, g_srcImage2, g_dBetaValue, 0.0, g_dstImage);

    // Show the image
    cv::imshow(WINDOW_NAME, g_dstImage);
}


/* main() */
int main(int argc, char** argv){

    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch3_intro_to_GUI/";

    // loaded image (the size of the two images should be the same.)
    g_srcImage1 = cv::imread(wd + "NFS01.jpg");
    g_srcImage2 = cv::imread(wd + "NFS02.jpg");

    if(!g_srcImage1.data){
        std::cout << "Image 1 does not exit. Please make sure the image exist.";
        return -1;
    }

    if(!g_srcImage2.data){
        std::cout << "Image 2 does not exit. Please make sure the image exist.";
        return -1;
    }

    cv::imshow("Image 1", g_srcImage1);
    cv::imshow("Image 2", g_srcImage2);
    // Image 1 以及 Image 2 需要相同 size。

    // Set the initial value of the slider (70)
    g_nAlphaValueSlider = 70;

    // Set the window
    cv::namedWindow(WINDOW_NAME, 1);

    // Set the slider in the assigned window
    char TrackbarName[50];
    sprintf(TrackbarName, "Transparent %d", g_nMaxAlphaValue);  //  write a formatted string to character string buffer. 格式化輸出變數
    // int sprintf( char* buffer, const char* format, ...)

    cv::createTrackbar(TrackbarName, WINDOW_NAME, &g_nAlphaValueSlider, g_nMaxAlphaValue, on_Trackbar);
    // int createTrackbar(const string& trackbarname, const string& winname, 
    // int* value, int count, TrackbarCallback onChange = 0, void* userdata = 0);

    // Print the result in the call back function in the initialization stage.
    on_Trackbar(g_nAlphaValueSlider, 0);

    // Press any button to exit
    cv::waitKey(0);

    return 0;
}