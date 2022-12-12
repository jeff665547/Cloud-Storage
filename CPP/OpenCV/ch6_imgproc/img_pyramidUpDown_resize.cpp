/* 影像金字塔與圖片尺寸縮放 */
// 我們經常將某種尺寸的影像轉換為其他尺寸的影像，如果要放大或者縮小圖片的尺寸，可以使用OpenCV提供的如下兩種方法：
// resize() 函數。(最直接的方式)
// pyrUp()、pyrDown()函數。即影像金字塔相關的兩個參數，對影像進行向上採樣和向下採樣的操作。
// pyrUp、pyrDown其實和專門用作放大和縮小影像尺寸的resize在功能上差不多，披著影像金字塔的皮，但還是在對影像進行放大和縮小操作。
// 比較不一樣的是pyrUp、pyrDown在OpenCV的imgproc模組中的Image Filtering子模組裡，
// 而resize在imgproc模組的Geometric Image Transformations子模組裡。
// 
// 影像金字塔
// 影像金字塔識影像中多尺度表達的一種，最主要用於影像的分割。
// 影像金字塔最初用於機器視覺和影像壓縮，一幅影像的金字塔是一系列以金字塔形狀排列的，
// 解析度逐步降低且來源於同一張原始圖的影像集合。其透過梯次向下採樣獲得，直到某點某個終止條件才停止採樣。
// 金字塔的底部是待處理影像的高解析度表示，而頂部則是低解析度的近似圖。層級越高，則影像越小，解析度越低。
// 
// 影像金字塔的向上採樣以及向下採樣
// * 對影像向上採樣: pyrUp()，過程中會使用到高斯金字塔(Gaussianpyramid)
// * 對影像向下採樣: pyrDown()，過程中會使用到高斯金字塔以及拉普拉斯金字塔(Laplacianpyramid)
// 這裡的向下採樣與向上採樣，是針對影像的尺寸而言的(和金字塔的方向相反)，
// 向上就是影像尺寸加倍，向下就是影像尺寸減半。然而金字塔向上影像其實是在縮小，向下影像其實是在放大。
// PryUp和PryDown不是戶逆的
// 
// 高斯金字塔(Gaussianpyramid)
// * 對影像的向下取樣
//   這個過程實際上就是一個重複高斯平滑並重新對圖象採樣的過程。
//   1. 對於原始圖像先進行一次高斯平滑處理，使用高斯核(5 * 5 kernel)進行一次卷積處理。
//   2. 對圖像進行採樣，進一步去除圖像中的偶數行和積數列，從而得到一張圖像。
//   3. 然後重複上面兩步，直到最終的目標圖像為止。
//   由上可知，每次循環中，得到的結果圖像只有原圖像的1/4大小。
//   向下採樣會逐漸丟失圖像信息，為非線性處理。
// 
// * 對影像的向上取樣
//   1. 將圖像在每個方向擴大為原來的兩倍，新增的行和列(偶數行和偶數列)以0填充。
//   2. 使用高斯核(5 * 5 kernel)對得到的圖像進行一次高斯平滑處理，獲得"新增像素"的近似值。
//   此過程得到的圖像為放大後的圖像，與原圖相比會比較模糊，因為在縮放的過程中丟失些圖像訊息，
//   如果想在縮放過程中減少圖像訊息的損失，就需要用到第二個圖像金字塔 -- 拉普拉斯金字塔。
// 
// 拉普拉斯金字塔(Laplacianpyramid)
// 拉普拉斯金字塔可以視為殘差金字塔，用來儲存下採樣後圖片與原始圖片的差異。
// 上面提到了基於高斯金字塔，一個原始圖像G_(i)，先進行向下採樣得到G_(i-1)，
// 再對G_(i-1)進行向上採樣得到Up(Down(G_i))，最終得到的Up(Down(G_i))與原始的G_i是存在差異的。
// 這是因為向下採樣丟失的訊息並不能由向上採樣進行恢復。
// 如果我們想要完全恢復原始影像，那麼我們在進行採樣的時候就需要保留差異訊息。
// 這就是拉普拉斯金字塔的核心思想，每次向下採樣後，將在向上採樣，得到向上採樣的Up(Down(G_i))後，
// 紀錄Up(Down(G_i))與G_i的差異訊息。
// 也就是L(0) = G(0) - Up(G(1)) => L(i) = G(i) - Up(Down(G(i)))
// OpenCV實作上為L(i) = G(i) - PyrUp(G_i+1)
// 
// 尺寸調整resize()
// resize() 為 OpenCV中專門用來調整影像大小的函數
// 此函數將來源影像精確地轉換為指定尺寸的目標影像。
// 如果還原影像中設定了ROI(Region of Interest)，那麼resize()函數會對來源影像的
// ROI區域進行調整影像尺寸的操作，來輸出到目標影像中。
// 若目標影像中已經設定了ROI區域，不難理解resize()將會對來源影像進行尺寸調整，
// 並且填充到目標影像的ROI中。
# include <opencv2/opencv.hpp>
# include <opencv2/imgproc/imgproc.hpp>

