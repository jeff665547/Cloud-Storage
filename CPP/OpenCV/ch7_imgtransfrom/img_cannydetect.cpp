/* CH7 Image Transformation */
// Ch6 各種對影像的操作都用於增強、修改或者"處理"影像，使之成為類似旦全新的影像。
// 而在 CH7 中關注的重點是影像變換(image transformation)，
// 即將一幅影像轉變為影像資料的另一種表現形式。
// 變換最常見的例子就是傅立葉轉換(Fourier Transformation)，
// 即將影像轉換成來源影像資料的另一種表示形式。
// 這類操作結果仍然儲存為OpenCV影像結構的形式，
// 但是對於新影像的每個單獨像素表示原始輸出影像的頻譜分量，
// 而不是通常所考慮的空間分量。

/* Canny 邊緣檢測 */
# include <opencv2/opencv.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){
    // Load the original plot.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    cv::Mat src = cv::imread(wd + "NFS01.jpg");
    cv::Mat src1 = src.clone();

    // Show the original plot.
    cv::imshow("Original Canny Edge Detection.", src);

    // Canny 用法，轉成灰階圖，降噪，用canny，最後將得到的邊緣作為遮罩，
    // 拷貝原圖到效果圖上，得到彩色的邊緣圖。
    cv::Mat dst, edge, gray;

    // 1. 建立與src同類型和大小的矩陣(dst)
    dst.create(src1.size(), src1.type());

    // 2. 將原影像轉換為灰階影像
    cv::cvtColor(src1, gray, cv::COLOR_BGR2GRAY);

    // 3. 先用使用3 x 3 kernel降噪
    cv::blur(gray, edge, cv::Size(3, 3));

    // 4. 執行Canny運算元
    cv::Canny(edge, edge, 3, 9, 3);

    // 5. 將g_dstImage內的所有元素設定為0
    dst = cv::Scalar::all(0);

    // 6. 使用Canny運算元輸出的邊緣圖g_cannyDetectedEdge作為遮罩，來將原圖
    //    原圖g_srcImage拷貝到目標圖g_dstImage中
    src1.copyTo(dst, edge);

    // 7. Show the processed image.
    cv::imshow("Processed: Canny Edge Detection", dst);

    cv::waitKey(0);

    return 0;
}