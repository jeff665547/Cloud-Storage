#include <opencv2\opencv.hpp>

int main(){
    // Setup the wd.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch1/";

    // Load the video
    // 下面也可以寫成 VideoCapture capture;  capture.open(wd + "paybackvideo.avi")
    // 若要使用opencv來開啟影片，還會牽涉到影片編碼與解碼的問題。
    cv::VideoCapture capture(wd + "paybackvideo.avi"); // 在定義時就直接初始化，如同 int a = 1; 
    // VideoCapture為一種類別。

    // 迴圈顯示每一幅
    while (1){
        cv::Mat frame; // 定義一個Mat變數，用於儲存每一幅的影像
        capture >> frame; // 讀取現在幅

        cv::imshow("Read Video", frame); // 顯示現在幅
        cv::waitKey(30);
    }

    return 0;
}