// 離散傅立葉轉換
# include "opencv2/core/core.hpp"
# include "opencv2/imgproc/imgproc.hpp"
# include "opencv2/highgui/highgui.hpp"
# include <iostream>

int main(){

    // 此範例將展示如何計算以及顯示傅立葉轉換後的幅度影像。由於數位影像的離散性，
    // 像素質的取值範圍也是有限的，例如：在灰階影像中，像素灰階值一般在0~255之間。
    // 如果需要得到影像中的幾何結構資訊，就要使用離散傅立葉轉換。

    // 1. 以灰階模式讀取原始影像並顯示
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    cv::Mat srcImage = cv::imread(wd + "NFS02.jpg", 0);

    if(!srcImage.data){
        std::cout << "Image loaded failed!" << std::endl;
        return false;
    }
    cv::imshow("Original image", srcImage);

    // ShowHelpText();

    // 2. 將匯入影像延擴到最佳的尺寸，邊界用0填充
    // 離散傅立葉轉換的執行速度與圖片的尺寸有很大的關係。當影像是2、3、5的整數倍時，計算速度最快。
    // 為了達到快速計算的目的，經常透過新的邊緣像素的方法取得最佳影像尺寸。
    // 函數getOptimalDFTSize()用於返回最佳尺寸，而函數copyMakeBorder()用於填充邊緣像素。
    int m = cv::getOptimalDFTSize( srcImage.rows );
    int n = cv::getOptimalDFTSize( srcImage.cols );
    // 將新增的像素初始化為0
    cv::Mat padded;
    cv::copyMakeBorder(srcImage, padded, 0, m - srcImage.rows, 0, n - srcImage.cols, cv::BORDER_CONSTANT, cv::Scalar::all(0));

    // 3. 為傅立葉轉換的結果(實部和虛部)分配儲存空間
    // 傅立葉變換的結果是複數，也就是說對於每個原影像值，結果會有兩個影像值。
    // 此外，頻域值範圍遠遠超過空間值範圍，因此至少要將頻域儲存在float格式中。
    // 所以，我們將匯入影像轉換成浮點類型，並多加一個額外色板來儲存複數部分。
    // 將planes陣列組合合併成一個多色版(通道)的陣列complexI
    cv::Mat planes[] = {cv::Mat_<float>(padded), cv::Mat::zeros(padded.size(), CV_32F)};
    cv::Mat complexI;
    cv::merge(planes, 2, complexI);

    // 4. 進行就地離散傅立葉轉換
    // 這裡的離散傅立葉轉換為影像就地計算模式(in-place，匯入匯出為同一影像)。
    cv::dft(complexI, complexI);

    // 5. 將複數轉為幅值，即 => log(1 + sqrt(Re(DFT(I))^2 + Im(DFT(I))^2))
    // 複數包含實數部分(Re)和虛數部分(imaginary - Im)。
    // 離散傅立葉轉換的結果是複數，對應的幅度可以表示為 M = sqrt(Re(DFT(I))^2 + Im(DFT(I))^2)
    cv::split(complexI, planes);  // 將多色版陣列complexI分離成幾個單色版陣列。planes[0] = Re(DFT(I)), planes[1]) = Im(DFT(I))
    cv::magnitude(planes[0], planes[1], planes[0]);
    cv::Mat magnitudeImage = planes[0];

    // 6. 進行對數尺度(logarithmic scale)縮放
    // 傅立葉轉換的幅度值範圍大到不適合在螢幕上顯示。
    // 值越高顏色越白，高值為白點，低值為黑點，高低值的變化無法有效分辨。
    // 為了在螢幕上凸顯高低變化的連續性，我們可以用對數尺度來代替線性尺度。即 M = log(1 + M)
    magnitudeImage += cv::Scalar::all(1);
    cv::log(magnitudeImage, magnitudeImage); // 求自然對數

    // 7. 剪切和重分布幅度圖像限
    // 因為在第二步延擴了影像，那現在是時候將新增的像素剔除了。
    // 為了方便顯示，也可以重新分布幅度圖像線位置(註：將第五步得到的幅度圖從中間劃開，得到4張1/4子影像，
    // 將每張子影像看成幅度圖的一個象限，重新分布，即將4個角點重疊到圖片中心)。
    // 這樣的話原點(0, 0)就位移到影像中心了。
    // 若有奇數行或奇數列，進行頻譜裁剪
    magnitudeImage = magnitudeImage(cv::Rect(0, 0, magnitudeImage.cols & -2, magnitudeImage.rows & -2));
    // 重新排列傅立葉影像中的象限，使得原點位於影像中心
    int cx = magnitudeImage.cols / 2;
    int cy = magnitudeImage.rows / 2;
    cv::Mat q0(magnitudeImage, cv::Rect(0, 0, cx, cy));  // ROI區域的左上
    cv::Mat q1(magnitudeImage, cv::Rect(cx, 0, cx, cy));  // ROI區域的右上
    cv::Mat q2(magnitudeImage, cv::Rect(0, cy, cx, cy));  // ROI區域的左下
    cv::Mat q3(magnitudeImage, cv::Rect(cx, cy, cx, cy));  // ROI區域的右下
    // 交換象限(左上與右下進行交換)
    cv::Mat tmp;
    q0.copyTo(tmp);
    q3.copyTo(q0);
    tmp.copyTo(q3);
    // 交換象限(右上與左下進行交換)
    q1.copyTo(tmp);
    q2.copyTo(q1);
    tmp.copyTo(q2);

    // 8. 正規化，用0到1之間的浮點值將矩陣變換為可視的影像格式
    // 為了顯示。現在有了重分佈後的幅度圖，但是幅度值仍然超過可顯示範圍[0, 1]。
    // 我們使用mnormalize()函數將幅度值正規化到可顯示範圍。
    // In OpenCV2:
    // cv::normalize(magnitudeImage, magnitudeImage, 0, 1, CV_MINMAX);
    // In OpenCV3:
    cv::normalize(magnitudeImage, magnitudeImage, 0, 1, cv::NORM_MINMAX);

    // 9. 顯示效果圖
    cv::imshow("Frequency Domain", magnitudeImage);
    cv::waitKey();

    return 0;
}