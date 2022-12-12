# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <iostream>

// 再下面的程式碼中，我們透過一個影像遮罩(mask)，直接將插入處的像素設定為logo影像的像素值
bool ROI_AddImage(){

    // 1. Load the images
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    cv::Mat srcImage1 = cv::imread(wd + "NFS01.jpg");
    cv::Mat logoImage = cv::imread(wd + "subaru.png");

    if(!srcImage1.data){
        std::cout << "Load the srcImage failed !!!" << std::endl;
        return false;
    }
    if(!logoImage.data){
        std::cout << "Load the logoImage failed !!!" << std::endl;
        return false;
    }

    // 2. Define a Mat and set the ROI of that image.
    cv::Mat imageROI = srcImage1(cv::Rect(400, 100, logoImage.cols, logoImage.rows));

    // 3. Load the mask (必須是灰階圖)
    cv::Mat mask = cv::imread(wd + "subaru.png", 0);

    // 4. Copy the mask to the ROI (使用mask才能讓黑色背景去背，保留精華的部分)
    logoImage.copyTo(imageROI, mask);

    // 5. Show the result. (影像疊加)
    cv::namedWindow("<1> Use the ROI to realize the image addition example.");
    cv::imshow("<1> Use the ROI to realize the image addition example.", srcImage1);
    cv::waitKey(0);

    return true;
}

// 線性混合操作
bool LinearBlending(){
    // 0. 定義一些區域變數
    double alphaValue = 0.5;
    double betaValue;
    cv::Mat srcImage2, srcImage3, dstImage;

    // 1. Load the image (兩幅圖片需為同樣的類型和尺寸)
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    srcImage2 = cv::imread(wd + "NFS01.jpg");
    srcImage3 = cv::imread(wd + "NFS02.jpg");

    // 讀取兩幅影像並作錯誤處理
    if (!srcImage2.data) {
        std::cout << "Load the srcImage2 failed !!!" << std::endl;
        return false;
    }
    if (!srcImage3.data){
        std::cout << "Load the srcImage3 failed !!!" << std::endl;
        return false;
    }

    // 2. Image mixture (做影像加權操作)
    betaValue = (1.0 - alphaValue);
    cv::addWeighted(srcImage2, alphaValue, srcImage3, betaValue, 0.0, dstImage);

    // 3. 建立並顯示原圖視窗
    cv::namedWindow("<2> Linear mixture (Original image)", 1);
    cv::imshow("<2> Linear mixture (Original image)", srcImage2);
    cv::waitKey(0);

    cv::namedWindow("<3> Linear mixture (Processed image)", 1);
    cv::imshow("<3> Linear mixture (Processed image)", dstImage);
    cv::waitKey(0);

    return true;
}

// 影像疊加 + 線性混合操作
bool ROI_LinearBlending(){

    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";

    // 1. 讀取影像
    cv::Mat srcImage4 = cv::imread(wd + "NFS01.jpg", 1);
    cv::Mat logoImage = cv::imread(wd + "subaru.png", 1);

    if (!srcImage4.data){
        std::cout << "Load srcImage4 failed!" << std::endl;
        return false;
    }
    if (!logoImage.data){
        std::cout << "Load logoImage failed!" << std::endl;
        return false;
    }

    // 2. 定義一個Mat類型並給其設定ROI區域
    cv::Mat imageROI;
    // Method 1
    imageROI = srcImage4(cv::Rect(200, 250, logoImage.cols, logoImage.rows));
    // Method 2
    // imageROI = srcImage4(cv::Range(250, 250+logoImage.rows), cv::Range(200, 200+logoImage.cols));

    // 3. 將logo加到原圖上
    cv::addWeighted(imageROI, 0.5, logoImage, 0.3, 0., imageROI);

    // 4. 顯示結果
    cv::namedWindow("<4> ROI + Linear Blending");
    cv::imshow("<4> ROI + Linear Blending", srcImage4);
    cv::waitKey(0);

    return true;
}

int main(){

    system("color 5E"); // DOS 環境

    /* ROI區域影像疊加 & 影像混合 */
    // ROI (Region of Interest) 感興趣區域
    // 使用ROI指定想讀入的目標可以減少處理時間，增加精確度以及便利性
    // 定義ROI的兩種方法
    // 1. 表示矩形區域 Rect() 構造函數的前兩個參數為指定矩形的左上角座標，後兩個參數為指定矩形的長寬
    cv::Mat imageROI;
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    cv::Mat image = cv::imread(wd + "NFS01.jpg");
    cv::Mat logo = cv::imread(wd + "logo.jpg");
    cv::Mat logoImage = cv::imread(wd + "logo.jpg");
    imageROI = image(cv::Rect(500, 250, logo.cols, logo.rows));

    // 2. 指定感興趣的行或列的範圍 Range() 指從起始索引到終止索引(不包括終止索引)的一段連續序列。
    imageROI = image(cv::Range(250, 250 + logoImage.rows), cv::Range(200, 200 + logoImage.cols));

    // 影像疊加
    ROI_AddImage();

    // 線性混合操作 addWeighted()函數 (計算兩個影像陣列的加權和)
    // I_New(x) = (1-a)*I_Original1(x) + a*I_Original2(x),   I_Original1(x) 和 I_Original2(x) 可為影像或視訊，若為視訊，則代表影像過場效果。
    // void (InputArray src1, double alpha, InputArray src2, double beta, double gamma, OutputArray dst, int dtype = -1);
    // param 1: 需要加權的第一個陣列，常填一個cv::Mat。
    // param 2: 表示第一個陣列的權重。
    // param 3: 需要加權的第二個陣列，它需要和第一個陣列擁有相同的尺寸以及色板(通道)數。
    // param 4: 表示第二個陣列的權重。
    // param 5: 一個加到權重總和上的標量值，代表混合操作後的增加值。 dst = src1[I]*alpha + src2[I]*beta + gamma; I代表是多維陣列的索引值
    // param 6: 輸出的陣列，它和輸入的兩個陣列擁有相同的尺寸和色版數。
    // param 7: 輸出陣列的可選深度，預設值為-1，即等同於src1, depth()。
    // 注意: 在遇到多色板(通道)陣列的時候，每個色板都需要獨立地進行處理。
    // 當輸出陣列的深度為CV_32S時，此函數就不適用了。(記憶體溢出)
    LinearBlending();

    // 影像疊加 + 線性混合操作
    ROI_LinearBlending();

    return 0;
}

