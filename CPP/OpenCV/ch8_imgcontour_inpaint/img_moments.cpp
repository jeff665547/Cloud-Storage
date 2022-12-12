/* 影像的矩 */
// 矩函數在影像分析中有著廣泛的應用，如模式識別、目標分類、目標識別、與方位估計、影像編碼與重構等。
// 一個從一幅數位圖形中計算出來的矩集，通常描述了該影像檔案形狀的全域特徵，
// 並提供了大量的關於該影像不同類型的幾何特性資訊。
// 比如大小、位置、方向集形狀等。
// 零階矩求面積
// 一階矩與形狀有關(一階矩確定重心、質心)，
// 二階矩顯示曲線圍繞直線平均值的擴展程度(二階矩確定主方向)。
// 三階矩則是關於平均值的對稱性的測量。
// 由二階矩和三階矩可以匯出一組共7個不變矩。
// 而不變矩是影像的統計特性，滿足平移、伸縮、旋轉均不變的不變性，
// 在影像識別領域(工業應用和模式識別)得到了廣泛的應用。
// 一個影像的矩由moments、contourArea、arcLength這三個函數配合求取。
// *使用moments計算影像的所有矩。
// *使用contourArea計算輪廓面積。
// *使用arcLength計算輪廓或曲線長度。
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

# define WINDOW_NAME1 "Original" 
# define WINDOW_NAME2 "Image Contour" 

cv::Mat g_srcImage; cv::Mat g_grayImage;
int g_nThresh = 100;
int g_nMaxThresh = 255;
cv::RNG g_rng(12345);
cv::Mat g_cannyMat_output;
std::vector<std::vector<cv::Point>> g_vContours;
std::vector<cv::Vec4i> g_vHierarchy;

/* Global variable declaration */
void on_ThreshChange(int, void*);
static void ShowHelpText();

int main(){
    // Load the original image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch8_imgcontour_inpaint/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");

    // Convert to the gray scale.
    cv::cvtColor(g_srcImage, g_grayImage, cv::COLOR_BGR2GRAY);
    cv::blur(g_grayImage, g_grayImage, cv::Size(3, 3));

    // Initialize the window
    cv::namedWindow(WINDOW_NAME1, cv::WINDOW_AUTOSIZE);
    cv::imshow(WINDOW_NAME1, g_srcImage);

    // create the trackbar and initilize
    cv::createTrackbar("Threshold", WINDOW_NAME1, &g_nThresh, g_nMaxThresh, on_ThreshChange);
    on_ThreshChange(0, 0);

    cv::waitKey(0);
    return 0;
}

void on_ThreshChange(int, void *){

    // Canny Edge Detection
    cv::Canny(g_grayImage, g_cannyMat_output, g_nThresh, g_nThresh*2, 3);

    // Find the contour
    cv::findContours(g_cannyMat_output, g_vContours, g_vHierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE, cv::Point(0, 0));

    // 計算矩
    std::vector<cv::Moments> mu(g_vContours.size());
    for(unsigned int i = 0; i < g_vContours.size(); i++){
        mu[i] = cv::moments(g_vContours[i], false);
    }

    // 計算中心矩
    std::vector<cv::Point2f> mc(g_vContours.size());
    for(unsigned int i = 0; i < g_vContours.size(); i++){
        mc[i] = cv::Point2f(static_cast<float>(mu[i].m10/mu[i].m00), static_cast<float>(mu[i].m01/mu[i].m00));
    }

    // 繪製輪廓
    cv::Mat drawing = cv::Mat::zeros(g_cannyMat_output.size(), CV_8UC3);
    for(unsigned int i = 0; i < g_vContours.size(); i++){
        cv::Scalar color = cv::Scalar(g_rng.uniform(0, 255), g_rng.uniform(0, 255), g_rng.uniform(0, 255)); // random generate the color.
        cv::drawContours(drawing, g_vContours, i, color, 2, 8, g_vHierarchy, 0, cv::Point()); // 繪製外層和內層輪廓
        cv::circle(drawing, mc[i], 4, color, -1, 8, 0);  // 繪製圓
    }

    // 顯示到視窗中
    cv::namedWindow(WINDOW_NAME2, cv::WINDOW_AUTOSIZE);
    cv::imshow(WINDOW_NAME2, drawing);

    // 透過m00計算輪廓面積
    std::cout << "output: area and contour length." << std::endl;
    for(unsigned int i = 0; i < g_vContours.size(); i++){
        printf(" > compute the contour area of [%d] by m00: (M_00) = %.2f\n   The area compute by the OpenCV function is %.2f, length: %.2f \n\n", 
                i, mu[i].m00, contourArea(g_vContours[i]), cv::arcLength(g_vContours[i], true));
        cv::Scalar color = cv::Scalar(g_rng.uniform(0, 255), g_rng.uniform(0, 255), g_rng.uniform(0, 255));
        cv::drawContours(drawing, g_vContours, i, color, 2, 8, g_vHierarchy, 0, cv::Point());
        cv::circle(drawing, mc[i], 4, color, -1, 8, 0);
    }
}