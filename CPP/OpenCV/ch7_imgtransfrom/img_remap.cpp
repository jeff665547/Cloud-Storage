# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

// 重映射，就是把一幅影像中某位置的像素放置另一張圖片指定位置的過程。
// dst(x, y) = src(map_x(x, y), map_y(x, y))
//  g(x, y)  =  f( h(x, y) ),   g(x, y) is the dstImage function, f(.) is the srcImage function, 
//  and h(x, y) is the mapping functioin ranging from x and y.
// 
// e.g. h(x, y) = (I.cols - x, y). Suppose that I.cols = 5, h(x, y) = (I.cols - x, y) = (5 - x, y)
// g(5, 0) = f(5 - 5, 0) = f(0, 0), 左右翻轉
// 

int main(){

    // Define the variables.
    cv::Mat srcImage, dstImage;
    cv::Mat map_x, map_y;

    // Load the raw image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    srcImage = cv::imread(wd + "NFS01.jpg", 1);

    if(!srcImage.data){
        printf("Load the image failed! Please make sure the image exist.");
        return false;
    }
    cv::imshow("Original", srcImage);

    // Construct an image that mimic the original image. x 重映射圖，y 重映射圖
    dstImage.create(srcImage.size(), srcImage.type());
    map_x.create(srcImage.size(), CV_32FC1);
    map_y.create(srcImage.size(), CV_32FC1);

    // 瀏覽每一個像素點，改變map_x & map_y的值
    for(int j = 0; j < srcImage.rows; j++){
        for(int i = 0; i < srcImage.cols; i++){
            // 改變map_x & map_y的值
            map_x.at<float>(j, i) = static_cast<float>(i);
            map_y.at<float>(j, i) = static_cast<float>(srcImage.rows - j);
        }
    }

    // 進行重映射操作
    cv::remap(srcImage, dstImage, map_x, map_y, cv::INTER_LINEAR, cv::BORDER_CONSTANT, cv::Scalar(0, 0, 0));
    cv::imshow("Processed", dstImage);
    cv::waitKey(0);

    return 0;
}