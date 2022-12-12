# include <opencv2/highgui/highgui.hpp> // OpenCV highgui 模組標頭檔
# include <opencv2/imgproc/imgproc.hpp> // OpenCV 影像處理標頭檔
int main(){
    // Setup the wd.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch1/";

    // Load the raw image
    cv::Mat srcImage = cv::imread(wd + "paybackposter.jpg");
    // Show the raw image
    cv::imshow("[raw image] Erosion", srcImage);
    // Erode the raw image 影像侵蝕: 用影像中的暗色部分"腐蝕"影像中的高亮部分。
    cv::Mat element = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(15, 15));
    cv::Mat dstImage;
    cv::erode(srcImage, dstImage, element);
    // Show the erosion effect
    cv::imshow("[processed image] Erosion", dstImage);
    // Close until some key be pressed.
    cv::waitKey(0);

    return 0;
}