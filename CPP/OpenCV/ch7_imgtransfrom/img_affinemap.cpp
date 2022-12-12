// 仿射變換與旋轉 (Linear Transformation and Rotation)
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>
# define WINDOW_NAME1 "Original"
# define WINDOW_NAME2 "Wrap Image"
# define WINDOW_NAME3 "Wrap and Rotate Image"

/* golbal function declaration */
static void ShowHelpText();

int main(){

    ShowHelpText();

    // [1] parameter preparation
    // 定義兩組點，代表兩個三角形
    cv::Point2f srcTriangle[3];
    cv::Point2f dstTriangle[3];

    // Define some cv::Mat
    cv::Mat rotMat(2, 3, CV_32FC1);
    cv::Mat warpMat(2, 3, CV_32FC1);
    cv::Mat srcImage, dstImage_warp, dstImage_warp_rotate;

    // [2] Load the srouce image and initialization
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch7_imgtransfrom/";
    srcImage = cv::imread(wd + "NFS01.jpg", 1);
    if(!srcImage.data){
        std::cout << "Load failed!" << std::endl;
        return false;
    }
    dstImage_warp = cv::Mat::zeros(srcImage.rows, srcImage.cols, srcImage.type());

    // [3] 設定來源影像和目標影像上的三組點以計算仿射變換
    srcTriangle[0] = cv::Point2f(0, 0);
    srcTriangle[1] = cv::Point2f(static_cast<float>(srcImage.cols - 1), 0);
    srcTriangle[2] = cv::Point2f(0, static_cast<float>(srcImage.rows - 1));

    dstTriangle[0] = cv::Point2f(static_cast<float>(srcImage.cols*0.0), static_cast<float>(srcImage.rows*0.33));
    dstTriangle[1] = cv::Point2f(static_cast<float>(srcImage.cols*0.65), static_cast<float>(srcImage.rows*0.35));
    dstTriangle[2] = cv::Point2f(static_cast<float>(srcImage.cols*0.15), static_cast<float>(srcImage.rows*0.6));

    // [4] 求得仿射變換
    warpMat = cv::getAffineTransform(srcTriangle, dstTriangle);

    // [5] 對來源影像應用剛剛求得的仿射變換
    cv::warpAffine(srcImage, dstImage_warp, warpMat, dstImage_warp.size());

    // [6] 對影像進行縮放後再旋轉
    cv::Point center = cv::Point(dstImage_warp.cols/2, dstImage_warp.rows/2);
    double angle = -30.0;
    double scale = 0.8;
    // 透過上面的旋轉細節資訊求得旋轉矩陣
    rotMat = cv::getRotationMatrix2D(center, angle, scale);

    // 旋轉已縮放後的影像
    cv::warpAffine(dstImage_warp, dstImage_warp_rotate, rotMat, dstImage_warp.size());

    // [7] 顯示結果
    cv::imshow(WINDOW_NAME1, srcImage);
    cv::imshow(WINDOW_NAME2, dstImage_warp);
    cv::imshow(WINDOW_NAME3, dstImage_warp_rotate);

    cv::waitKey(0);

    return 0;
}

static void ShowHelpText(){
    // 輸出一些說明資訊
    std::cout << "\t\t Welcome!" << std::endl;
    std::cout << "\t OpenCV version is " << CV_VERSION << std::endl;
}