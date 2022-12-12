#include <opencv2/opencv.hpp>
#include <iostream>

int main(){
    
    // Show image
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch1/";
    
    // 1. Read an image
    cv::Mat img = cv::imread(wd + "paybackposter.jpg");
    // 2. Show the image in the window
    cv::imshow("Need For Speed Payback", img);
    // 3. Wait 6000 ms and auto closed
    cv::waitKey(6000);

    return 0;

}