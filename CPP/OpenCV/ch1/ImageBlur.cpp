# include "opencv2/highgui/highgui.hpp"
# include "opencv2/imgproc/imgproc.hpp"

int main(){
    
    // Setup the wd.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch1/";

    // Loaded the raw image
    cv::Mat srcImage = cv::imread(wd + "paybackposter.jpg");

    // Show the raw image 
    cv::imshow("[raw image] blur", srcImage);

    // Blur the raw image 影像模糊: 對影像進行均值濾波操作。
    cv::Mat dstImage;
    cv::blur(srcImage, dstImage, cv::Size(7, 7));

    // Show the processed image
    cv::imshow("[processed image] blur", dstImage);

    cv::waitKey(0);

    return 0;
}