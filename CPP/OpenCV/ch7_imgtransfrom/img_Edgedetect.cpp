/* CH7 Image Transformation */
// Ch6 各種對影像的操作都用於增強、修改或者"處理"影像，使之成為類似旦全新的影像。
// 而在 CH7 中關注的重點是影像變換(image transformation)，
// 即將一幅影像轉變為影像資料的另一種表現形式。
// 變換最常見的例子就是傅立葉轉換(Fourier Transformation)，
// 即將影像轉換成來源影像資料的另一種表示形式。
// 這類操作結果仍然儲存為OpenCV影像結構的形式，
// 但是對於新影像的每個單獨像素表示原始輸出影像的頻譜分量，
// 而不是通常所考慮的空間分量。

/* Scharr 濾波器 */
# include <opencv2/opencv.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

/* Global Variable Declaration */
cv::Mat g_srcImage, g_srcGrayImage, g_dstImage;


// Canny Edge Detection
cv::Mat g_cannyDetectedEdges;
int g_cannyLowThreshold = 1;  // TrackBar Position

// Sobel Edge Detection
cv::Mat g_sobelGradient_X, g_sobelGradient_Y;
cv::Mat g_sobelAbsGradient_X, g_sobelAbsGradient_Y;
int g_sobelKernelSize = 1;  // Trackbar Position

// Scharr
cv::Mat g_scharrGradient_X, g_scharrGradient_Y;
cv::Mat g_scharrAbsGradient_X, g_scharrAbsGradient_Y;


/* Global Function Declaratioin */
static void on_Canny(int, void*); // Canny Edge Detection window slider call back function.
static void on_Sobel(int, void*); // Sobel Edge Detection window slider call back function.
void Scharr();  // 封裝了Scharr邊緣檢測相關程式碼的函數

int main(){
    
    // Change the color in the console.
    system("color 2F");

    // Load the original image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");
    if(!g_srcImage.data){
        std::cout << "Load the srcImage failed! " << std::endl;
        return  false;
    }

    // Show the original image.
    cv::namedWindow("Original plot");
    cv::imshow("Original plot", g_srcImage);

    // 建立與src同類型和大小的矩陣(dst)
    g_dstImage.create(g_srcImage.size(), g_srcImage.type());

    // 將原影像轉換為灰階影像
    cv::cvtColor(g_srcImage, g_srcGrayImage, cv::COLOR_BGR2GRAY);

    // Construct the showing window.
    cv::namedWindow("Processed Canny Edge Detection", cv::WINDOW_AUTOSIZE);
    cv::namedWindow("Processed Sobel Edge Detection", cv::WINDOW_AUTOSIZE);

    // Contruct the trackbar.
    cv::createTrackbar("Param:", "Processed Canny Edge Detection", &g_cannyLowThreshold, 120, on_Canny);
    cv::createTrackbar("Param:", "Processed Sobel Edge Detection", &g_sobelKernelSize, 3, on_Sobel);

    // Use the callback function.
    on_Canny(0, 0);
    on_Sobel(0, 0);

    // 使用封裝了scharr邊緣檢測程式碼的函數
    Scharr();

    // 輪詢取得按鍵資訊，若按下Q，程式退出
    while((char(cv::waitKey(1)) != 'q')){}

    return 0;
}

/* on_Canny() */
void on_Canny(int, void*){
    // 先使用3 x 3 kernel來 denoise
    cv::blur(g_srcGrayImage, g_cannyDetectedEdges, cv::Size(3, 3));

    // 執行 Canny Operator
    cv::Canny(g_cannyDetectedEdges, g_cannyDetectedEdges, g_cannyLowThreshold, g_cannyLowThreshold*3, 3);

    // 先將g_dstImage內的所有元素設為0
    g_dstImage = cv::Scalar::all(0);

    // 使用Canny運算元輸出的邊緣圖g_cannyDetectedEdges作為遮罩，來將原圖g_srcImage拷貝到目標圖g_dstImage中
    g_srcImage.copyTo(g_dstImage, g_cannyDetectedEdges);

    // Show the processed image.
    cv::imshow("Processed Canny Edge Detection", g_dstImage);
}

/* on_Sobel() */
void on_Sobel(int, void*){
    // 求X方向梯度
    cv::Sobel(g_srcImage, g_sobelGradient_X, CV_16S, 1, 0, (2*g_sobelKernelSize + 1), 1, 1, cv::BORDER_DEFAULT);
    cv::convertScaleAbs(g_sobelGradient_X, g_sobelAbsGradient_X); // 計算絕對值，並將結果轉換成8位元
    // 求Y方向梯度
    cv::Sobel(g_srcImage, g_sobelGradient_Y, CV_16S, 0, 1, (2*g_sobelKernelSize + 1), 1, 1, cv::BORDER_DEFAULT);
    cv::convertScaleAbs(g_sobelGradient_Y, g_sobelAbsGradient_Y); // 計算絕對值，並將結果轉換成8位元
    // 合併梯度
    cv::addWeighted(g_sobelAbsGradient_X, 0.5, g_sobelAbsGradient_Y, 0.5, 0, g_dstImage);
    // Show the processed image.
    cv::imshow("Processed Sobel Edge Detection", g_dstImage);
}

void Scharr(){
    // 求X方向梯度
    cv::Scharr(g_srcImage, g_scharrGradient_X, CV_16S, 1, 0, 1, 0, cv::BORDER_DEFAULT);
    cv::convertScaleAbs(g_scharrGradient_X, g_scharrAbsGradient_X);  // 計算絕對值，並將結果轉換為8位元
    // 求Y方向梯度
    cv::Scharr(g_srcImage, g_scharrGradient_Y, CV_16S, 0, 1, 1, 0, cv::BORDER_DEFAULT);
    cv::convertScaleAbs(g_scharrGradient_Y, g_scharrAbsGradient_Y);  // 計算絕對值，並將結果轉換為8位元

    // 合併梯度
    cv::addWeighted(g_scharrAbsGradient_X, 0.5, g_scharrAbsGradient_Y, 0.5, 0, g_dstImage);

    // Show the processed image
    cv::imshow("Processed Scharr Edge Detection", g_dstImage);
}