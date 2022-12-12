/* XML和YAML檔的匯入和匯出 */
// XML和YAML是使用非常廣泛的檔案格式，
// 可以利用XML或者YAML格式的檔案儲存和還原各式各樣的資料結構。
// 它們也可以儲存和載入任意複雜的資料結構，
// 其中就包含了OpenCV相關周邊的資料結構，
// 以及各種原始資料類型，如整數和浮點數字和文字字串。
// 
// XML為可延伸標記式語言。
// 所謂"標記"，就代表開發者可以根據自身需要定義自己的標記，
// 比如<book>，<name>。任何滿足XML命名規則的名稱都可以標記
// 此外，XML是一種語意/結構化語言，它描述了文件的結構和語義。
// YAML是一個可讀性高，用來表達資料序列的格式。
// 
// 我們一般使用非常廣泛如下過程來寫入或者讀取資料到XML和YAML檔案中。
// 1. 產生實體一個FileStorage類別的物件，用預設帶參數的構造函數完成初始化，
//    或者使用FileStorage::open()成員函數輔助初始化。
// 2. 使用串流符號<<進行檔案寫入操作，或者>>進行檔案讀取操作，類似C++中的檔案輸入輸出串流。
// 3. 使用FileStorage::release()函數(它來自FileStorage類別物件)，同時關閉檔案。

# include "opencv2/opencv.hpp"
# include <time.h>

int main(){

    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";

    // Initialization
    cv::FileStorage fs(wd + "test.yaml", cv::FileStorage::WRITE);

    // 檔案寫入 "<<"
    // 文字和數字的輸入和輸出
    fs << "frameCount" << 5;
    time_t rawtime; time(&rawtime);
    fs << "calibrationDate" << asctime(localtime(&rawtime));
    
    // OpenCV資料結構的輸入和輸出
    // 從Mat中寫入資料
    cv::Mat cameraMatrix = (cv::Mat_<double>(3, 3) << 1000, 0, 320, 0, 1000, 240, 0, 0, 1);
    cv::Mat distCoeffs = (cv::Mat_<double>(5, 1) << 0.1, 0.01, -0.001, 0, 0);
    fs << "cameraMatrix" << cameraMatrix << "distCoeffs" << distCoeffs;

    // vectors (arrays) 和 maps 的輸入和輸出 (vector須加上"["(初始元素)以及"]"(末端元素), 
    // maps則須加上"{"(初始元素)以及"}"(末端元素))
    fs << "features" << "[";

    for( int i = 0; i < 3 ; i++ ){
        int x = rand() % 640;
        int y = rand() % 480;
        uchar lbp = rand() % 256;

        fs << "{:" << "x" << x << "y" << y << "lbp" << "[:";
        for(int j = 0; j < 8; j++){
            fs << ((lbp >> j) & 1);
        }
        fs << "]" << "}";
    }

    fs << "]";

    // 檔案關閉
    fs.release();

    std::cout << "Read files over, please view the files under the directory.";
    getchar();

    return 0;
}