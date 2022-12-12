/* 此範例程式最後編譯的結果有兩個滑動軸，
   第一個滑動軸為"腐蝕/膨脹"，
   用於在腐蝕/膨脹之間進行切換；
   第二個滑動軸為"核心尺寸(kernel size)"，
   用於調節形態學操作時的核心尺寸，
   以得到效果不同的影像。*/
# include <opencv2/opencv.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

/* Global Variable Declaration */
cv::Mat g_srcImage, g_dstImage;  // 原始圖和效果圖
int g_nTrackbarNumber = 0;  // 0 表示腐蝕erode，1 表示膨脹dilate
int g_nStructElementSize = 3;  // 結構元素(kernel核心矩陣的尺寸)

/* Global Functioin Declaration */
void Process();  //膨脹和腐蝕的處理函數
void on_TrackbarNumChange(int, void *);  // callback function.
void on_ElementSizeChange(int, void *);  // callback function.

/* main() function */
int main(){
    system("color 5E");

    // Load the raw image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");
    if(!g_srcImage.data){
        std::cout << "Load the srcImage failed! " << std::endl;
        return false;
    }

    // Show the original plot.
    cv::namedWindow("Original");
    cv::imshow("Original", g_srcImage);

    // Initialize the first erode and show the processed effect.
    cv::namedWindow("Processed");
    cv::imshow("Original", g_srcImage);

    // Get the customized kernel.
    cv::Mat element = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(2*g_nStructElementSize+1, 2*g_nStructElementSize+1),
                                                cv::Point(g_nStructElementSize, g_nStructElementSize));
    
    cv::erode(g_srcImage, g_dstImage, element);
    cv::imshow("Processed", g_dstImage);

    // Create the trackbar
    cv::createTrackbar("Erode/Dilate", "Processed", &g_nTrackbarNumber, 1, on_TrackbarNumChange);
    cv::createTrackbar("Kernel size", "Processed", &g_nStructElementSize, 21, on_ElementSizeChange);

    // Use while tho get the information from the keypad, if we press 'q', exit the program.
    while(char(cv::waitKey(1)) != 'q') { }

    return 0;
}

void Process(){
    // Get the customized kernel
    cv::Mat element = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(2*g_nStructElementSize+1, 2*g_nStructElementSize + 1), 
                                                cv::Point(g_nStructElementSize, g_nStructElementSize));

    // Erode or Dilate
    if(g_nTrackbarNumber == 0 ){
        cv::erode(g_srcImage, g_dstImage, element);
    }else{
        cv::dilate(g_srcImage, g_dstImage, element);
    }
    // Show the processed result.
    cv::imshow("Processed", g_dstImage);
}

void on_TrackbarNumChange(int, void *){
    // 腐蝕和膨脹之間效果已經切換，回呼函數體內需用一次Process()，使改變後的效果立即生效並且顯示出來。
    Process();
}

void on_ElementSizeChange(int, void *){
    // Kernel尺寸已改變，callback function 內需使用一次Process函數，使改變後的效果立即生效並顯示出來
    Process();
}