# include <opencv2/opencv.hpp>
# include <vector>

// using namespace cv;
using namespace std;

std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch3_intro_to_GUI/";

void createAlphaMat(cv::Mat &mat){
    for (int i = 0; i < mat.rows; ++i){
        for (int  j = 0; j < mat.cols; ++j){
            cv::Vec4b&rgba = mat.at<cv::Vec4b>(i, j);
            rgba[0] = UCHAR_MAX;
            rgba[1] = cv::saturate_cast<uchar>((float (mat.cols - j)) / ((float)mat.cols) *UCHAR_MAX);
            rgba[2] = cv::saturate_cast<uchar>((float (mat.rows - i)) / ((float)mat.rows) *UCHAR_MAX);
            rgba[3] = cv::saturate_cast<uchar>(0.5 * (rgba[1] + rgba[2]));
        }
    }
}

int main(){
    // 建立帶Alpha色版的Mat
    cv::Mat mat(480, 640, CV_8UC4);
    createAlphaMat(mat);

    vector<int>compression_params;
    // OpenCV 2:
    // compression_params.push_back(CV_IMWRITE_PNG_COMPRESSION);
    // OpenCV 3:
    compression_params.push_back(cv::IMWRITE_PNG_COMPRESSION);
    compression_params.push_back(9);

    try{
        cv::imwrite(wd + "Transparent_Alpha_value.png", mat, compression_params);
        cv::imshow("Generated PNG", mat);
        fprintf(stdout, "PNG圖片檔的alpha資料儲存完畢~\n可以在專案目錄下查看由imwrite函數產生的圖片\n");
        cv::waitKey(0);
    }
    catch(runtime_error& ex){
        fprintf(stderr, "影像轉換PNG格式發生錯誤:%s\n", ex.what());
        return 1;
    }

    return 0;
}