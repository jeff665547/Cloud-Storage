# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>

int main(){

    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    cv::Mat srcImage = cv::imread(wd + "circle.jpg");
    cv::Mat midImage, dstImage;

    cv::imshow("original", srcImage);

    // Convert the image to the gray scale and blur the image.
    cv::cvtColor(srcImage, midImage, cv::COLOR_BGR2GRAY); // convert the plot to the gray scale.
    cv::GaussianBlur(midImage, midImage, cv::Size(9, 9), 2, 2);
    cv::imshow("midImage", midImage);

    // Hough Transformation
    std::vector<cv::Vec3f> circles;
    cv::HoughCircles(midImage, circles, cv::HOUGH_GRADIENT, 1.5, 10, 200, 100, 0, 0);

    // Draw in the image.
    for(size_t i = 0; i < circles.size(); i++){
        // Define the parameter.
        cv::Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
        int radius = cvRound(circles[i][2]);

        // Draw the center of the circle.
        cv::circle(srcImage, center, 3, cv::Scalar(0, 255, 0), -1, 8, 0);

        // Draw the shape of the circle.
        cv::circle(srcImage, center, radius, cv::Scalar(155, 50, 255), 3, 8, 0);
    } 
    
    // Show the image.
    cv::imshow("Processed", srcImage);

    cv::waitKey(0);

    return 0;
}