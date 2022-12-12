# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

/* Define the Macro */
# define WINDOW_NAME "Window"

/* Global Variable declaration */
cv::Mat g_srcImage, g_dstImage;
cv::Mat g_map_x, g_map_y;

/* Global function declaration */
int update_map(int key);
static void ShowHelpText(); // 輸出說明文字

int main(){

    // Show the Help text.
    ShowHelpText();

    // Load the original plot.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);
    if(!g_srcImage.data){
        std::cout << "Loading image failed." << std::endl;
        return false;
    }
    cv::imshow("Original", g_srcImage);

    // 建立和原始圖一樣的效果圖，x為重映射圖，y為重映射圖
    g_dstImage.create(g_srcImage.size(), g_srcImage.type());
    g_map_x.create(g_srcImage.size(), CV_32FC1);
    g_map_y.create(g_srcImage.size(), CV_32FC1);

    // 建立視窗並顯示
    cv::namedWindow(WINDOW_NAME, cv::WINDOW_AUTOSIZE);
    cv::imshow(WINDOW_NAME, g_srcImage);

    // 輪詢按鍵，更新map_x和map_y的值，進行重映射操作並且顯示效果圖
    while(1){
        // 取得鍵盤按鍵
        int key = cv::waitKey(0);

        // 判斷esc是否按下，若按下便退出
        if((key & 255) == 27){
            std::cout << "Program exit ......." << std::endl;
            break;
        }

        // 根據按下的按鍵來更新map_x & map_y的值，然後使用remap()進行重映射
        update_map(key);
        cv::remap(g_srcImage, g_dstImage, g_map_x, g_map_y, cv::INTER_LINEAR, cv::BORDER_CONSTANT, cv::Scalar(0, 0, 0));
        cv::imshow(WINDOW_NAME, g_dstImage);
    }

    return 0;
}

int update_map(int key){
    // 雙層迴圈，瀏覽每個像素點
    std::cout << key << std::endl;
    for(int j = 0; j < g_srcImage.rows; j++){
        for(int i = 0; i < g_srcImage.cols; i++){
            switch(key){
                case 49: // 鍵盤1按下，進行第一種映射操作
                    if (i > g_srcImage.cols*0.25 && i < g_srcImage.cols*0.75 && j > g_srcImage.rows*0.25 && j < g_srcImage.rows*0.75){
                        g_map_x.at<float>(j, i) = static_cast<float>(2*(i - g_srcImage.cols*0.25) + 0.5);
                        g_map_y.at<float>(j, i) = static_cast<float>(2*(j - g_srcImage.rows*0.25) + 0.5);
                    }else{
                        g_map_x.at<float>(j, i) = 0;
                        g_map_y.at<float>(j, i) = 0;
                    }
                    break;
                case 50: // 鍵盤2按下，進行第二種映射操作
                    g_map_x.at<float>(j, i) = static_cast<float>(i);
                    g_map_y.at<float>(j, i) = static_cast<float>(g_srcImage.rows - j);
                    break;
                case 51: // 鍵盤3按下，進行第三種映射操作
                    g_map_x.at<float>(j, i) = static_cast<float>(g_srcImage.cols - i);
                    g_map_y.at<float>(j, i) = static_cast<float>(j);
                    break;
                case 52: // 鍵盤4按下，進行第四種映射操作
                    g_map_x.at<float>(j, i) = static_cast<float>(g_srcImage.cols - i);
                    g_map_y.at<float>(j, i) = static_cast<float>(g_srcImage.rows - j);
                    break;
            }
        }
    }
    return 1;
}

static void ShowHelpText(){
    // Output some information
    std::cout << "\t\t Welcome " << std::endl;
    std::cout << "\t\t Keypad [ESC] - exit the program. " << std::endl;
    std::cout << "\t\t Keypad [1] - The first mapping method " << std::endl;
    std::cout << "\t\t Keypad [2] - The second mapping method " << std::endl;
    std::cout << "\t\t Keypad [3] - The third mapping method " << std::endl;
    std::cout << "\t\t Keypad [4] - The fourth mapping method " << std::endl;
}