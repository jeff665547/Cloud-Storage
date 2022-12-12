# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){

    // Load the raw image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg");
    cv::Mat midImage, dstImage;

    // Edge Detection and convert to the gray scale.
    cv::Canny(srcImage, midImage, 50, 200, 3); // Canny detection.
    cv::cvtColor(midImage, dstImage, CV_GRAY2BGR);  // Convert the plot to the gray scale after edge detection.

    // Hough detection
    std::vector<cv::Vec2f> lines;  // Define a vector structure lines to store the lines.
    cv::HoughLines(midImage, lines, 1, CV_PI/180,  150, 0, 0);

    std::cout << lines.size() << std::endl;

    // 依次在圖中繪製出每條線段
    for(size_t i = 0; i < lines.size(); i++){
        float rho = lines[i][0], theta = lines[i][1];
        cv::Point pt1, pt2;
        double a = cos(theta), b = sin(theta);
        double x0 = a*rho, y0 = b*rho;
        pt1.x = cvRound(x0 + 1000*(-b));
        pt1.y = cvRound(y0 + 1000*(a));
        pt2.x = cvRound(x0 - 1000*(-b));
        pt2.y = cvRound(y0 - 1000*(a));
        cv::line(dstImage, pt1, pt2, cv::Scalar(55, 100, 195), 1, cv::LINE_AA);
    }

    // Show the original image
    cv::imshow("Original", srcImage);

    // Show the image after edge detection
    cv::imshow("edge detection", midImage);

    // Show the processed plot
    cv::imshow("processed", dstImage);

    cv::waitKey(0);
    
    return 0;
}