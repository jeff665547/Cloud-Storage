# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){
    // Load the raw image and show the image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch9_imghist_matching/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg", 0);

    if(!srcImage.data){
        std::cout << "Loaded failed!" << std::endl;
        return false;
    }

    // Define the variable
    cv::MatND dstHist;  // 在cv中用CvHistogram *hist = cvCreateHist
    int dims = 1;
    float hranges[] = {0, 255};
    const float *ranges[] = {hranges}; // 這裡需要為const類型
    int size = 256;
    int channels = 0;

    // Compute the image histogram
    cv::calcHist(&srcImage, 1, &channels, cv::Mat(), dstHist, dims, &size, ranges);
    int scale = 1;

    cv::Mat dstImage(size*scale, size, CV_8U, cv::Scalar(0));
    // Get the maximum and minmum.
    double minValue = 0;
    double maxValue = 0;
    cv::minMaxLoc(dstHist, &minValue, &maxValue, 0, 0);

    // Draw the histogram.
    int hpt = cv::saturate_cast<int>(0.9*size);
    for(int i = 0; i < 256; i++){
        float binValue = dstHist.at<float>(i);    // 注意hist中是float類型
        int realValue = cv::saturate_cast<int>(binValue * hpt/maxValue);
        cv::rectangle(dstImage, cv::Point(i*scale, size - 1), cv::Point((i+1)*scale - 1, size - realValue), cv::Scalar(255));
    }

    cv::imshow("histogram", dstImage);
    cv::waitKey(0);

    return 0;
}