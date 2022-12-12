# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>

int main(){
    // Load the image and show the file.
    cv::Mat srcImage;
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch9_imghist_matching/";
    srcImage = cv::imread(wd + "NFS01.jpg");
    cv::imshow("original", srcImage);

    // Parameter preparation
    int bins = 256;
    int hist_size[] = {bins};
    float range[] = {0, 256};
    const float* ranges[] = {range};
    cv::MatND redHist, greenHist, blueHist;

    // Histogram computation (red)
    int channels_r[] = {0};
    cv::calcHist(&srcImage, 1, channels_r, cv::Mat(), // 不使用遮罩
                redHist, 1, hist_size, ranges, true,  // the histogram is uniform.
                false);

    // Histogram computation (green)
    int channels_g[] = {1};
    cv::calcHist(&srcImage, 1, channels_g, cv::Mat(),  // 不使用遮罩
                greenHist, 1, hist_size, ranges, true, // the histogram is uniform. 
                false);

    // Histogram computation (blue)
    int channels_b[] = {2};
    cv::calcHist(&srcImage, 1, channels_b, cv::Mat(), // 不使用遮罩
                blueHist, 1, hist_size, ranges, true, // the histogram is uniform.
                false);
    

    /* 繪製出三色直條圖 */
    double maxValue_red, maxValue_green, maxValue_blue;
    cv::minMaxLoc(redHist, 0, &maxValue_red, 0, 0);
    cv::minMaxLoc(greenHist, 0, &maxValue_green, 0, 0);
    cv::minMaxLoc(blueHist, 0, &maxValue_blue, 0, 0);
    int scale = 1;
    int histHeight = 256;
    cv::Mat histImage = cv::Mat::zeros(histHeight, bins*3, CV_8UC3);

    // 正式繪製
    for(int i = 0; i < bins; i++){
        // parameter preparation
        float binValue_red = redHist.at<float>(i);
        float binValue_green = greenHist.at<float>(i);
        float binValue_blue = blueHist.at<float>(i);
        int intensity_red = cvRound(binValue_red*histHeight/maxValue_red);    // 要繪製的高度
        int intensity_green = cvRound(binValue_green*histHeight/maxValue_green);    // 要繪製的高度
        int intensity_blue = cvRound(binValue_blue*histHeight/maxValue_blue);   // 要繪製的高度
    

    // 繪製紅色分量的直條圖
    cv::rectangle(histImage, cv::Point(i*scale, histHeight - 1), 
        cv::Point((i+1)*scale - 1, histHeight - intensity_red), 
        cv::Scalar(255, 0, 0));

    // 繪製綠色分量的直條圖
    cv::rectangle(histImage, cv::Point((i+bins)*scale, histHeight - 1), 
        cv::Point((i+bins+1)*scale - 1, histHeight - intensity_green), 
        cv::Scalar(0, 255, 0));

    // 繪製藍色分量的直條圖
    cv::rectangle(histImage, cv::Point((i+bins*2)*scale, histHeight - 1), 
        cv::Point((i+bins*2+1)*scale - 1, histHeight - intensity_blue), 
        cv::Scalar(0, 0, 255));
    }

    // Show the histogram.
    cv::imshow("Image RGB's histogram.", histImage);
    cv::waitKey(0);
    
    return 0;
}