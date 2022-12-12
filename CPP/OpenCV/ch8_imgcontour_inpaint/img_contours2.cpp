// 此程式利用了影像平滑技術(blur函數)和邊緣檢測技術(canny())，
// 根據滑動軸的調整，可以動態地檢測出圖形的輪廓。
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

# define WINDOW_NAME1 "Original"
# define WINDOW_NAME2 "Contour"

/* Global Variable Declaraion */
cv::Mat g_srcImage;
cv::Mat g_grayImage;
int g_nThresh = 80;
int g_nThresh_max = 255;
cv::RNG g_rng(12345);
cv::Mat g_cannyMat_output;
std::vector<std::vector<cv::Point>> g_vContours;
std::vector<cv::Vec4i> g_vHierarchy;

/* Global Function Declaration */
static void ShowHelpText();
void on_ThreshChange(int, void *);

int main(){

    // 顯示歡迎和說明文字
    ShowHelpText();
    
    // Load the source image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch8_imgcontour_inpaint/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);
    if(!g_srcImage.data){
        std::cout << "Loading failed!" << std::endl;
        return false;
    }

    // Convert to the gray scale and denoise.
    cv::cvtColor(g_srcImage, g_grayImage, cv::COLOR_BGR2GRAY);
    cv::blur(g_grayImage, g_grayImage, cv::Size(3, 3));

    // Initialized the window
    cv::namedWindow(WINDOW_NAME1, cv::WINDOW_AUTOSIZE);
    cv::imshow(WINDOW_NAME1, g_srcImage);

    // Setup the trackbar and Initialization.
    cv::createTrackbar("canny thresh", WINDOW_NAME1, &g_nThresh, g_nThresh_max, on_ThreshChange);
    on_ThreshChange(0, 0);

    cv::waitKey(0);

    return(0);
}

void on_ThreshChange(int, void*){
    // Canny Edge detection.
    cv::Canny(g_grayImage, g_cannyMat_output, g_nThresh, g_nThresh*2, 3);

    // Find the contour
    cv::findContours(g_cannyMat_output, g_vContours, g_vHierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE, cv::Point(0, 0));

    // Draw the contour
    cv::Mat drawing = cv::Mat::zeros(g_cannyMat_output.size(), CV_8UC3);
    for(int i = 0; i < g_vContours.size(); i++){
        cv::Scalar color = cv::Scalar(g_rng.uniform(0, 255), g_rng.uniform(0, 255), g_rng.uniform(0, 255), g_rng.uniform(0, 255)); // any value
        cv::drawContours(drawing, g_vContours, i, color, 2, 8, g_vHierarchy, 0, cv::Point());
    }

    // Show the processed image
    cv::imshow(WINDOW_NAME2, drawing);

}

static void ShowHelpText(){
    std::cout << "\tWelcome" << std::endl;
    std::cout << "\tOpenCV version: " << CV_VERSION << std::endl << std::endl;
    std::cout << "\tPress any button - exit the program." << std::endl;
    std::cout << "\tScroll the slider - change the threshold." << std::endl << std::endl;
}