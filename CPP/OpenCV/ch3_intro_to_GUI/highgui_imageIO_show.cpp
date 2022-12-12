# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>

int main(){

    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch3_intro_to_GUI/";

    /* 1. Image Loading and Showing. */
    cv::Mat evoque = cv::imread(wd + "evoque.jpg"); // 影像載到Mat
    cv::namedWindow("[1] car");  // 建立一個名為"[1] car"的視窗
    cv::imshow("[1] car", evoque);  // 顯示名為"[1] car"的視窗


    /* 2. Image Mixture 初級影像混合 */
    cv::Mat image = cv::imread(wd + "evoque.jpg");
    cv::Mat logo = cv::imread(wd + "logo.jpg");

    // 載入後先顯示
    cv::namedWindow("[2] original");
    cv::imshow("[2] original", image);

    cv::namedWindow("[3] logo");
    cv::imshow("[3] logo", logo);

    // 定義一個Mat類型，用於存放影像的ROI
    cv::Mat imageROI;
    // method I
    imageROI = image(cv::Rect(0, 320, logo.cols, logo.rows));
    // method II
    // imageROI = image(cv::Range(350, 350 + logo.rows), Range(800, 800 + logo.cols));

    // 將logo加到原圖上
    cv::addWeighted(imageROI, 0.5, logo, 0.8, 0., imageROI);

    // Show the results
    cv::namedWindow("[4] original + logo");
    cv::imshow("[4] original + logo", image);

    /* 3. Image Output 影像的輸出 */
    cv::imwrite("car_and_logo.jpg", image);
    cv::waitKey(0);
    
    return 0;
}