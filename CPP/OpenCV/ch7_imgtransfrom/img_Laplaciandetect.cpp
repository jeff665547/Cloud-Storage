/* CH7 Image Transformation */
// Ch6 各種對影像的操作都用於增強、修改或者"處理"影像，使之成為類似旦全新的影像。
// 而在 CH7 中關注的重點是影像變換(image transformation)，
// 即將一幅影像轉變為影像資料的另一種表現形式。
// 變換最常見的例子就是傅立葉轉換(Fourier Transformation)，
// 即將影像轉換成來源影像資料的另一種表示形式。
// 這類操作結果仍然儲存為OpenCV影像結構的形式，
// 但是對於新影像的每個單獨像素表示原始輸出影像的頻譜分量，
// 而不是通常所考慮的空間分量。

/* Laplacian 運算元的使用 */
# include <opencv2/opencv.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){

    // 0. Variable Definition
    cv::Mat src, src_gray, dst, abs_dst;

    // 1. Load the original plot.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    src = cv::imread(wd + "NFS01.jpg");

    // 2. Show the original plot.
    cv::imshow("Original Sobel Edge Detection.", src);

    // 3. 使用高斯濾波消除雜訊
    cv::GaussianBlur(src, src, cv::Size(3, 3), 0, 0, cv::BORDER_DEFAULT);

    // 4. 轉為灰階圖
    cv::cvtColor(src, src_gray, cv::COLOR_BGR2GRAY);

    // 5. 使用Laplace函數
    cv::Laplacian(src_gray, dst, CV_16S, 3, 1, 0, cv::BORDER_REFLECT101);

    // 6. 計算絕對值，並將結果轉換為8位元
    cv::convertScaleAbs(dst, abs_dst);

    // 7. 顯示效果圖
    cv::imshow("Processed Laplacian", abs_dst);

    cv::waitKey(0);

    return 0;
}