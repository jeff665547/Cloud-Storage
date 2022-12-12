# include <opencv2/imgproc.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

/* Global Variable Declaration */
cv::Mat g_srcImage, g_dstImage;  // 原始圖和效果圖
int g_nElementShape = cv::MORPH_RECT;  // 元素結構的形狀

// 變數接收的TrackBar位置參數
int g_nMaxIteratioinNum = 10;
int g_nOpenCloseNum = 0;
int g_nErodeDilateNum = 0;
int g_nTopBlackHatNum = 0;

/* Global Function Declaration */
static void on_OpenClose(int, void *); // callback function
static void on_ErodeDilate(int, void *); // Callback function
static void on_TopBlackHat(int, void *); // Callback function
static void ShowHelpText();  // Showing instruction.

/* main() */
int main(){

    // Load the original image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");

    if( !g_srcImage.data ){
        std::cout << "Load the srcImage failed! " << std::endl;
        return false;
    }

    cv::namedWindow("Original");
    cv::imshow("Original", g_srcImage);

    // Initalized three windows
    cv::namedWindow("Open/Closed", 1);
    cv::namedWindow("Erode/Dilate", 1);
    cv::namedWindow("Top Hat/Black Hat", 1);

    // Definition
    g_nOpenCloseNum = 9;
    g_nErodeDilateNum = 9;
    g_nTopBlackHatNum = 2;

    // Create the trackbar for each three window.
    cv::createTrackbar("Shift", "Open/Closed", &g_nOpenCloseNum, g_nMaxIteratioinNum*2 + 1, on_OpenClose);
    cv::createTrackbar("Shift", "Erode/Dilate", &g_nErodeDilateNum, g_nMaxIteratioinNum*2 + 1, on_ErodeDilate);
    cv::createTrackbar("Shift", "Top Hat/Black Hat", &g_nTopBlackHatNum, g_nMaxIteratioinNum*2 + 1, on_TopBlackHat);

    while(1){
        int c;

        // call back function
        on_OpenClose(g_nOpenCloseNum, 0);
        on_ErodeDilate(g_nErodeDilateNum, 0);
        on_TopBlackHat(g_nTopBlackHatNum, 0);

        // Get the keypad.
        c = cv::waitKey(0);

        // 按下鍵盤按鍵Q或者ESC，程式退出
        if( (char) c == 'q' || (char) c == 27 )
            break;
        // 按下鍵盤按鍵1，使用橢圓(Elliptic)結構元素MORPH_ELLIPSE
        // 鍵盤按鍵1的ASCII碼為49
        if( (char) c == 49 ) 
            g_nElementShape = cv::MORPH_ELLIPSE;
        // 按下鍵盤按鍵2，使用矩形(Rectangle)結構元素MORPH_RECT
        // 鍵盤按鍵2的ASCII碼為50
        else if( (char) c == 50)
            g_nElementShape = cv::MORPH_RECT;
        // 按下鍵盤按鍵3，使用十字形(Cross-shaped)結構元素MORPH_CROSS
        // 鍵盤按鍵3的ASCII碼為51
        else if( (char) c == 51)
            g_nElementShape = cv::MORPH_CROSS;
        // 按下鍵盤按鍵space，在矩形、橢圓、十字形結構元素中迴圈
        else if( (char) c == ' ')
            g_nElementShape = (g_nElementShape + 1) % 3;
    }

    return 0;
}

static void on_OpenClose(int, void *){
    // The definition of shift.
    int offset = g_nOpenCloseNum - g_nMaxIteratioinNum; // Shift amount.
    int Absolute_offset = offset > 0 ? offset : -offset; // Absolute value of the shift amount.
    // Customized the kernel.
    cv::Mat element = cv::getStructuringElement(g_nElementShape, cv::Size(Absolute_offset*2 + 1, Absolute_offset*2 + 1),
                                                cv::Point(Absolute_offset, Absolute_offset));
    // Close operation
    if(offset < 0){
        // OpenCV 2
        // cv::morphologyEx(g_srcImage, g_dstImage, CV_MOP_OPEN, element);
        // OpenCV 3
        cv::morphologyEx(g_srcImage, g_dstImage, cv::MORPH_OPEN, element);
    }else{
        // OpenCV 2
        // cv::morphologyEx(g_srcImage, g_dstImage, CV_MOP_CLOSE, element);        
        // OpenCV 3
        cv::morphologyEx(g_srcImage, g_dstImage, cv::MORPH_CLOSE, element);
    }
    // Show the processed result.
    cv::imshow("Open/Closed", g_dstImage);
}

static void on_ErodeDilate(int, void *){
    // The definition of shift.
    int offset = g_nErodeDilateNum - g_nMaxIteratioinNum; // Shift amount.
    int Absolute_offset = offset > 0 ? offset : -offset; // Absolute value of the shift amount.
    // Customized the kernel.
    cv::Mat element = cv::getStructuringElement(g_nElementShape, cv::Size(Absolute_offset*2 + 1, Absolute_offset*2 + 1),
                                                cv::Point(Absolute_offset, Absolute_offset));
    // Close operation
    if(offset < 0){
        cv::erode(g_srcImage, g_dstImage, element);
    }else{
        cv::dilate(g_srcImage, g_dstImage, element);
    }
    // Show the processed result.
    cv::imshow("Erode/Dilate", g_dstImage);
}

static void on_TopBlackHat(int, void *){
    // The definition of shift.
    int offset = g_nTopBlackHatNum - g_nMaxIteratioinNum; // Shift amount.
    int Absolute_offset = offset > 0 ? offset : -offset; // Absolute value of the shift amount.
    // Customized the kernel.
    cv::Mat element = cv::getStructuringElement(g_nElementShape, cv::Size(Absolute_offset*2 + 1, Absolute_offset*2 + 1),
                                                cv::Point(Absolute_offset, Absolute_offset));
    // Close operation
    if(offset < 0){
        cv::morphologyEx(g_srcImage, g_dstImage, cv::MORPH_TOPHAT, element);
    }else{
        cv::morphologyEx(g_srcImage, g_dstImage, cv::MORPH_BLACKHAT, element);
    }
    // Show the processed result.
    cv::imshow("Top Hat/Black Hat", g_dstImage);
}