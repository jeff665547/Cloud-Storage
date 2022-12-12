# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){
    // Load the raw image and define the Mat.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg");
    cv::Mat midImage, dstImage;

    // Canny edge detection and convert to the gray scale.
    cv::Canny(srcImage, midImage, 50, 200, 3);  // canny edge detection.
    cv::cvtColor(midImage, dstImage, cv::COLOR_GRAY2BGR);  // convert to the gray scale image after edge detection.

    // Hough transformation
    std::vector<cv::Vec4i> lines;
    cv::HoughLinesP(midImage, lines, 1, CV_PI/180, 80, 50, 10);

    // Draw each lines in the plot.
    for(size_t i = 0; i < lines.size(); i++){
        cv::Vec4i l = lines[i];
        cv::line(dstImage, cv::Point(l[0], l[1]), cv::Point(l[2], l[3]), cv::Scalar(186, 88, 255), 1, cv::LINE_AA);
    }

    // Show the original plot.
    cv::imshow("Original", srcImage);

    // Show the plot after the edge detection.
    cv::imshow("edge detection", midImage);

    // Show the processed image.
    cv::imshow("Processed", dstImage);

    cv::waitKey(0);
    
    return 0;
}