/* 反向投影 (back projection) */
// 如果一幅影像的區域中顯示的是一種結構紋理或者一個獨特的物體，
// 那麼這個區域的直條圖可以看做一個機率函數，
// 其表現形式是某個像素屬於該紋理或物體的機率。
// 反向投影(back projection)就是一種紀錄給定影像中的像素點
// 如何適應直條圖模型像素分布方式的一種方法。
# include <opencv2/imgproc/imgproc.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <iostream>

#define WINDOW_NAME1 "Original"

/* Global Variable Declaration */
cv::Mat g_srcImage; cv::Mat g_hsvImage; cv::Mat g_hueImage;
int g_bins = 30; // 直條圖組距

/* Global Function Declaration */
void on_BinChange(int, void*);

int main(){

    // Load the image and convert to the hsv space.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch9_imghist_matching/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);
    if(!g_srcImage.data){
        std::cout << "Loading failed!" << std::endl;
        return false;
    }
    cv::cvtColor(g_srcImage, g_hsvImage, cv::COLOR_BGR2HSV);

    // 分離Hue通道
    g_hueImage.create(g_hsvImage.size(), g_hsvImage.depth());

    int ch[ ] = {0, 0};
    cv::mixChannels(&g_hsvImage, 1, &g_hueImage, 1, ch, 1);

    // 建立trackbar來輸入bin的數目
    cv::namedWindow(WINDOW_NAME1, cv::WINDOW_AUTOSIZE);
    cv::createTrackbar("Hue group", WINDOW_NAME1, &g_bins, 180, on_BinChange);
    on_BinChange(0, 0); // 進行一次初始化

    // 顯示效果圖
    cv::imshow(WINDOW_NAME1, g_srcImage);

    cv::waitKey(0);

    return 0;
}

void on_BinChange(int, void*){

    // Parameter preparation
    cv::MatND hist;
    int histSize = MAX(g_bins, 2);
    float hue_range[] = {0, 180};
    const float*ranges = {hue_range};

    // Compute the histogram and normaized
    cv::calcHist(&g_hueImage, 1, 0, cv::Mat(), hist, 1, &histSize, &ranges, true, false);
    cv::normalize(hist, hist, 0, 255, cv::NORM_MINMAX, -1, cv::Mat());

    // Compute the back projection.
    cv::MatND backproj;
    cv::calcBackProject(&g_hueImage, 1, 0, hist, backproj, &ranges, 1, true);

    // Show the back projection.
    cv::imshow("Back Projection", backproj);

    // 繪製直條圖的參數準備
    int w = 400; int h = 400;
    int bin_w = cvRound((double) w / histSize);
    cv::Mat histImg = cv::Mat::zeros(w, h, CV_8UC3);

    // 繪製直條圖
    for(int i = 0; i < g_bins; i++){
        cv::rectangle(histImg, cv::Point(i*bin_w, h), 
            cv::Point((i+1)*bin_w, h - cvRound(hist.at<float>(i)*h/255.0)), 
            cv::Scalar(100, 123, 255), -1);
    }

    // 顯示直條圖視窗
    cv::imshow("histogram", histImg);

}