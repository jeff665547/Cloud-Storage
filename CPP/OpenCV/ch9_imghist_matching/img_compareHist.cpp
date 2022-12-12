// 對於直條圖來說，
// 一個不可或缺的工具便是用某些具體的標準來比較兩個直條圖的相似度。
// 一個衡量直條圖相似度的對比標準(d(H_1, H_2))。
// 在這裡使用compareHist()函數來對比兩個直條圖的相似度
// 相似度的度量方式可使用Correlation, Chi-Square test statistic, 
// Intersection, Bhattacharyya distance. 來測量。
// 此範例示範如何使用compareHist()函數進行直條圖對比。
// 程式碼中的cv::MatND類別是用於儲存直條圖的一種資料結構，用法簡單。
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){

    // 宣告儲存基準影像和另外兩張對比影像的矩陣 (RGB & HSV)
    cv::Mat srcImage_base, hsvImage_base;
    cv::Mat srcImage_test1, hsvImage_test1;
    cv::Mat srcImage_test2, hsvImage_test2;
    cv::Mat hsvImage_halfDown;

    // 載入基準影像(srcImage_base)和兩張測試影像srcImage_test1、srcImage_test2，並顯示
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch9_imghist_matching/";
    srcImage_base = cv::imread(wd + "NFS01.jpg", 1);
    srcImage_test1 = cv::imread(wd + "NFS02.jpg", 1);
    srcImage_test2 = cv::imread(wd + "apple1.png", 1);
    // Show the three images.
    cv::imshow("Basis", srcImage_base);
    cv::imshow("test1", srcImage_test1);
    cv::imshow("test2", srcImage_test2);

    // convert the image form RGB into HSV.
    cv::cvtColor(srcImage_base, hsvImage_base, cv::COLOR_BGR2HSV);
    cv::cvtColor(srcImage_test1, hsvImage_test1, cv::COLOR_BGR2HSV);
    cv::cvtColor(srcImage_test2, hsvImage_test2, cv::COLOR_BGR2HSV);

    // 建立包含基準影像下半部的半身影像 (HSV格式)
    hsvImage_halfDown = hsvImage_base(cv::Range(hsvImage_base.rows/2, hsvImage_base.rows - 1), 
                        cv::Range(0, hsvImage_base.cols - 1));

    // 初始化計算直條圖需要的實數參數
    // 對hue通道(channel)使用30個bin，對saturation通道(channel)使用32個bin
    int h_bins = 50; int s_bins = 60;
    int histSize[] = {h_bins, s_bins};
    // hue的取值範圍從0到256，對saturation取值範圍從0到180
    float h_ranges[] = {0, 256};
    float s_ranges[] = {0, 180};
    const float* ranges[] = {h_ranges, s_ranges};
    // 使用第0和第1個通道(channel)
    int channels[] = {0, 1};

    // 建立儲存直條圖的cv::MatND類別的實例
    cv::MatND baseHist;
    cv::MatND halfDownHist;
    cv::MatND testHist1;
    cv::MatND testHist2;

    // 計算基準影像，兩張測試影像，半身基準影像的HSV直條圖
    cv::calcHist(&hsvImage_base, 1, channels, cv::Mat(), baseHist, 2, histSize, ranges, true, false);
    cv::normalize(baseHist, baseHist, 0, 1, cv::NORM_MINMAX, -1, cv::Mat());
    
    cv::calcHist(&hsvImage_halfDown, 1, channels, cv::Mat(), halfDownHist, 2, histSize, ranges, true, false);
    cv::normalize(halfDownHist, halfDownHist, 0, 1, cv::NORM_MINMAX, -1, cv::Mat());

    cv::calcHist(&hsvImage_test1, 1, channels, cv::Mat(), testHist1, 2, histSize, ranges, true, false);
    cv::normalize(testHist1, testHist1, 0, 1, cv::NORM_MINMAX, -1, cv::Mat());

    cv::calcHist(&hsvImage_test2, 1, channels, cv::Mat(), testHist2, 2, histSize, ranges, true, false);
    cv::normalize(testHist2, testHist2, 0, 1, cv::NORM_MINMAX, -1, cv::Mat());

    // 按順序使用4種對比標準將基準影像的直條圖與其餘各直條圖進行對比
    for(int i = 0; i < 4; i++){
        // 進行影像直條圖的對比
        int compare_method = i;
        double base_base = cv::compareHist(baseHist, baseHist, compare_method);
        double base_half = cv::compareHist(baseHist, halfDownHist, compare_method);
        double base_test1 = cv::compareHist(baseHist, testHist1, compare_method);
        double base_test2 = cv::compareHist(baseHist, testHist2, compare_method);

        // 輸出結果
        printf("Method used: [%d], results: \n\n", i);
        printf("[baseline - baseline]:%f, [baseline - half]:%f, [baseline - test1]:%f, [baseline - test2]:%f \n",
                 i, base_base, base_half, base_test1, base_test2);
        printf("------------------------------------------------------------------------------------\n");

    }

    std::cout << std::endl << " 0: Correlation, 1: Chi-Square, 2: Intersection , 3: Bhattacharyya distance" << std::endl;
    // 對於correlation 和 Intersection 標準，值越大表示相似度越高。
    // [baseline - baseline]的匹配數值結果相對於其他匹配方式是最大的。
    // [baseline - half]的匹配度次大，而其他的匹配結果卻不盡如人意。
    printf("End the test.");
    cv::waitKey(0);

    return 0;
}