int main(){

    // Load the original image.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch6_imgproc/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg");
    cv::Mat tmpImage, dstImage1, dstImage2, dstImage3, dstImage4;
    tmpImage = srcImage;

    // Show the original plot.
    cv::imshow("Original", srcImage);

    // Resize the image size.
    cv::resize(tmpImage, dstImage1, cv::Size(tmpImage.cols/2, tmpImage.rows/2), (0, 0), (0, 0), 3);
    cv::resize(tmpImage, dstImage2, cv::Size(tmpImage.cols*2, tmpImage.rows*2), (0, 0), (0, 0), 3);
    // param 1: 代表輸入影像，即來源影像，為cv::Mat類別的物件。
    // param 2: 代表輸出影像，當其非零時，有著dsize (param 3) 的尺寸。
    // param 3: cv::Size類型的dsize，輸出影像的大小，如果它等於0，由下面式子進行計算:
    //              dsize = cv::Size(round(fx*src.cols), round(fy*src.rows))，其中，dsize、fx、fy都不能為0。
    // param 4: 為double類型的fx，沿水平軸的縮放係數，有預設值0，當其為0時，由下面式子進行計算：
    //              (double)dsize.width/src.cols
    // param 5: 為double類型的fy，沿垂直軸的縮放係數，有預設值0，當其為0時，由下面式子進行計算：
    //              (double)dsize.height/src.rows
    // param 6: int類型的interploation，用於指定差值的方式，預設為INTER_LINEAR(線性插值)。
    //          可選的插值方式如下:
    //          INTER_NEAREST: 最近鄰插值
    //          INTER_LINEAR: 線性插值(預設值)
    //          INTER_AREA: 區域插值(利用像素區域關係的重採樣插值)，縮小影像常使用
    //          INTER_CUBIC: 三次樣條插值 (超過4 x 4 像素鄰域內的雙三次插值)，放大影像使用，但速度慢
    //          INTER_LANCZOS4: Lanczos插值 (超過8 x 8 像素鄰域的Lanczos插值)，放大影像常使用，速度快

    // Show the processed image. (resize)
    cv::imshow("Resize One", dstImage1);
    cv::imshow("Resize Two", dstImage2);

    // PyrUP
    cv::pyrUp(tmpImage, dstImage3, cv::Size(tmpImage.cols*2, tmpImage.rows*2));
    // param 1: 代表輸入影像，即來源影像，為cv::Mat類別的物件。
    // param 2: 代表輸出影像，和來源影像有一樣的尺寸及類型。
    // param 3: dstsize，輸出影像的大小，預設情況下，由cv::Size(src.cols*2, src.rows*2)來進行計算，
    //          而且需要滿足下列條件：
    //          |dstsize.width - src.cols*2| <= (dstsize.width mod 2)
    //          |dstsize.heihgt - src.rows*2| <= (dstsize.heihgt mod 2)
    // param 4: borderType，邊界模式，一般不去管它

    // Show the processed image (PyrUP).
    cv::imshow("PyrUP", dstImage3);

    // PyrDown
    cv::pyrDown(tmpImage, dstImage4, cv::Size(tmpImage.cols/2, tmpImage.rows/2));
    // param 1: 代表輸入影像，即來源影像，為cv::Mat類別的物件。
    // param 2: 代表輸出影像，和來源影像有一樣的尺寸及類型。
    // param 3: dstsize，輸出影像的大小，預設情況下，由cv::Size((src.cols + 1)/2, (src.rows + 1)*2)來進行計算，
    //          而且需要滿足下列條件：
    //          |dstsize.width*2 - src.cols| <= 2
    //          |dstsize.heihgt*2 - src.rows| <= 2
    // param 4: borderType，邊界模式，一般不去管它

    // Show the processed image (PyrDown)
    cv::imshow("PyrDown", dstImage4);

    cv::waitKey(0);
    
    return 0;
}