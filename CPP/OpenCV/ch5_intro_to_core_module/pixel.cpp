/* 影像在記憶體中的儲存方式 */
// 矩陣的大小取決於所用的色彩模型(所用的通道數)，如果是灰階影像，矩陣就會如下方所示：
//           col 0,   col 1,   col 2,   col 3, ...,  col m,   
// row 0      0,0      0,1      0,2      0,3          0,m
// row 1      1,0      1,1      1,2      1,3          1,m
// row 2      2,0      2,1      2,2      2,3          2,m
// ...      ...,0    ...,1    ...,2    ...,3        ...,m
// row n      n,0      n,1      n,2      n,3          n,m
// 
// 而對多通道影像來說，矩陣中的列會包含多個子列，其子列個數與通道數相等。(如RGB色彩模型)
//                 col 0,               col 1,                col 2,                col 3,       ...,           col m,   
// row 0      0,0   0,0   0,0      0,1   0,1   0,1      0,2   0,2   0,2      0,3   0,3   0,3           0,m   0,m   0,m
// row 1      1,0   1,0   1,0      1,1   1,1   1,1      1,2   1,2   1,2      1,3   1,3   1,3           1,m   1,m   1,m
// row 2      2,0   2,0   2,0      2,1   2,1   2,1      2,2   2,2   2,2      2,3   2,3   2,3           2,m   2,m   2,m
// ...      ...,0 ...,0 ...,0    ...,1 ...,1 ...,1    ...,2 ...,2 ...,2    ...,3 ...,3 ...,3         ...,m ...,m ...,m
// row n      n,0   n,0   n,0      n,1   n,1   n,1      n,2   n,2   n,2      n,3   n,3   n,3           n,m   n,m   n,m
//             (B)   (G)   (R)      (B)   (G)   (R)      (B)   (G)   (R)      (B)   (G)   (R)           (B)   (G)   (R)
// 很多情況下，因為記憶體足夠大，可以實現連續儲存，因此，影像中的各行就能一行一行的連接起來，形成一個長行。
// 連續儲存有助於提升影像掃描速度，我們可以使用isContinuous()來判斷矩陣是否連續儲存的。
// 
// 
# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <iostream>

/* 存取影像中像素的三類方法 (方法一  用指標存取像素) */
// 此方法速度最快
void colorReduce(cv::Mat& inputImage, cv::Mat& outputImage, int div){
    // parameter preparation
    outputImage = inputImage.clone();  // 複製實體參數到臨時變數
    int rowNumber = outputImage.rows;  // 行數
    int colNumber = outputImage.cols*outputImage.channels();  // 列數 x 色版數 = 每一行元素的個數
    // 成員函數channels()用於返回影像的色板(通道)數。灰階圖的色板通道數為1，彩色圖的色板通道數為3。

    // 雙重迴圈，瀏覽過所有的像素值
    for (int i = 0; i < rowNumber; i++){  // 行迴圈
        unsigned char* data = outputImage.ptr<uchar>(i);  // 取得第i行的首地址 (Mat類別提供的ptr模板函數可以得到影像任一行的第一個位址)
        for (int j = 0; j < colNumber; j++){  // 列迴圈
            data[j] = data[j]/div*div + div/2;  // 處理每個像素 data/div*div <=> (I_new = (I_old/div)*div) 先整除在乘再平移(一起增加亮度)
        }  // 行處理結束
    }
    std::cout << 50/3*3 << std::endl; // example 等於48。
}

/* 存取影像中像素的三類方法 (方法二  用反覆運算器操作像素，此法與STL (Standard Template Library，標準模板庫)的用法相似) */
// 此方法是非常安全的方法 (STL反覆運算器)
// Vec3b在OpenCV中代表由3個unsigned char 組成的向量。(對於一個包含彩色影像(RGB)的Mat，會返回一個由3個位元陣列組成的向量。)
void colorReduce2(cv::Mat& inputImage, cv::Mat& outputImage, int div){
    // parameter preparation
    outputImage = inputImage.clone();  // 複製實體參數到臨時變數
    // 取得反覆運算器
    cv::Mat_<cv::Vec3b>::iterator it = outputImage.begin<cv::Vec3b>(); // 初始位置的反覆運算器
    cv::Mat_<cv::Vec3b>::iterator itend = outputImage.end<cv::Vec3b>(); // 終止位置的反覆運算器

    // 存取彩色影像像素
    for (;it != itend; ++it){
        // ---------------------開始處理每個像素------------------------------
        (*it)[0] = (*it)[0]/div*div + div/2;
        (*it)[1] = (*it)[1]/div*div + div/2;
        (*it)[2] = (*it)[2]/div*div + div/2;
        //  -----------------------處理結束----------------------------------
    }
    std::cout << 50/3*3 << std::endl; // example 等於48。
}

