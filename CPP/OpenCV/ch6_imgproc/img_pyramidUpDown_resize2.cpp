# include <iostream>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <opencv2/opencv.hpp>
# define WINDOW_NAME "Programming"

/* Global Variable Declaration */
cv::Mat g_srcImage, g_dstImage, g_tmpImage;

int main(){

    // Load the original image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    g_srcImage = cv::imread(wd + "NFS01.jpg");
    if(!g_srcImage.data){
        std::cout << "Load the srcImage failed!" << std::endl;
        return false;
    }

    // Initialized the window
    cv::namedWindow(WINDOW_NAME, CV_WINDOW_AUTOSIZE);

    g_tmpImage = g_srcImage;
    g_dstImage = g_tmpImage;

    int key = 0;

    // 輪詢取得按鍵資訊
    while(1){
        key = cv::waitKey(9);  // 讀取鍵值到key變數中

        // 根據key變數的值，進行不同的操作
        switch(key){
            // ============================ Exit the Program ======================================
            case 27:  // Press ESC
                return 0;
                break;
            case 'q':
                return 0;
                break;
            // ============================ Image Amplificatioin ======================================
            case 'a':
                cv::pyrUp(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols*2, g_tmpImage.rows*2));
                std::cout << "Keypad 'A' is pressed, amplified the image based on the pyrUp(). Image size x 2 " << std::endl;
                break;
            case 'w':
                cv::resize(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols*2, g_tmpImage.rows*2));
                std::cout << "Keypad 'W' is pressed, amplified the image based on the resize(). Image size x 2 " << std::endl;
                break;
            case '1':
                cv::resize(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols*2, g_tmpImage.rows*2));
                std::cout << "Keypad '1' is pressed, amplified the image based on the resize(). Image size x 2 " << std::endl;
                break;
            case '3':
                cv::pyrUp(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols*2, g_tmpImage.rows*2));
                std::cout << "Keypad '3' is pressed, amplified the image based on the pyrUp(). Image size x 2 " << std::endl;
                break;
            // ============================ Image Shrinkage ======================================
            case 'd':
                cv::pyrDown(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols/2, g_tmpImage.rows/2));
                std::cout << "Keypad 'D' is pressed, shrink the image based on the pyrDown(). Image size / 2 " << std::endl;
                break;
            case 's':
                cv::resize(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols/2, g_tmpImage.rows/2));
                std::cout << "Keypad 'S' is pressed, shrink the image based on the resize(). Image size / 2 " << std::endl;
                break;
            case '2':
                cv::resize(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols/2, g_tmpImage.rows/2), (0, 0), (0, 0), 2);
                std::cout << "Keypad '2' is pressed, shrink the image based on the resize(), Image size / 2 " << std::endl;
                break;
            case '4':
                cv::pyrDown(g_tmpImage, g_dstImage, cv::Size(g_tmpImage.cols/2, g_tmpImage.rows/2));
                std::cout << "Keypad '4' is pressed, shrink the image based on the pyrDown(). Image size / 2 " << std::endl;
                break;
        }

        // Show the image after the operation
        cv::imshow(WINDOW_NAME, g_dstImage);

        // Assign the g_dstImage to g_tmpImage
        g_tmpImage = g_dstImage;
    }
    

    return 0;
}