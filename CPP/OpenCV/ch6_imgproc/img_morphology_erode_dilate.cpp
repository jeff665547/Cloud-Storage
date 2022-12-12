/* 形態學濾波(1): 腐蝕與膨脹 */
// 形態學(morphology)一詞通常表示生物學的一個分支
// 影像處理的形態學指的是數學形態學。
// 數學形態學(Mathematical morphology)是一門建立在
// 格論和拓樸學基礎之上的影像分析學科，
// 是數學形態學影像處理的基本理論。
// 其基本運算包含: 二值腐蝕和膨脹、二值開閉運算、骨架抽取、極限腐蝕
// 擊中擊不中變換、形態學梯度、Top-hat變換、顆粒分析、流域變換、灰值腐蝕和膨脹、
// 灰值開閉運算、灰值型態梯度等。
// 形態學操作就是基於形狀的一系列影像處理操作。
// 最基本的形態學操作有兩種：膨脹(dilate)與腐蝕(erode)。
// * 膨脹與腐蝕能實現各是各樣的功能
//   1. 消除雜訊
//   2. 分割(isolate)出獨立的影像元素，在影像中連接(join)相鄰的元素。
//   3. 尋找影像中的明顯的極大值區域或極小值區域。
//   4. 求出影像的梯度。
// * 腐蝕和膨脹是對影像中白色部分(高亮部分)而言的，不是黑色部分。
// 
// * 膨脹是將原圖中的高亮部分被腐蝕，類似於"領域被蠶食"，效果圖擁有比原圖更小的高亮區域。
// * 膨脹(dilate)就是求局部最大值的操作。從數學角度來說，膨脹膨脹或者腐蝕操作就是將影像
//   (或影像的一部份區域，稱之為A)與核(稱之為B)進行卷積。
// * 核可以是任何形狀和大小，他擁有一個單獨定義出來的參考點，我們稱其為錨點(anchorpoint)。
//   多數情況下，核心是一個小的，中間帶有參考點和實心正方形或者圓形。其實可以把核心視為模板或者遮罩。
// * 膨脹就是求局部最大值的操作。核B與圖形卷積，即計算核B覆蓋的區域的像素點的最大值，並把這個最大值
//   賦值給參考點指定的像素。這樣就會使影像中的高亮區域逐漸增長。
// * 膨脹的數學運算式如下：
//           dst(x, y) = max_((x',y'): element(x',y') != 0){src(x + x', y + y')}
// 
// * 膨脹和腐蝕是相反的一對操作，所以腐蝕就是求局部最小值的操作。
// * 腐蝕的數學運算式如下：
//           dst(x, y) = min_((x',y'): element(x',y') != 0){src(x + x', y + y')}

# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){

    // Load the raw image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    cv::Mat img = cv::imread(wd + "NFS01.jpg");

    // Initialize the window.
    cv::namedWindow("Original");
    cv::namedWindow("Dilate (Processed)");
    cv::namedWindow("Erode (Processed)");

    // Show the original image.
    cv::imshow("Original", img);
    
    // Get the customized kernel.
    cv::Mat element = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(15, 15));
    // 第一個參數代表核心的形狀，有如下三種可以選擇：
    // 矩形： MORPH_RECT
    // 交叉形： MORPH_CROSS
    // 橢圓形： MORPH_ELLIPSE
    // 第二個參數代表核心(kernel)的尺寸
    // 第三個參數代表錨點(anchor)的位置，預設值為cv::Point(-1, -1)，表示錨點位於中心。
    //      注意十字形的element形狀唯一依賴於錨點的位置，
    //      而在其他情況下，錨點只是影響了形態學運算結果的偏移。

    cv::Mat out1, out2;

    // Image Dilate.
    cv::dilate(img, out1, element);
    // 第一個參數代表輸入影像，待處理的圖片深度應為CV_8U、CV_16U、CV_16S、CV_32F以及CV_64F之一。
    // 第二個參數代表目標影像，需要和來源圖片(第一個參數)有一致的尺寸和類型。
    // 第三個參數代表 kernel 當為NULL時，表示的是使用參考點位於中心的3x3的核心。此參數通常會搭配getStructuringElement使用，
    //          getStructuringElement函數會返回指定形狀和尺寸的結構元素(核心矩陣)。
    // 第四個參數(未列出)代表 Point 類型的 Anchor，錨的位置，其有預設值(-1, -1)，表示錨位於中心。
    // 第五個參數(未列出)代表反覆運算使用erode()的次數，預設值為1。
    // 第六個參數(未列出)用於診斷影像外部像素的某種邊界模式。
    // 第七個參數(未列出)代表當邊界為常數時的邊界值，一般來說不用管它。

    // Image Erode.
    cv::erode(img, out2, element);

    // Show the effect.
    cv::imshow("Dilate (Processed)", out1);
    cv::imshow("Erode (Processed)", out2);
    cv::waitKey(0);

    return 0;
}