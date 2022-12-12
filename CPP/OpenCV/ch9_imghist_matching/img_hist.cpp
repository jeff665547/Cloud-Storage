// 影像直條圖(histogram)
// * 直條圖是影像中像素強度分布的圖形表達方式
// * 它統計了每一個強度值所具有的像素個數
// 影像直條圖不局限於統計顏色灰階，而是可以統計任何影像特徵，如梯度、方向等。
// 直條圖的參數：
// 1. dims: 需要統計的特徵數，在灰階影像中的dims = 1，是因為我們僅僅統計了灰階值(灰階影像)。
// 2. bins: 每個特徵空間子區段的數目，可譯為"直條"或"組距"。
// 3. range: 每個特徵空間的取值範圍。e.g. range = [0, 255]。
// 以下範例說明如何計算彩色影像的色相，飽和度二維直條圖。 (Hue-Saturation histogram)
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){

    // Load the source image, convert into HSV color model.
    cv::Mat srcImage, hsvImage;
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch9_imghist_matching/";
    srcImage = cv::imread(wd + "logo.jpg");
    cv::cvtColor(srcImage, hsvImage, cv::COLOR_BGR2HSV);

    // Parameter preparation
    // 將色相量化為30個等級，將飽和度量化為32個等級
    int hueBinNum = 30;  // 色相的直條圖直條數量
    int saturationBinNum = 32;  // 飽和度的直條圖直條數量
    int histSize[] = {hueBinNum, saturationBinNum};
    // 定義色相的變化範圍從0到179
    float hueRanges[] = {0, 180};
    // 定義飽和度的變化範圍為0(黑、白、灰)到255(純光譜顏色)
    float saturationRanges[] = {0, 256};
    const float * ranges[] = {hueRanges, saturationRanges};
    cv::MatND dstHist;
    // 參數準備，calcHist函數中將計算第0通道和第1通道的直條圖
    int channels[] = {0, 1};

    // 正式使用calcHist，進行直條圖計算
    cv::calcHist(&hsvImage,   // Input Array
                 1,           // 陣列個數為1
                 channels,    // 通道(channel)索引
                 cv::Mat(),   // 不使用遮罩
                 dstHist,     // 輸出的目標直條圖
                 2,           // 需要計算的直條圖的維度為2
                 histSize,    // 存放每個維度的直條圖尺寸的陣列
                 ranges,      // 每一維數值的取值範圍陣列
                 true,        // 指示直條圖是否均勻的識別字，true表示均勻地直條圖
                 false);      // 累計識別字，false表示直條圖在設定階段會被清零。

    // 為繪製直條圖準備參數
    double maxValue = 0;  // Maximum
    cv::minMaxLoc(dstHist, 0, &maxValue, 0, 0); // 查詢陣列和子陣列的全域最小值和最大值存入maxValue中
    int scale = 10;
    cv::Mat histImg = cv::Mat::zeros(saturationBinNum*scale, hueBinNum*10, CV_8UC3);

    // 雙層迴圈，進行直條圖繪製
    for(int hue = 0; hue < hueBinNum; hue++){
        for(int saturation = 0; saturation < saturationBinNum; saturation++){
            float binValue = dstHist.at<float>(hue, saturation); // 直條圖直條的值
            int intensity = cvRound(binValue*255/maxValue); // 亮度

            // 進行繪製
            cv::rectangle(histImg, cv::Point(hue*scale, saturation*scale), 
                cv::Point((hue+1)*scale - 1, (saturation+ 1 )*scale - 1),
                cv::Scalar::all(intensity), cv::FILLED);
        }

        // Show the processed image
        cv::imshow("Material Plot", srcImage);
        cv::imshow("H-S histogram", histImg);

        cv::waitKey(0);
    }

    return 0;
}