/* 存取影像中像素的三類方法 (方法三  動態位址計算) */
// Vec3b在OpenCV中代表由3個unsigned char 組成的向量。(對於一個包含彩色影像(RGB)的Mat，會返回一個由3個位元陣列組成的向量。)
void colorReduce3(cv::Mat& inputImage, cv::Mat& outputImage, int div){
    // parameter preparation
    outputImage = inputImage.clone();   // 複製實體參數到臨時變數
    int rowNumber = outputImage.rows;   // 行數
    int colNumber = outputImage.cols;   // 列數

    // 存取彩色影像像素
    for (int i = 0; i < rowNumber; i++){
        for (int j = 0; j < colNumber; j++){
            // ------------------開始處裡每個像素------------------------------
            outputImage.at<cv::Vec3b>(i, j)[0] = outputImage.at<cv::Vec3b>(i, j)[0] / div*div + div/2; // 藍色通道
            outputImage.at<cv::Vec3b>(i, j)[1] = outputImage.at<cv::Vec3b>(i, j)[1] / div*div + div/2; // 綠色通道
            outputImage.at<cv::Vec3b>(i, j)[2] = outputImage.at<cv::Vec3b>(i, j)[2] / div*div + div/2; // 紅色通道
            //  ---------------------處理結束----------------------------------
            // 成員函數at(int y, int, x) 可以用來存取影像元素，但需要再編譯期知道影像的資料類型。
            // 需要注意的是，我們一定要確保指定的資料類型要和矩陣中的資料類型相符合，
            // 因為at方法本身不會對任何資料類型進行轉換。
        }   // 行處理結束
    }

}



int main(){
    /* 顏色空間縮減 */
    // 用越多的顏色來進行處理，會對演算法性能造成嚴重影響(如RGB色彩模型)。其實，僅用這些顏色中具有代表性的很小的一部分，就足以達到同樣的效果。
    // 顏色空間縮減(color space reduction)，在很多應用中可以大大降低運算複雜度。
    // 顏色空間縮減的作法是：將現有顏色空間值除以某個輸入值，以獲得較少的顏色數。
    // 如：原有顏色值0~9可取新值為0，10~19可取新值為10，以此類推。 (I_new = (I_old/10)*10)
    // 在處理影像像素時，每個像素都需要進行一遍上述計算，也需要一定的時間花費。
    // 但我們注意到其實只有0~255種像素，即只有256種情況。我們可以進一步地把256種計算好的結果提前存在table中，這樣每種情況不需計算，
    // 直接從table中取結果即可。此種策略對於較大的影像是非常有效的，查閱的資料表可以是一維或多維的陣列，儲存了不同輸入值所對應的輸出值。
    // 因此簡單的顏色空間縮減演算法就可由下面兩部組成:
    // 1. 瀏覽影像矩陣的每一個像素。
    // 2. 對像素運用 p[j] = table[p[j]]; 這個公式。
    // 注意: 除法和乘法這兩種運算特別費時，因此盡可能運用代價較低的加、減、賦值(運用在查表)等運算來替換他們。

    int divideWith = 10;
    unsigned char table[256];
    for (int i = 0; i < 256; ++i)
        table[i] = divideWith* (i/divideWith);
        // table[i]存放的值為原像素值為i減少顏色空間的結果。

    // p[j] = table[p[j]];


    /* LUT函數: Look up table 操作 */
    // 他用於批次進行影像元素查詢、掃描與操作影像
    // 首先，我們建立一個mat型用於查表
    cv::Mat lookUpTable(1, 256, CV_8U);
    unsigned char* p = lookUpTable.data;
    for (int i = 0; i < 256; ++i){
        p[i] = table[i];
    }

    // 然後我們使用函數(I是輸入J是輸出):
    // for (int i = 0; i < times; ++i){
    //      cv::LUT(I, lookUpTable, J);
    // }

    /* 計時函數 */
    // getTickCount() return CPU 自某事件(如啟動電腦)以來走過的單位時間。
    // getTickFrequency() return CPU 一秒鐘所走過的單位時間。
    double time0 = static_cast<double>(cv::getTickCount()); // 紀錄起始時間
    // 進行影像處理操作......
    time0 = ((double)cv::getTickCount() - time0) / cvGetTickFrequency();
    std::cout << "Cost time: " << time0 << "sec" << std::endl; // 輸出執行時間

    /* 存取影像中像素的三類方法 */
    // 1. 指標訪問: C操作符號[];
    // 2. 反覆運算器iterator;
    // 3. 動態位址計算
    // 這三種方法在速度上略有差異 (尤其在debug模式下更為明顯) 方法一最快
    // 以下程式說明 (程式目的: 減少影像中顏色的數量)
    // 1. 建立原始圖並顯示
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg");
    cv::imshow("Original image", srcImage);

    // 2. 按原始圖的參數規格來建立效果圖
    cv::Mat dstImage;
    dstImage.create(srcImage.rows, srcImage.cols, srcImage.type());
    // 效果圖的大小、類型原圖片相同

    // 3. 紀錄起始時間
    double times = static_cast<double>(cv::getTickCount());

    // 4. 使用顏色空間縮減函數 (自定義函數，用途為減少顏色)
    colorReduce(srcImage, dstImage, 32);

    // 5. 計算執行時間並輸出
    times = ((double)cv::getTickCount() - times) / cv::getTickFrequency();
    std::cout << "Cost time: " << times << "secs" << std::endl;

    // 6. 顯示效果圖
    cv::imshow("Processed image", dstImage);
    cv::waitKey(0);

    return 0;
}
