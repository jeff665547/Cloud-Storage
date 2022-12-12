# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>
# define WINDOW_NAME1 "Original"
# define WINDOW_NAME2 "Processed"

/* Global variable declaration */
cv::Mat g_srcImage;
cv::Mat g_grayImage;
int g_nThresh = 50; // threshold
int g_nMaxThresh = 255; // threshold maximum
cv::RNG g_rng(12345); // random generator

/* Global function declaration */
void on_ContoursChanged(int, void*);
static void ShowHelpText();

int main(){
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch8_imgcontour_inpaint/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");
    if(!g_srcImage.data){
        std::cout << "Loading failed!" << std::endl;
        return false;
    }

    // conver into gray scale and blur the image.
    cv::cvtColor(g_srcImage, g_grayImage, cv::COLOR_BGR2GRAY);
    cv::blur(g_grayImage, g_grayImage, cv::Size(3, 3));

    // Show the original image and show
    cv::namedWindow(WINDOW_NAME1, cv::WINDOW_AUTOSIZE);
    cv::imshow(WINDOW_NAME1, g_srcImage);

    // Set the trackbar and use the call back function 
    cv::createTrackbar("Threshold: ", WINDOW_NAME1, &g_nThresh, g_nMaxThresh, on_ContoursChanged);
    on_ContoursChanged(0, 0);

    cv::waitKey(0);

    return(0);
}

void on_ContoursChanged(int, void*){
    // Define some parameter
    cv::Mat threshold_output;
    std::vector<std::vector<cv::Point>> contours;
    std::vector<cv::Vec4i> hierarchy;

    // Use the threshold to detect the edge.
    cv::threshold(g_grayImage, threshold_output, g_nThresh, 255, cv::THRESH_BINARY);

    // Find the contour.
    cv::findContours(threshold_output, contours, hierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE, cv::Point(0, 0));

    // 多邊形逼近輪廓 + 取得矩形和圓形邊界框
    std::vector<std::vector<cv::Point>> contours_poly(contours.size());
    std::vector<cv::Rect> boundRect(contours.size());
    std::vector<cv::Point2f> center(contours.size());
    std::vector<float> radius(contours.size());

    // 一個迴圈，瀏覽所有部分，進行本程式最核心的操作
    for(unsigned int i = 0; i < contours.size(); i++){
        cv::approxPolyDP(cv::Mat(contours[i]), contours_poly[i], 3, true); // 用指定精度逼近多邊形曲線
        boundRect[i] = cv::boundingRect(cv::Mat(contours_poly[i])); // 計算點集的最外面(up-right)矩形邊界
        cv::minEnclosingCircle(contours_poly[i], center[i], radius[i]);  // 對給定的2D點集，尋找最小面積的包圍圓形
    }

    // 繪製多邊形輪廓 + 包圍的矩形框 + 圓形框
    cv::Mat drawing = cv::Mat::zeros(threshold_output.size(), CV_8UC3);
    for(int unsigned i = 0; i < contours.size(); i++){
        cv::Scalar color = cv::Scalar(g_rng.uniform(0, 255), g_rng.uniform(0, 255), g_rng.uniform(0, 255)); // 隨機設定顏色
        cv::drawContours(drawing, contours_poly, i, color, 1, 8, std::vector<cv::Vec4i>(), 0, cv::Point()); // 繪製輪廓
        cv::rectangle(drawing, boundRect[i].tl(), boundRect[i].br(), color, 2, 8, 0); // 繪製矩形
        cv::circle(drawing, center[i], (int)radius[i], color, 2, 8, 0); // 繪製圓形
    }

    // 顯示效果圖視窗
    cv::namedWindow(WINDOW_NAME2, cv::WINDOW_AUTOSIZE);
    cv::imshow(WINDOW_NAME2, drawing);
}