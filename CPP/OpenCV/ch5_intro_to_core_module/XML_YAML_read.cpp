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
# include <iostream>

int main(){

    // Chnage the consle color.
    system("color 0D");

    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";

    // Initialization
    cv::FileStorage fs2(wd + "test.yaml", cv::FileStorage::READ);

    // Method I: 對FileNode操作
    int frameCount = (int)fs2["frameCount"];
    // 和 int frameCount; fs2["frameCount"] >> frameCount; 意思一樣

    std::string date;

    // Method II: 使用FileNode運算子
    fs2["calibrationDate"] >> date;

    // OpenCV資料結構的輸入和輸出
    // 從Mat中讀取資料
    cv::Mat cameraMatrix2, distCoeffs2;
    fs2["cameraMatrix"] >> cameraMatrix2;
    fs2["distCoeffs"] >> distCoeffs2;

    std::cout << "frameCount: " << frameCount << std::endl
    << "calibration date: " << date << std::endl
    << "camera matrix: " << cameraMatrix2 << std::endl
    << "distortion coeffs: " << distCoeffs2 << std::endl;

    // 讀取vector (array) 和 maps這些結構時會使用 FileNode 以及 FileNodeIterator 資料結構
    // 對於FileStorage類別的 "[", "]" 操作符號會返回FileNode資料類型
    // 對於一連串的FileNode，可以使用FileNodeIterator結構。
    cv::FileNode features = fs2["features"];
    cv::FileNodeIterator it = features.begin(), it_end = features.end();
    int idx = 0;
    std::vector<uchar> lbpval;

    // 使用FileNodeIterator瀏覽序列
    for(; it != it_end; ++it, idx++){
        std::cout << "feature #" << idx << ": ";
        std::cout << "x=" << (int)(*it)["x"] << ", y=" << (int) (*it) ["y"] << ",lbp: (";
        // 我們也可以使用filenode >> std::vector操作符號來輕易地讀取數值陣列
        (*it)["lbp"] >> lbpval;
        for( int i = 0; i < (int)lbpval.size(); i++){
            std::cout << " " << (int)lbpval[i];
        }
        std::cout << ")" << std::endl;
    }

    // 檔案關閉
    fs2.release();

    // 程式結束，輸出一些說明文字
    std::cout << "Press any key!" << std::endl;
    getchar();

    return 0;
}