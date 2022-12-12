/* CH7 Image Transformation */
// Ch6 各種對影像的操作都用於增強、修改或者"處理"影像，使之成為類似旦全新的影像。
// 而在 CH7 中關注的重點是影像變換(image transformation)，
// 即將一幅影像轉變為影像資料的另一種表現形式。
// 變換最常見的例子就是傅立葉轉換(Fourier Transformation)，
// 即將影像轉換成來源影像資料的另一種表示形式。
// 這類操作結果仍然儲存為OpenCV影像結構的形式，
// 但是對於新影像的每個單獨像素表示原始輸出影像的頻譜分量，
// 而不是通常所考慮的空間分量。

/* Sobel運算元的使用 */
# include <opencv2/opencv.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){

    // 0. 建立 grad_x 和 grad_y 矩陣
    cv::Mat grad_x, grad_y;
    cv::Mat abs_grad_x, abs_grad_y, dst;

    // 1. Load the original plot.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    cv::Mat src = cv::imread(wd + "NFS01.jpg");

    // 2. Show the original plot.
    cv::imshow("Original Sobel Edge Detection.", src);

    // 3. 求x方向梯度
    cv::Sobel(src, grad_x, CV_16S, 1, 0, 3, 1, 1, cv::BORDER_DEFAULT);
    cv::convertScaleAbs(grad_x, abs_grad_x);
    cv::imshow("Processed X direction Sobel", abs_grad_x);

    // 4. 求y方向梯度
    cv::Sobel(src, grad_y, CV_16S, 0, 1, 3, 1 ,1, cv::BORDER_DEFAULT);
    cv::convertScaleAbs(grad_y, abs_grad_y);
    cv::imshow("Processed Y direction Sobel", abs_grad_y);

    // 5. 合併梯度(近似)
    cv::addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0, dst);
    cv::imshow("Processed All directions of Sobel", dst);

    cv::waitKey(0);

    return 0;
}