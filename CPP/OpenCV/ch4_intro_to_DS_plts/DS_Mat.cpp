// OpenCV的資料結構 Mat
// 自從OpenCV踏入2.0時代，資料結構使用Mat類別後，有幾點需要注意：
// 1. 不必再手動為其開闢空間。(但仍然還是存在的，
//                           大多數OpenCV函數仍會手動地位輸出資料開闢空間。)
// 2. 不必再不需要時立即將空間釋放。
// 在最初幾個OpenCV版本中，一般使用名為IplImage的C語言結構體在記憶體中儲存影像。(基於C語言介面而建的影像儲存格式)
// 如果在退出前忘記release掉的話，就會造成記憶體洩漏，而且用起來有些不便。
// 因此，當開發目標不是僅能使用C語言作為開發語言的時候，便沒有必要使用舊有的C語言介面了。
// 
// Mat是一個類別，由兩個資料部分組成:矩陣標頭(包含矩陣尺寸、儲存方法、儲存位址等資訊)
// 和一個指向儲存所有像素值得矩陣的指標(根據所選儲存方法的不同，矩陣可以是不同的維度)
// 矩陣標頭的尺寸是常數值，但矩陣本身的尺寸會依影像的不同而不同，通常比矩陣頭的尺寸大數個數量級。
// 因此，當在程式中傳遞影像並建立副本時，大的開銷是由矩陣造成的，而不是資訊標頭。
// OpenCV是一個影像處理庫，囊括了大量的影像處理函數，為了解決問題通常要使用函式庫中的多個函數，
// 因此，在函數中傳遞影像是常有的事。總之，除非萬不得已，不應該進行大影像的複製，因為這會降低程式的執行速度。
// OpenCV使用了引數計數機制。其思路是讓每個Mat物件有自己的資訊標頭，但共用一個矩陣。
// 這透過讓矩陣指標指向同一位址而實現。而拷貝構造函數則只複製資訊標頭和矩陣指標，而不複製矩陣。
// 

# include <opencv2/opencv.hpp>
# include <iostream>
# include <opencv2/core.hpp>
#include <opencv2/core/mat.hpp>

