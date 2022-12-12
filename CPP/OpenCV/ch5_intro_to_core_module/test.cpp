# include "opencv2/imgproc/imgproc.hpp"
# include "opencv2/highgui/highgui.hpp"
# include <iostream>

int main(int argc, char *argv[]){

    std::string img1_path, img2_path, output_path;
    img1_path = argv[1];
    img2_path = argv[2];
    output_path = argv[3];

    cv::Mat img1, img2, imgsum;

    img1 = cv::imread(img1_path, cv::IMREAD_ANYCOLOR | cv::IMREAD_ANYDEPTH);
    img2 = cv::imread(img2_path, cv::IMREAD_ANYCOLOR | cv::IMREAD_ANYDEPTH);
    imgsum = img1 + img2;

    cv::imwrite(output_path, imgsum);

    return 0;
}
