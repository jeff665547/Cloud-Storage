// 直條圖均衡化
// 1. 直條圖均衡化是透過拉伸影像像素強度直條圖的分布範圍來增強影像對比度的一種方法。(用演算法使直條圖大致均衡)
// 2. 均衡化的本質是擴大了量化區隔，而量化級別反而減少了。
//    因此，原來灰階不同的像素經處理後可能變得相同，形成一片相同的灰階區域，
//    各區域之間有明顯的邊界，形成偽輪廓。
// 3. 在原始影像對比度本來就很高的情況下，如果再均衡化則灰階調和，對比度會降低。
// 4. 在泛白緩和的影像中，均衡化會合併一些像素灰階，從而增大對比度。
// 5. 均衡化後的圖片在均衡化則影像不會有任何變化。
// 
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){

    // [1] Load the source image.
    cv::Mat srcImage, dstImage;
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    srcImage = cv::imread(wd + "NFS01.jpg", 1);
    if(!srcImage.data){
        std::cout << "Load failed. Please make sure the files exist." << std::endl;
        return false;
    }

    // [2] Convert to the gray scale image and show the image.
    cv::cvtColor(srcImage, srcImage, cv::COLOR_BGR2GRAY);
    cv::imshow("Original", srcImage);

    // [3] 進行直條圖均衡化
    cv::equalizeHist(srcImage, dstImage);

    // [4] Show the result
    cv::imshow("Equalized Histogram", dstImage);

    // Wait the keypad pressed and exit the program.
    cv::waitKey(0);

    return 0;
}