int main(){

    std::string wd =  "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch4_intro_to_DS_plts/";
    cv::Mat A, W; // 僅建立資訊標頭部分
    A = cv::imread(wd + "NFS01.jpg");  // 這裡為矩陣開闢記憶體
    cv::Mat B(A); // 使用拷貝構造函數
    W = A; // 設定運算子

    // 以上程式碼中的所有Mat物件最終都指向同一個也是唯一一個資料矩陣。
    // 雖然它們的資訊標頭不同，但透過任何一個物件所做的改變也會影響其他物件。
    // 實際上，不同的物件只是存取相同資料的不同途徑而已。
    // 如果矩陣屬於多個Mat物件，那麼當不再需要它時，最後一個使用它的物件會負責清理該矩陣。
    // 透過引用計數機制，我們無論甚麼時候複製一個Mat物件的資訊標頭，都會增加矩陣的引用次數。
    // 當一個標頭被釋放之後，這個計數被減一;當計數值為零，矩陣會被清理。但某些時候你仍會想複製
    // 矩陣本身(不只是資訊標頭和矩陣指標)，這時候可以使用函數clone()或者copyTo()。
    
    // 矩陣複製
    // 方法一
    cv::Mat F = A.clone();
    // 方法二
    cv::Mat G;
    A.copyTo(G);

    // ROI (Region of Interest)
    // 建立只引用部分資料的資訊標頭。比如，想要建立一個感興趣區域(ROI)，只需要
    // 建立包含邊界資訊的資訊標頭:
    cv::Mat D (A, cv::Rect(10, 10, 100, 100)); // 使用矩形界定
    cv::Mat E = A(cv::Range::all(), cv::Range(1, 3)); // 用行和列來界定

    // 總結:
    // 1. OpenCV函數中輸出影像的記憶體分配是自動完成的(如果不特別指定的話)。
    // 2. 使用OpenCV的C++介面時不需要考慮記憶體釋放問題。
    // 3. 設定運算子(=)和拷貝構造函數(B(A))只複製資訊標頭。
    // 4. 使用clone()或者copyTo()來複製一幅影像的矩陣。


    /* 建立Mat物件的七種方法 */
    // 1. 使用Mat()構造函數
    cv::Mat M(2, 2, CV_8UC3, cv::Scalar(0, 0, 255)); 
    // params: 行數、列數、儲存元素的資料類型、每個點的色板(通道)數。
    // 資料類型 CV_[位元數][類型首碼]C[色板數]
    // 位元數: 8bite\16bite\32bite\64bite
    // 類型首碼: S\U\F; 
    //   S: signed int，有符號整型
    //   U: unsigned int，無符號整型
    //   F: float，單精度浮點型
    // 色板(通道)數: 1, 3, ...
    //   1: grayImg灰度圖像，是單通道圖像
    //   3: RGB彩色圖像，是3通道圖像
    //   4: 帶Alpha通道的RGB彩色圖像，是4通道圖像
    //   若需更多色板數，可以使用大寫的巨集並把色版數放在小括弧中。
    // Scalar是個short型別的向量，能使用指定的定制化值來初始化矩陣，它還可以用於表示顏色。

    std::cout << "M = " << std::endl << " " << M << std::endl << std::endl;


    // 2. 在C\C++中透過構造函數進行初始化
    // 建立一個超過2維的矩陣
    int sz[3] = {2, 2, 2};
    cv::Mat L(3, sz, CV_8UC1, cv::Scalar::all(0));
    // params: 維度數、指向陣列的指標、儲存元素的資料類型、每個點的色板(通道)數。
    //         這個陣列包含每個維度的尺寸。

    // 3. 為已存在的IplImage指標建立資訊標頭
    // 為已存在的IplImage指標建立資訊標頭。
    IplImage* img = cvLoadImage("C:/Users/jeff/Desktop/ProjectTemplate/src/Exam\
    ple/app/OpenCV/ch4_intro_to_DS_plts/NFS01.jpg");
    cv::Mat mtx = cv::cvarrToMat(img); // 轉換 IplImage* -> Mat

    // 4. 利用Create() 函數
    // 利用Mat類別中的Create()成員函數進行Mat類別的資料結構轉換。
    // 此方法不能為矩陣設定初值，只是在改變尺寸時重新為矩陣資料開闢記憶體而已。
    // M矩陣原本的內容在經過這道手續以後會被清除
    M.create(4, 4, CV_8UC(2));
    std::cout << "M = " << std::endl << std::endl;

    // 5. 採用Matlab式的初始化方式
    // 此方法採用Matlab形式的初始化方式: zeros()、ones()、eyes()。
    // Identity matrix
    cv::Mat Eye = cv::Mat::eye(4, 4, CV_64F);
    std::cout << "Eye = " << std::endl << " " << Eye << std::endl << std::endl;
    // Zero matrix (all entries are 0)
    cv::Mat O = cv::Mat::ones(2, 2, CV_32F);
    std::cout << "O = " << std::endl << " " << O << std::endl << std::endl;
    // One matrix (all entries are 1)
    cv::Mat Z = cv::Mat::ones(3, 3, CV_8UC1);
    std::cout << "Z = " << std::endl << " " << Z << std::endl << std::endl;


    // 6. 對小矩陣使用逗號分隔式初始化函數
    // 此方法為對小矩陣使用逗號分隔式初始化函數
    cv::Mat C = (cv::Mat_<double>(3, 3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);
    std::cout << "C = " << std::endl << " " << C << std::endl << std::endl;
    // [0, -1, 0;
    //  -1, 5, -1;
    //  0, -1, 0]


    // 7. 為已存在的物件建立新資訊標頭
    // 此方法為使用成員函數clone()或者copyTo()為一個已存在的Mat物件建立一個新的資訊標頭。
    cv::Mat RowClone = C.row(1).clone();
    std::cout << "RowClone = " << std::endl << " " << RowClone << std::endl << std::endl;
    // RowClone = [-1, 5, -1]





    /* OpenCV中的格式化輸出方法 */
    // OpenCV 有提供風格各異的格式化輸出方法。
    // 定義r矩陣(用randu()函數產生的隨機值來填充矩陣，需要給定一個上下界來確保
    // 隨機值在期望的範圍內)
    cv::Mat r = cv::Mat(10, 3, CV_8UC3);
    cv::randu(r, cv::Scalar::all(0), cv::Scalar::all(255));

    std::cout << r << std::endl;

    // Format 1: OpenCV預設風格
    std::cout << "r (OpenCV default) = " << std::endl << r << ";" << std::endl << std::endl;

    // Format 2-1: Python預設風格(OpenCV2)
    // std::cout << "r (Python 風格) = " << cv::format(r, "python") << ";" << std::endl << std::endl;

    // Format 2-2: Python預設風格(OpenCV3)
    std::cout << "r (Python format) = " << std::endl << cv::format(r, cv::Formatter::FMT_PYTHON) << ";" << std::endl << std::endl;

    // Format 3-1: 逗號分隔風格(Comma separated values, CSV)(OpenCV2)
    // std::cout << "r (逗號分隔風格) = " << cv::format(r, "csv") << ";" << std::endl << std::endl;

    // Format 3-2: 逗號分隔風格(Comma separated values, CSV)(OpenCV3)
    std::cout << "r (csv format) = " << std::endl << cv::format(r, cv::Formatter::FMT_CSV) << ";" << std::endl << std::endl;

    // Format 4-1: Numpy風格(OpenCV2)
    // std::cout << "r (Numpy風格) = " << cv::format(r, "numpy") << ";" << std::endl << std::endl;

    // Format 4-2: Numpy風格(OpenCV3)
    std::cout << "r (Numpy format) = " << std::endl << cv::format(r, cv::Formatter::FMT_NUMPY) << ";" << std::endl << std::endl;

    // Format 5-1: C語言風格(OpenCV2)
    // std::cout << "r (C語言風格) = " << cv::format(r, "C") << ";" << std::endl << std::endl;

    // Format 5-2: C語言風格(OpenCV3)
    std::cout << "r (C format) = " << std::endl << cv::format(r, cv::Formatter::FMT_C) << ";" << std::endl << std::endl;

    return 0;
}