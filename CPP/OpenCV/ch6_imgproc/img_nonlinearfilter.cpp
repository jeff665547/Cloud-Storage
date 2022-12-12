/* 非線性濾波： 中值濾波、雙邊濾波 */
// 線性濾波可以實現很多種不同的影像變換。
// 而非線性濾波，如中值濾波器和雙邊濾波器，有時可以達到更好的實現效果。
// 在很多情況下，使用鄰域像素的非線性濾波會得到更好的效果。
// 如：
// 在雜訊是散粒雜訊而不是高斯雜訊，即影像偶爾出現很大的值的時候，
// 用高斯濾波器對影像進行模糊的話，雜訊像素是不會被去除的，他們只是轉換為更為柔和
// 但仍然可見的散粒。
// 
/* 中值濾波 */
// * 中值濾波(Median filter)是一種典型的非線性濾波技術，基本思想是用像素點鄰域灰階值
//   的中值來代替該像素點的灰階值，讓周圍的像素值接近真實值，從而消除孤立的雜訊點。
// * 具體演算法步驟：(計算以點[i, j]為中心的函數視窗像素中值)
//   1. 按強度值大小排列像素點。
//   2. 選擇排列像素級的中間值作為點[i, j]的新值。
//   3. 一般採用奇數點的鄰域來計算中值，但像素點為偶數時，中值就取排序像素中間兩點的平均值。
// * 該方法在去除脈衝雜訊、鹽和胡椒雜訊的同時又能保留影像的邊緣細節。
// * 中值濾波不依賴於鄰域內那些與典型值差別很大的值(Extreme Value)。
// * 中值濾波器在處理連續影像窗函數時與線性濾波器的工作方式類似，
//   但濾波過程不再是加權運算。
// * 中值濾波器在一定的條件下可以克服常見的線性濾波器所帶來的影像細節模糊，而且對濾除
//   脈衝干擾及影像掃描雜訊非常有效，也常用於保護邊緣資訊，這使它在不希望出現邊緣模糊
//   的場合非常有用，是經典的平滑雜訊處理方法。
// * 相較於均值濾波(在均值濾波器中，由於雜訊成分被放入平均計算中，
//   所以輸出受到了雜訊的影響)更可以消除雜訊。
// * 缺點: 花費時間是均值濾波的5倍以上。
// * 缺點: 對於一些細節(特別是細、尖頂等)多的影像不太適合。
// 
/* 雙邊濾波 */
// * 雙邊濾波(Bilateral filter)是一種非線性的濾波方法，
//   是結合影像的空間鄰近度和像素質相似度的一種折衷處理，
//   同時考慮空間域資訊和灰階相似性，達到雙邊去噪的目的，具有簡單、非反覆運算、局部的特點。
// * 具體演算法步驟:
//   1. Notation:
//      A. I_p: The image value at pixel position p. (Pixel size is assumed to be 1.)
//      B. F[I]: The output of a filter F applied to the image I.
//      C. R: The set of all possible pixel values that we name the range domain.
//      D. SUMMATION(p in S) denotes a sum over all image pixels indexed by p.
//      E. ||p-q|| is the Euclidean distance between pixel locations p and q. (||.|| is the L_2 norm.)
//      F. |.| is the absolute value.
//   2. The GaussianBlur (Gaussian Convolution) filter: GC[I]_p = SUMMATION(q in S)(G_sigma(||p - q||)*I_q)
//   3. G(x, y) = (1/(2*pi*sigma^2))*exp{(-1/(2*sigma^2))*(x^2 + y^2)}, sigma is a parameter defining the neighborhood size.
//   4. The Bilateral filter: BF[I]_p = (1/W_p)*SUMMATION(q in S)(G_sigma_S(||p - q||)*G_sigma_r(|I_p - I_q|)*I_q)
//   5. W_p = SUMMATION(q in S)(G_sigma_S(||p - q||)*G_sigma_r(|I_p - I_q|)*I_q), W_p is the normalization factor.
//   6. G_sigma_S(.) is a spatial Gaussian weighting that decreases the influence of distant pixels.
//   7. G_sigma_r(.) is a range Gaussian that decreases the influence of pixels q when their intensity vlaues differ from I_p.
//   8. If sigma_r increases, then BF[I] approximate to GC[I], and G_sigma_r(.) is nearly constant over the intensity interval of the image.
//   9. Increasing the spatial parameter sigma_S(.) smooths larger features.
//   10. The range weight enforces a strict presentation of the contours.
// * 雙邊濾波可以做邊緣儲存(即保留邊緣edge preserving)。以往常用維納濾波或者高斯濾波降噪，
//   但兩者都會明顯的模糊邊緣，對於高頻細節的保護效果並不明顯。
// * 雙邊濾波器顧名思義，比高斯濾波器多了一個高斯方差，在邊緣附近，
//   離的較遠的像素不會對邊緣上的像素值影響太多，這樣就保證了邊緣附近像素值的儲存。
// * 雙邊濾波器不能夠乾淨地濾掉高頻雜訊，只能對低頻資訊進行較好地濾波。
// 
# include "opencv2/core/core.hpp"
# include "opencv2/highgui/highgui.hpp"
# include "opencv2/imgproc/imgproc.hpp"

int main(){

    // Load the original plot.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    cv::Mat image = cv::imread(wd + "NFS01.jpg");

    // Establish the window.
    cv::namedWindow("original");
    cv::namedWindow("medianBlur (Processed)");
    cv::namedWindow("bilateralFilter (Processed)");

    // Show the original plot.
    cv::imshow("original", image);
    
    cv::Mat out1, out2;

    // medianBlur()
    cv::medianBlur(image, out1, 7);
    cv::imshow("medianBlur (Processed)", out1);

    // bilateralFilter()
    cv::bilateralFilter(image, out2, 25, 25*2, 25/2);
    cv::imshow("bilateralFilter (Processed)", out2);

    cv::waitKey(0);

    return 0;
}