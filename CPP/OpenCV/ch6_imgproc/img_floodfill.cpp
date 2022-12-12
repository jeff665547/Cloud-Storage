/* 漫水填充 floodfill */
// 
// 在影像中選擇一個種子點，然後把鄰近區域所有相似點填充上相同的顏色。ㄕ
// 
// 運算：
// 漫水填充法是一種用特定的顏色填充連通區域，透過設定可連通像素的上下限，
// 以及以連通方式來達到不同的填充效果方法。簡單來說就是自動選取了和種子點相連的區域，
// 接著將該區域替換成指定的顏色。類似PhotoShop的魔術棒選擇工具。
// 
// 用途:
// 1. 用來標記或分離影像的一部份，以便對其進行進一步處理或分析。
// 2. 用來從輸入影像取得遮罩區域，遮罩會加速處理過程，或只處理遮罩指定的像素點，
//    操作的結果總是某個連續的區域。
# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

int main(){
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    cv::Mat src = cv::imread(wd + "NFS02.jpg");
    cv::imshow("Original", src);
    cv::Rect ccomp;
    
    cv::floodFill(src, cv::Point(50, 300), cv::Scalar(155, 255, 55), &ccomp, cv::Scalar(20, 20, 20), cv::Scalar(20, 20, 20));
    // param 1: InputOutputArray類型的image，輸入/輸出單色版(通道)或3色版(通道)，8位元或浮點影像，具體參數由之後的參數指明。
    // param 2: (未列出) InputOutputArray類型的mask，表示操作遮罩。它應該為單色版(通道)，8位元，長和寬上都比輸入影像image大兩個像素點的影像。
    // param 3: cv::Point類型的seedPoint，漫水填充演算法的起始點。
    // param 4: cv::Scalar類型的newVal，像素點被染色的值，即在重繪區域像素的新值。
    // param 5: cv::Rect*類型的rect，有預設值0，一個可選的參數，用於設定floodFill函數將要重繪區域的最小邊界矩形區域
    // param 6: cv::Scalar類型的loDiff，有預設值Scalar()，表示現在觀察像素值與其設定元件鄰域像素值或者待加入該設定
    //          元件的種子像素之間的亮度或顏色的負差(lower brightness/color difference)的最大值。
    // param 7: cv::Scalar類型的UpDiff，有預設值Scalar()，表示現在觀察像素值與其設定元件鄰域像素值或者待加入該設定
    //          元件的種子像素之間的亮度或顏色的正差(lower brightness/color difference)的最大值。
    // param 8: (未列出) int類型的flags，操作標誌符號，此參數包含三個部分，較為複雜。
    //          (1) FLOODFILL_FIXED_RANGE 如果設定為這個識別字，就會考慮現在像素與種子像素之間的差，否則就考慮現在像素與其相鄰像素的差。也就是說，這個範圍是浮動的。
    //          (2) FLOODFILL_MASK_ONLY 如果設定為這個識別字，函數不會去填充改變原始影像(也就是忽略newVal)，而是去填充遮罩影像(mask)。
    //          (3) 中間8位元部分，上面關於高八位FLOODFILL_MASK_ONLY識別字中已寫明，需要輸入符合要求的遮罩。
    //              Floodfill的flags參數中間八位的值就是用於指定填充遮罩影像的值，但如果flags中間八位的值為0，則遮罩會用1來填充。
    // 
    // 所有flags可以用or操作符號連接起來，即"|"(bitwise OR)。
    // 例如，如果想用8鄰域填充，並填充固定像素值範圍，填充遮罩而不是填充來源影像，以及設填充值為38，那麼輸入的參數是下面這樣:
    // flags = 8 | FLOODFILL_MASK_ONLY | FLOODFILL_FIXED_RANGE | (38 << 8)

    cv::imshow("Processed", src);
    cv::waitKey(0);
    return 0;
}