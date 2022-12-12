# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>
# define WINDOW_NAME1 "Original"
# define WINDOW_NAME2 "Processed"

/* Global Variable Declaration */
cv::Mat g_srcImage;
cv::Mat g_grayImage;
int g_nThresh = 50;
int g_maxThresh = 255;
cv::RNG g_rng(12345);
cv::Mat srcImage_copy = g_srcImage.clone();
cv::Mat g_thresholdImage_output;
std::vector<std::vector<cv::Point>> g_vContours;
std::vector<cv::Vec4i> g_vHierarchy;

/* Global Function Declarartion */
static void ShowHelpText();
void on_ThreshChange(int, void *);

int main(){

    // Load the raw image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch8_imgcontour_inpaint/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);

    // convert to the gray scale and blur.
    cv::cvtColor(g_srcImage, g_grayImage, cv::COLOR_BGR2GRAY);
    cv::blur(g_grayImage, g_grayImage, cv::Size(3, 3));

    // Show the image.
    cv::namedWindow(WINDOW_NAME1, cv::WINDOW_AUTOSIZE);
    cv::imshow(WINDOW_NAME1, g_srcImage);

    // Setup the trackbar
    cv::createTrackbar(" Threshold:", WINDOW_NAME1, &g_nThresh, g_maxThresh, on_ThreshChange);
    on_ThreshChange(0, 0);  // Initializaion

    cv::waitKey(0);
    return(0);
}

void on_ThreshChange(int, void*){
    // 對影像進行二值化，控制閾值
    cv::threshold(g_grayImage, g_thresholdImage_output, g_nThresh, 255, cv::THRESH_BINARY);

    // Find the contour
    cv::findContours(g_thresholdImage_output, g_vContours, g_vHierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE, cv::Point(0, 0));

    // View each contour and find the convex hull.
    std::vector<std::vector<cv::Point>>hull(g_vContours.size());
    for(unsigned int i = 0; i < g_vContours.size(); i++){
        cv::convexHull(cv::Mat(g_vContours[i]), hull[i], false);
    }

    // Draw the contour and the convex hull
    cv::Mat drawing = cv::Mat::zeros(g_thresholdImage_output.size(), CV_8UC3);
    for(unsigned int i = 0; i < g_vContours.size(); i++){
        cv::Scalar color = cv::Scalar(g_rng.uniform(0, 255), g_rng.uniform(0, 255), g_rng.uniform(0, 255));
        cv::drawContours(drawing, g_vContours, i, color, 1, 8, std::vector<cv::Vec4i>(), 0, cv::Point());
        cv::drawContours(drawing, hull, i, color, 1, 8, std::vector<cv::Vec4i>(), 0, cv::Point());
    }

    // Show the processed image
    cv::imshow(WINDOW_NAME2, drawing);
}