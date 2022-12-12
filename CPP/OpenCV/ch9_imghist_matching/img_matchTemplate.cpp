// 模板匹配
// 模板匹配是一項在一幅影像中尋找與另一幅模板影像最匹配(相似)部分的技術。
// 模板匹配由MatchTemplate()函數完成。
// 模板匹配不是基於直條圖的，而是透過在輸入影像上滑動影像塊，
// 對實際的影像塊和輸入影像進行匹配的一種匹配方法。
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>

# define WINDOW_NAME1 "Original"
# define WINDOW_NAME2 "Processed"

/* Global Variable Declaration */
cv::Mat g_srcImage; cv::Mat g_templateImage; cv::Mat g_resultImage;
int g_nMatchMethod;
int g_nMaxTrackbarNum = 5;

/* Global Function Declaration */
void on_Matching(int, void *);

int main(){
    // Load the raw image and template.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch9_imghist_matching/";
    g_srcImage = cv::imread(wd + "NFS01.jpg", 1);
    g_templateImage = cv::imread(wd + "subaru.png", 1);

    // Initialize the window.
    cv::namedWindow(WINDOW_NAME1, cv::WINDOW_AUTOSIZE);
    cv::namedWindow(WINDOW_NAME2, cv::WINDOW_AUTOSIZE);

    // Create the trackbar and initialize the call back function.
    cv::createTrackbar("Method", WINDOW_NAME1, &g_nMatchMethod, g_nMaxTrackbarNum, on_Matching);
    on_Matching(0, 0);

    cv::waitKey(0);

    return 0;
}

void on_Matching(int, void*){
    // Initialize the local variable
    cv::Mat srcImage;
    g_srcImage.copyTo(srcImage);

    // Initialize the output matrix.
    int resultImage_cols = g_srcImage.cols - g_templateImage.cols + 1;
    int resultImage_rows = g_srcImage.rows - g_templateImage.rows + 1;
    g_resultImage.create(resultImage_cols, resultImage_rows, CV_32FC1);

    // templatematching and standardlize
    cv::matchTemplate(g_srcImage, g_templateImage, g_resultImage, g_nMatchMethod);
    cv::normalize(g_resultImage, g_resultImage, 0, 1, cv::NORM_MINMAX, -1, cv::Mat());

    // Find the most suitable position through minMaxLoc
    double minValue; double maxValue; cv::Point minLocation; cv::Point maxLocation;
    cv::Point matchLocation;
    cv::minMaxLoc(g_resultImage, &minValue, &maxValue, &minLocation, &maxLocation, cv::Mat());

    // 對於方法SQDIFF和SQDIFF_NORMED，越小的數值有著更高的匹配結果，而其餘的方法，數值越大匹配效果越好
    if(g_nMatchMethod == cv::TM_SQDIFF || g_nMatchMethod == cv::TM_SQDIFF_NORMED){
        matchLocation = minLocation;
    }else{
        matchLocation = maxLocation;
    }

    // 繪製出矩形，並顯示出最終結果
    cv::rectangle(srcImage, matchLocation, 
        cv::Point(matchLocation.x + g_templateImage.cols, matchLocation.y + g_templateImage.rows), 
        cv::Scalar(0, 0, 255), 2, 8, 0);
    cv::rectangle(g_resultImage, matchLocation, 
        cv::Point(matchLocation.x + g_templateImage.cols, matchLocation.y + g_templateImage.rows), 
        cv::Scalar(0, 0, 255), 2, 8, 0);
    cv::imshow(WINDOW_NAME1, srcImage);
    cv::imshow(WINDOW_NAME2, g_resultImage);
}