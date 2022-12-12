# include <opencv2/opencv.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(int argc, char** argv){
    // [1] Load the raw image with binary format.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch8_imgcontour_inpaint/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg", 0);
    cv::imshow("Original", srcImage);

    // [2] Initialize the image
    cv::Mat dstImage = cv::Mat::zeros(srcImage.rows, srcImage.cols, CV_8UC3);

    // [3] srcImage 取大於閾值119的那部分
    srcImage = srcImage > 119;
    cv::imshow("Original (> some threshold)", srcImage);

    // [4] Define contour and 層次結構
    std::vector<std::vector<cv::Point>> contours;
    std::vector<cv::Vec4i> hierarchy;

    // [5] Find the contour
    cv::findContours(srcImage, contours, hierarchy, cv::RETR_CCOMP, cv::CHAIN_APPROX_SIMPLE);

    // [6] 瀏覽所有頂層的輪廓，以隨機顏色繪製出每個連接元件的顏色
    int index = 0;
    for(; index >= 0; index = hierarchy[index][0]){ // 如果沒有對應項，對應的hierarchy值設為負數。並且迴圈終止。
        cv::Scalar color(rand()&255, rand()&255, rand()&255);
        cv::drawContours(dstImage, contours, index, color, cv::FILLED, 8, hierarchy);
    }

    // [7] 顯示最後的輪廓圖
    cv::imshow("Contour of the image.", dstImage);
    cv::waitKey(0);

    return 0;
}