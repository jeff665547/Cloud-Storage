/* 各種濾波的示範程式 */
# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

/* Global Variable Declaratioin */
cv::Mat g_srcImage, g_dstImage1, g_dstImage2, g_dstImage3, g_dstImage4, g_dstImage5;
int g_nBoxFilterValue = 6;  // 方框濾波
int g_nMeanBlurValue = 10;  // 均值濾波核心值
int g_nGaussianBlurValue = 6;  // 高斯濾波核心值
int g_nMedianBlurValue = 10;  // 中值濾波參數值
int g_nBilateralFilterValue = 10;  // 雙邊濾波參數值

/* Global Function Declaration */
// Trackbar callback function
static void on_BoxFilter(int, void *);  // 方框濾波
static void on_MeanBlur(int, void *);  // 均值塊濾波器
static void on_GaussianBlur(int, void *);  // 高斯濾波器
static void on_MedianBlur(int, void *);  // 中值濾波器
static void on_BilateralFilter(int, void *);  // 雙邊濾波器

/* main() function */
int main(){
    
    system("color 5E");

    // Load the original plot
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);
    if(!g_srcImage.data){
        std::cout << "Read the srcImage failed!" << std::endl;
        return false;
    }

    // Copy the original plot to the 4 cv::Mat.
    g_dstImage1 = g_srcImage.clone();
    g_dstImage2 = g_srcImage.clone();
    g_dstImage3 = g_srcImage.clone();
    g_dstImage4 = g_srcImage.clone();
    g_dstImage5 = g_srcImage.clone();

    // Show the original plot.
    cv::namedWindow("<0> Original", 1);
    cv::imshow("<0> Original", g_srcImage);

    /* <1> 方框濾波 */
    cv::namedWindow("<1> BoxFilter", 1);
    // Create the trackbar
    cv::createTrackbar("kernel:", "<1> BoxFilter", &g_nBoxFilterValue, 50, on_BoxFilter);
    on_BoxFilter(g_nBoxFilterValue, 0);
    
    /* <2> 均值濾波 */
    cv::namedWindow("<2> MeanBlur", 1);
    // Create the trackbar
    cv::createTrackbar("kernel:", "<2> MeanBlur", &g_nMeanBlurValue, 50, on_MeanBlur);
    on_MeanBlur(g_nMeanBlurValue, 0);

    /* <3> 高斯濾波 */
    cv::namedWindow("<3> GaussianBlur", 1);
    // Create the trackbar
    cv::createTrackbar("kernel:", "<3> GaussianBlur", &g_nGaussianBlurValue, 50, on_GaussianBlur);
    on_GaussianBlur(g_nGaussianBlurValue, 0);

    /* <4> 中值濾波 */
    cv::namedWindow("<4> MedianBlur", 1);
    // Create the trackbar
    cv::createTrackbar("Param:", "<4> MedianBlur", &g_nMedianBlurValue, 50, on_MedianBlur);
    on_MedianBlur(g_nMedianBlurValue, 0);

    /* <5> 雙邊濾波 */
    cv::namedWindow("<5> BilateralFilter", 1);
    // Create the trackbar
    cv::createTrackbar("Param:", "<5> BilateralFilter", &g_nBilateralFilterValue, 50, on_BilateralFilter);
    on_BilateralFilter(g_nBilateralFilterValue, 0);
    
    while (char(cv::waitKey(1)) != 'q') {}

    return 0;
}

static void on_BoxFilter(int, void *){
    // 方框濾波操作
    cv::boxFilter(g_srcImage, g_dstImage1, -1, cv::Size(g_nBoxFilterValue + 1, g_nBoxFilterValue + 1));
    // Show the image.
    cv::imshow("<1> BoxFilter", g_dstImage1);
}

static void on_MeanBlur(int, void *){
    cv::blur(g_srcImage, g_dstImage2, cv::Size(g_nMeanBlurValue + 1, g_nMeanBlurValue + 1), cv::Point(-1, -1));
    cv::imshow("<2> MeanBlur", g_dstImage2);
}

static void on_GaussianBlur(int, void *){
    cv::GaussianBlur(g_srcImage, g_dstImage3, cv::Size(g_nGaussianBlurValue*2 + 1, g_nGaussianBlurValue*2 + 1), 0, 0);
    cv::imshow("<3> GaussianBlur", g_dstImage3);
}

static void on_MedianBlur(int, void *){
    cv::medianBlur(g_srcImage, g_dstImage4, g_nMedianBlurValue*2 + 1);
    cv::imshow("<4> MedianBlur", g_dstImage4);
}

static void on_BilateralFilter(int, void *){
    cv::bilateralFilter(g_srcImage, g_dstImage5, g_nBilateralFilterValue, g_nBilateralFilterValue*2, g_nBilateralFilterValue/2);
    cv::imshow("<5> BilateralFilter", g_dstImage5);
}

// 從結果可以看出方框濾波和均值濾波效果很相似，中值濾波對原圖顛覆很大，而雙邊濾波和原圖差別不大，要仔細看才看得出效果。
