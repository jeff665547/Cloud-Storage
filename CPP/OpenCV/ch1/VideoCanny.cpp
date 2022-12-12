#include <opencv2\opencv.hpp>

int main(){
    // 從攝影機讀入視訊
    cv::VideoCapture capture(0);

    cv::Mat edges;

    // 迴圈顯示每一幅
    while (1){
        
        // 1. Load the image
        cv::Mat frame; // 定義一個Mat變數，用於儲存每一幅的影像
        capture >> frame; // 讀取現在幅

        // 2. Convert the camera video into gray video.
        cv::cvtColor(frame, edges, CV_BGR2GRAY); // convert the BGR colorful image into gray image

        // 3. 使用3x3核心來降噪 ( 2 x 3 + 1 = 7)
        cv::blur(edges, edges, cv::Size(7, 7)); // 進行模糊

        // 4. 進行canny邊緣檢測並顯示
        cv::Canny(edges, edges, 0, 30, 3);

        cv::imshow("raw video (canny):", frame); // 顯示現在原始幅
        cv::imshow("processed video (canny):", edges); // 顯示現在處理過的幅
        if (cv::waitKey(30) >= 0) break; // 延時30ms
    }

    return 0;
}