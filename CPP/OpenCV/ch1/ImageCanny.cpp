# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>

int main(){

    // Setup the wd.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch1/";

    // Loaded the raw image
    cv::Mat srcImage = cv::imread(wd + "paybackposter.jpg");

    // Show the raw image 
    cv::imshow("[raw image] canny", srcImage);

    // Define the parameter
    cv::Mat dstImage, edge, grayImage; 

    // 1. 建立與src同類型和大小的矩陣 (dst)
    dstImage.create(srcImage.size(), srcImage.type());

    // 2. 將影像轉為灰階影像
    cv::cvtColor(srcImage, grayImage, CV_BGR2GRAY);

    // 3. 先使用3x3核心來降噪
    cv::blur(grayImage, edge, cv::Size(3, 3));

    // 4. 執行Canny運算元
    cv::Canny(edge, edge, 3, 9, 3);

    // 5. 顯示效果圖
    cv::imshow("[processed image] canny", edge);

    cv::waitKey(0);

    return 0;
}