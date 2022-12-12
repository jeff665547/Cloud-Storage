// CH3 HighGUI圖形化使用者介面入門
// HighGUI模組為高層GUI圖形化使用者介面模組，
// 包含媒體的輸入輸出、視訊捕捉、影像和視訊的編碼解碼、
// 圖形互動介面的接口等內容。
// 此章節介紹一些OpenCV中最常用的一些互動操作，
// 包括影像的載入、顯示和輸出，為程式新增滑動軸，
// 以及滑鼠操作。
# include <iostream>
# include "opencv2/opencv.hpp"
# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>

int main(int argc, char* argv[]){
    // Mat 類別是用於儲存影像以及其他矩陣資料的資料結構，
    // 預設情況下其尺寸為0。
    // 我們也可以指定其初始尺寸，如定義一個Mat類別物件
    cv::Mat pic(320, 640, CV_8UC2);
    // cv::Mat 對應到OpenCV 1.0時代的IplImage，主要用來存放影像的資料結構。

    // imread() function
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch3/";
    cv::Mat srcImage = cv::imread(wd + "needforspeedpaybackmustang.jpg");
    // cv::imread() 用於將圖片讀入cv::Mat類型中。
    
    // 若查看OpenCV官方文件的原型可以看到以下結果:
    // cv::Mat imread(const string& filename, int flag = 1);
    // 第二個參數int flag為int類型的flag，為載入標識，他指定一個載入影像的顏色類型。
    // 自帶預設值為1，代表載入三色板的彩色影像。
    // 這個參數可以在OpenCV中標識影像格式的舉立體中取值。
    // 透過轉到定義，我們可以在higui_c.h中發現這個舉例的定義是這樣的:
    /*
    enum
    {
        // enum 代表 enumerate，為舉例體的意思
        
        // 8 bit, color or not
        CV_LOAD_IMAGE_UNCHANGED = -1,
        // 此標識在新版本中已被廢棄，可忽略。

        // 8 bit, gray
        CV_LOAD_IMAGE_GRAYSCALE = 0, (0000)
        // 等價取值為0，如果取這個標識，始終將影像轉換為灰階再返回(return)。

        // ?, color
        CV_LOAD_IMAGE_COLOR = 1, (0001)
        // 等價取值為1，如果取這個標識，總是轉換影像到彩色再返回(return)。

        // any depth, ?
        CV_LOAD_IMAGE_ANYDEPTH = 2, (0010)
        // 等價取值為2，如果取這個標識，且載入的影像的深度為16位元或者32位元，
        // 就返回(return)對應深度的影像。否則就轉換為8位元影像再返回。

        // ?, any color
        CV_LOAD_IMAGE_ANYCOLOR = 4, (0100)

        // 如果輸入有衝突的標誌，將採用較小的數字值。
        // e.g. CV_LOAD_IMAGE_COLOR | CV_LOAD_IMAGE_ANYCOLOR 將載入三色版圖。
        
        // 如果想要載入最真實無損的來源影像，
        // 可以選擇 CV_LOAD_IMAGE_ANYDEPTH | CV_LOAD_IMAGE_ANYCOLOR

        flags是int型的變數，若我們不在這個舉立體中取固定的值，可以這樣進行：
        flags > 0  return一個三色版的彩色影像。
        flags = 0  return一個灰階影像。
        flags < 0  return一個包含alpha色板的載入影像。

        輸出影像預設情況下不返回alpha色板。如果想要alpha色板就需要取負值。
        如: 將flags取1999和取1的效果一樣，同樣表示return一個三色版的彩色影像。
        將flags取-1,return一個包含alpha色板的彩色影像。
        另外，需要額外注意，若以彩色模式載入影像，解碼後的影像會以BGR的色版順序進行儲存，
        及藍、綠、紅的順序，而不是平常的RGB的順序。

    };    
    */

    // 載入無損的來源影像
    cv::Mat srcrawImage = cv::imread(wd + "needforspeedpaybackmustang.jpg", 2 | 4); 

    // 載入灰階圖
    cv::Mat srcgrayImage = cv::imread(wd + "needforspeedpaybackmustang.jpg", 0);

    // 載入三色版的彩色影像
    cv::Mat srccolorImage = cv::imread(wd + "needforspeedpaybackmustang.jpg", 199);

    // 載入包含alpha色板的彩色影像
    cv::Mat srcalphaImage = cv::imread(wd + "needforspeedpaybackmustang.jpg", -1);

    // Bitwise operation 
    int flag = CV_LOAD_IMAGE_COLOR | CV_LOAD_IMAGE_ANYCOLOR;
    std::cout << flag << std::endl;

    // namedWindow() function
    cv::namedWindow("Testing window", cv::WINDOW_AUTOSIZE);
    // cv::namedWindow() 用於建立一個視窗。若是簡單地進行圖片顯示，可以略去namedWindow函數的使用，
    // 但若需要在顯示視窗之前就用到視窗名時，比如滑動軸的使用，要指定滑動軸依附到某個視窗上，就需要
    // namedWindow() 函數先建立出視窗，顯示規定視窗名稱了。
    // void namedWindow(const string& winname, int flags = WINDOW_AUTOSIZE);
    // param 1: const string& 類型的winname，填需要顯示的視窗標示名稱。
    // param 2: int 類型的flags，視窗的標識，可以有以下幾種值：
    //  1. WINDOW_NORMAL (or CV_WINDOW_NORMAL)，設定這個值，使用者可以改變視窗的大小(沒有限制)
    //  2. WINDOW_AUTOSIZE (or CV_WINDOW_AUTOSIZE)，設定這個值，視窗大小會自動調整以適應所顯示的影像，
    //  並且使用者不能手動更改視窗大小，為 namedWindow 函數的預設值。
    //  3. WINDOW_OPENGL (or CV_WINDOW_OPENGL)，設定這個值，視窗建立的時候會支援OpenGL。
    // 
    // namedWindow函數的作用是透過指定的名字，建立一個可以作為影像和進度條的容器視窗。
    // 如果具有相同名稱的視窗已經存在，則函數不做任何事情。
    // 
    // 可以使用destroyWindow()或者destroyAllWindow()函數來關閉視窗，
    // 並取消之前分配的與視窗相關的所有記憶體空間。
    // 但在現實生活中，對於程式碼不大的簡單程式來說，我們完全沒有必要手動使用上述的
    // destroyWindow()或者destroyAllWindow()函數，因為在退出時，
    // 所有的資源和應用程式的視窗會被作業系統自動關閉。

    // imshow() function
    cv::imshow("Testing window", srcrawImage);
    // cv::imshow() 用於在指定的視窗中顯示一幅影像。
    // void imshow(const string& winname, InputArray mat);
    // param 1: const string& 類型的winname，填需要顯示的視窗標示名稱。
    // param 2: InputArray 類型的mat，填需要顯示的影像。
    //          由於InputArray略顯冗長，因此在此若遇到原型中的InputArray以及OutputArray類型，
    //          可以把它簡單地當作Mat類別即可。
    cv::waitKey(0);


    // imwrite() function
    std::vector<int>quality_params;
    quality_params.push_back(10);
    quality_params.push_back(cv::IMWRITE_JPEG_QUALITY);
    cv::imwrite(wd + "needforspeedpaybackmustangout.jpg", srcrawImage, quality_params);
    // 輸出影像到檔案: imwrite()函數
    // bool imwrite(const string& filename, InputArray img, const vector<int>& params=vector<int>() );
    // param 1: const string&類型的filename，填寫需要寫入的檔案名。注意要帶上附檔名。
    // param 2: InputArray類型的img，一般填一個Mat類型的影像資料。
    // param 3: const vector<int>& 類型的params，表示為特定格式儲存的參數編碼。它有預設值vector<int>&類型的params，
    // 它有預設值vector<int>()，所以一般情況下不需要填寫。若有需要填寫的話，須了解以下參數的意義。
    // 1. 對於JPEG格式的圖片，這個參數表示從0到100的圖片品質(CV_IMWRITE_JPEG_QUALITY)，預設值是95。
    // 2. 對於PNG格式的圖片，這個參數表示壓縮層級(CV_IMWRITE_PNG_COMPRESSION)，從0到9。較高的值意味著更小的尺寸和
    //    更長的壓縮時間，預設值是3。
    // 3. 對於PPM，PGM，或PBM格式的圖片，這個參數表示一個二進位格式標誌(CV_IMWRITE_PXM_BINARY)，取值為0 or 1，預設值是1。
    //    imwrite函數用於將影像儲存到指定的檔案。

    
    return 0;
}
