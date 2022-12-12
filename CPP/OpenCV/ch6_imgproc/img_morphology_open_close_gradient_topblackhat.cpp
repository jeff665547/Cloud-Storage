/* 形態學濾波(2): 開運算、閉運算、形態學梯度、頂帽、黑帽 */
// 運用腐蝕和膨脹這兩種最基本的形態學操作，可以實現更進階的形態學轉換。
// morphologyEx()利用基本的腐蝕和膨脹技術，來執行更加進階形態學轉換。
// * 膨脹(Dilate): 影像中的白色區域膨脹，求局部極大運算子。
// * 腐蝕(Erode): 影像中的白色區域被腐蝕，求局部極小運算子。
// * 開運算(Opening Operatioin)： 先腐蝕後膨脹的過程
// * 閉運算(Closing Operatioin)： 先膨脹後腐蝕的過程
// * 形態學梯度(Morphological Gradient)： 膨脹圖與腐蝕圖的差距
// * 頂(禮)帽(Top Hat): 原影像與開運算的結果圖之差距
// * 黑帽(Black Hat): 閉運算的結果與原影像之差距
// 運算式: 
// * 開運算: dst = open(src, element) = cv::dilate(cv::erode(src, element))
// * 閉運算: dst = close(srd, element) = cv::erode(cv::dilate(src, element))
// * 形態學梯度：dst = morph-grad(src, element) = cv::dilate(src, element) - cv::erode(src, element)
// * 頂帽: dst = tophat(src, element) = src - cv::open(src, element)
// * 黑帽: dst = blackhat(src, element) = cv::close(src, element) - src
// 特性:
// * 開運算: 1. 用來消除小物體  2. 在纖細點處分離物體，並且在平滑較大物體的邊界的同時不明顯改變其面積。 3. 放大裂縫或局部低亮度的區域。
// * 閉運算: 1. 能排除小型黑洞(黑色區域)
// * 形態學梯度: 1. 對二值影像進行這一操作可以將團塊(bolb)的邊緣突顯出來。 2. 可以用來保留物體的邊緣輪廓。
// * 頂帽: 1. 凸顯比原圖輪廓周圍附近的區域更明亮的區域。 2. 在原圖上的一群黑點中凸顯isolated噪點(白(亮)點) 3. 獲取輪廓外部的噪點(更亮(白)點)運算。
//         4. 在一幅影像具有大幅的背景，而微小物品比較有規律的情況下，可以用來進行背景提取。
// * 黑帽: 1. 凸顯比原圖輪廓周圍附近的區域更暗的區域。 2. 在原圖上的一群白點中凸顯isolated噪點(黑(暗)點) 3. 獲取輪廓外部的噪點(更暗(黑)點)運算。
//         4. 分離比鄰近點暗一些的斑塊，效果有著非常完美的輪廓。
// 
// morphologyEx()其實就是內部的一個大switch而已，根據不同的識別字取不同的操作。

# include <opencv2/opencv.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>

int main(){

    // Load the original image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    cv::Mat image = cv::imread(wd + "subaru.png");

    // Initialized the window.
    cv::namedWindow("Original");
    cv::namedWindow("Processed");

    // Show the original image.
    cv::imshow("Original", image);

    // Define the kernel
    cv::Mat element = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(15, 15));
    // 第一個參數代表核心的形狀，有如下三種可以選擇：
    // 矩形： MORPH_RECT
    // 交叉形： MORPH_CROSS
    // 橢圓形： MORPH_ELLIPSE
    // 第二個參數代表核心(kernel)的尺寸
    // 第三個參數代表錨點(anchor)的位置，預設值為cv::Point(-1, -1)，表示錨點位於中心。
    //      注意十字形的element形狀唯一依賴於錨點的位置，
    //      而在其他情況下，錨點只是影響了形態學運算結果的偏移。


    // 進行形態學操作
    cv::morphologyEx(image, image, cv::MORPH_GRADIENT, element);
    // param 1: 輸入影像，待處理的圖片深度應為CV_8U、CV_16U、CV_16S、CV_32F以及CV_64F之一。
    // param 2: 目標影像，需要和來源圖片(第一個參數)有一致的尺寸和類型。
    // param 3: 表示形態學運算的flag，int類型。
    //          cv::MORPH_OPEN       開運算
    //          cv::MORPH_CLOSE      閉運算
    //          cv::MORPH_GRADIENT   形態學梯度
    //          cv::MORPH_TOPHAT     頂帽
    //          cv::MORPH_BLACKHAT   黑帽
    //          cv::MORPH_ERODE      腐蝕
    //          cv::MORPH_DILATE     膨脹
    // param 4: 代表 kernel 當為NULL時，表示的是使用參考點位於中心的3x3的核心。此參數通常會搭配getStructuringElement使用，
    //          getStructuringElement函數會返回指定形狀和尺寸的結構元素(核心矩陣)。
    // param 5: 未列出，代表 Point 類型的 Anchor，錨的位置，其有預設值(-1, -1)，表示錨位於中心。
    // param 6: 未列出，代表反覆運算使用函數的次數，預設值為1。
    // param 7: 未列出，用於推斷影像外部像素的某種邊界模式。
    // param 8: 未列出，代表當邊界為常數時的邊界值，一般來說不用管它。

    // Show the Processed image.
    cv::imshow("Processed", image);

    cv::waitKey(0);

    return 0;
}