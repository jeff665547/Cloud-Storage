# include <opencv2/opencv.hpp>
# include <opencv2/highgui.hpp>
# include <opencv2/imgproc.hpp>
# include <iostream>

/* Global variable declaration  */
cv::Mat g_srcImage, g_dstImage, g_midImage;
std::vector<cv::Vec4i> g_lines; // 定義一個向量結構用於存放得到的線段向量集合
int g_nthreshold = 100;  // 變數接收的Trackbar位置參數

/* Global function declaration */
static void on_HoughLines(int, void*); // callback function

int main(){

    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";

    // Load the raw image.
    cv::Mat g_srcImage = cv::imread(wd + "NFS01.jpg");

    // Show the raw image.
    cv::imshow("Original", g_srcImage);

    // Setup the tracebar
    cv::namedWindow("Processed", 1);
    cv::createTrackbar("value", "Processed", &g_nthreshold, 200, on_HoughLines);

    // Edge detection and convert to the gray scale image.
    cv::Canny(g_srcImage, g_midImage, 50, 200, 3);  // Canny edge detection.
    cv::cvtColor(g_midImage, g_dstImage, cv::COLOR_GRAY2BGR);  // Convert to the gray scale after the edge detection.

    // Use the callback function.
    on_HoughLines(g_nthreshold, 0);
    cv::HoughLinesP(g_midImage, g_lines, 1, CV_PI/180, 80, 50, 10);

    // Show the processed image.
    cv::imshow("Processed", g_dstImage);

    cv::waitKey(0);

    return 0;
}

static void on_HoughLines(int, void*){
    // Define the global variable
    cv::Mat dstImage = g_dstImage.clone();
    cv::Mat midImage = g_midImage.clone();

    // Use the HoughLinesP()
    std::vector<cv::Vec4i> mylines;
    cv::HoughLinesP(midImage, mylines, 1, CV_PI/180, g_nthreshold + 1, 50, 10);

    // 循環瀏覽繪製每一條線段
    for(size_t i = 0; i < mylines.size(); i++){
        cv::Vec4i l = mylines[i];
        cv::line(dstImage, cv::Point(l[0], l[1]), cv::Point(l[2], l[3]), cv::Scalar(23, 180, 55), 1, cv::LINE_AA);
    }

    // show the image
    cv::imshow("Processed", dstImage);
}