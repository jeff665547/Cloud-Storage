# include <iostream>
# include "opencv2/core/core.hpp"
# include "opencv2/highgui/highgui.hpp"
# include "opencv2/imgproc/imgproc.hpp"

/* Global Variable Declaration */
cv::Mat g_srcImage, g_dstImage1, g_dstImage2, g_dstImage3; // 儲存圖片的Mat類型
int g_nBoxFilterValue = 3;  // 方框濾波參數值
int g_nMeanBlurValue = 3;  // 均值濾波參數值
int g_nGaussinaBlurValue = 3;  // 高斯濾波參數值


/* Global Function Declaration */
static void on_BoxFilter(int, void *);   // 方框濾波
static void on_MeanBlur(int, void *);    // 均值濾波
static void on_GaussianBlur(int, void *);   // 高斯濾波

int main(){

    // Load the original image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);
    if (!g_srcImage.data){
        std::cout << "Read the srcImage failed!" << std::endl;
        return false;
    }

    // 複製原圖到三個Mat類型中
    g_dstImage1 = g_srcImage.clone();
    g_dstImage2 = g_srcImage.clone();
    g_dstImage3 = g_srcImage.clone();

    // 顯示原圖
    cv::namedWindow("<0> Original", 1);
    cv::imshow("<0> Original", g_srcImage);
    // cv::waitKey(0);




    // 方框濾波
    cv::namedWindow("<1> Box Filter", 1);
    // Create the trackbar.
    cv::createTrackbar("kernal size:", "<1> Box Filter", &g_nBoxFilterValue, 40, on_BoxFilter);
    on_BoxFilter(g_nBoxFilterValue, 0);
    // cv::imshow("<1> Box Filter", g_dstImage1);


    // 均值濾波
    cv::namedWindow("<2> Blur Filter", 1);
    // Create the trackbar.
    cv::createTrackbar("kernal size:", "<2> Blur Filter", &g_nMeanBlurValue, 40, on_MeanBlur);
    on_MeanBlur(g_nMeanBlurValue, 0);
    // cv::imshow("<2> Mean Blur", g_dstImage2);


    // 高斯濾波
    cv::namedWindow("<3> Gaussian Filter", 1);
    // Create the trackbar.
    cv::createTrackbar("Kernal size:", "<3> Gaussian Filter", &g_nGaussinaBlurValue, 40, on_GaussianBlur);
    on_GaussianBlur(g_nGaussinaBlurValue, 0);
    // cv::imshow("<3> Gaussian Filter", g_dstImage3);

    // Output some information
    std::cout << std::endl << "\t Move the trackbar and observe the image precessed effect." << std::endl;
    std::cout << "Press 'q' to exit the program." << std::endl;
    while(char(cv::waitKey(1)) != 'q'){ }

    return 0;
}


/* on_BoxFilter() function */
static void on_BoxFilter(int, void *){
    // 方框濾波操作
    cv::boxFilter(g_srcImage, g_dstImage1, -1, cv::Size(g_nBoxFilterValue + 1, g_nBoxFilterValue + 1));
    // 顯示視窗
    cv::imshow("<1> Box Filter", g_dstImage1);
}

/* on_MeanFilter() function */
static void on_MeanBlur(int, void *){
    // 均值濾波操作
    cv::blur(g_srcImage, g_dstImage2, cv::Size(g_nMeanBlurValue + 1, g_nMeanBlurValue + 1), cv::Point(-1, -1));
    // 顯示視窗
    cv::imshow("<2> Blur Filter", g_dstImage2);
}

/* on_GaussianBlur() function */
static void on_GaussianBlur(int, void *){
    // 高斯濾波操作
    cv::GaussianBlur(g_srcImage, g_dstImage3, cv::Size(g_nGaussinaBlurValue*2 + 1, g_nGaussinaBlurValue*2 + 1), 0, 0);
    // 顯示視窗
    cv::imshow("<3> Gaussian Filter", g_dstImage3);
}
