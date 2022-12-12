# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <iostream>

bool MultiChannelBlending(){
    // 0 定義相關變數
    cv::Mat srcImage;
    cv::Mat logoImage;
    std::vector<cv::Mat> channels;
    cv::Mat imageBlueChannel;

    // 藍色色版(通道)部分
    // 1 Load the images.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    logoImage = cv::imread(wd + "subaru.png", 0);
    srcImage = cv::imread(wd + "NFS01.jpg");

    if(!logoImage.data){
        std::cout << "Oh, no, load the logoImage failed! " << std::endl;
        return false;
    }
    if(!srcImage.data){
        std::cout << "Oh, no, load the srcImage failed! " << std::endl;
        return false;
    }

    // 2 把一個三色版影像轉換成三個單色版影像
    cv::split(srcImage, channels); // 分離色彩色版
    
    // 3 將原圖的藍色色版引用返回給imageBlueChannel，注意是引用，相當於兩者等價，修改其中一個另一個跟著變
    imageBlueChannel = channels.at(0);

    // 4 將原圖藍色色版的(500, 250)座標處右下方一塊區域和logo圖進行加權動作，將得到的混合結果存到imageBlueChannel中
    cv::addWeighted(imageBlueChannel(cv::Rect(500, 250, logoImage.cols, logoImage.rows)), 1.0, 
                    logoImage, 0.5, 0, imageBlueChannel(cv::Rect(500, 250, logoImage.cols, logoImage.rows)));

    // 5 將三個單色版重新合併成一個三色版
    cv::merge(channels, srcImage);

    // 6 顯示效果圖
    cv::namedWindow("<1> Original + blue logo");
    cv::imshow("<1> Original + blue logo", srcImage);


    // 綠色色版(通道)部分
    // 0 定義相關變數
    cv::Mat imageGreenChannel;    

    // 1 Load the images.
    logoImage = cv::imread(wd + "subaru.png", 0);
    srcImage = cv::imread(wd + "NFS01.jpg");

    if(!logoImage.data){
        std::cout << "Oh, no, load the logoImage failed! " << std::endl;
        return false;
    }
    if(!srcImage.data){
        std::cout << "Oh, no, load the srcImage failed! " << std::endl;
        return false;
    }

    // 2 把一個三色版影像轉換成三個單色版影像
    cv::split(srcImage, channels); // 分離色彩色版
    
    // 3 將原圖的綠色色版引用返回給imageGreenChannel，注意是引用，相當於兩者等價，修改其中一個另一個跟著變
    imageGreenChannel = channels.at(1);

    // 4 將原圖藍色色版的(500, 250)座標處右下方一塊區域和logo圖進行加權動作，將得到的混合結果存到imageBlueChannel中
    cv::addWeighted(imageGreenChannel(cv::Rect(500, 250, logoImage.cols, logoImage.rows)), 1.0, 
                    logoImage, 0.5, 0, imageGreenChannel(cv::Rect(500, 250, logoImage.cols, logoImage.rows)));

    // 5 將三個單色版重新合併成一個三色版
    cv::merge(channels, srcImage);

    // 6 顯示效果圖
    cv::namedWindow("<2> Original + green logo");
    cv::imshow("<2> Original + green logo", srcImage);


    // 紅色色版(通道)部分
    // 0 定義相關變數
    cv::Mat imageRedChannel;    

    // 1 Load the images.
    logoImage = cv::imread(wd + "subaru.png", 0);
    srcImage = cv::imread(wd + "NFS01.jpg");

    if(!logoImage.data){
        std::cout << "Oh, no, load the logoImage failed! " << std::endl;
        return false;
    }
    if(!srcImage.data){
        std::cout << "Oh, no, load the srcImage failed! " << std::endl;
        return false;
    }

    // 2 把一個三色版影像轉換成三個單色版影像
    cv::split(srcImage, channels); // 分離色彩色版
    
    // 3 將原圖的綠色色版引用返回給imageRedChannel，注意是引用，相當於兩者等價，修改其中一個另一個跟著變
    imageRedChannel = channels.at(2);

    // 4 將原圖藍色色版的(500, 250)座標處右下方一塊區域和logo圖進行加權動作，將得到的混合結果存到imageBlueChannel中
    cv::addWeighted(imageRedChannel(cv::Rect(500, 250, logoImage.cols, logoImage.rows)), 1.0, 
                    logoImage, 0.5, 0, imageRedChannel(cv::Rect(500, 250, logoImage.cols, logoImage.rows)));

    // 5 將三個單色版重新合併成一個三色版
    cv::merge(channels, srcImage);

    // 6 顯示效果圖
    cv::namedWindow("<3> Original + red logo");
    cv::imshow("<3> Original + red logo", srcImage);

    return true;
}

int main(){

    // 色版(通道)分離 split()
    // split 函數用於將一個多色版陣列分成幾個單色版陣列。這裡的array按語意翻譯為數組或陣列。
    // void split(const cv::Mat& src, cv::Mat*mvbegin);
    // void split(InputArray m, OutputArray mv);
    // param 1: 填我們需要進行的多色版陣列。
    // param 2: 填函數的輸出陣列，或者輸出的vector容器。
    // split函數分割多色版陣列轉換成獨立的單色版陣列

    cv::Mat srcImage;
    cv::Mat imageROI;
    cv::Mat logoImage;
    std::vector<cv::Mat> channels;
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    srcImage = cv::imread(wd + "NFS01.jpg");
    logoImage = cv::imread(wd + "subaru.png", 0); // 灰階影像

    // 把一個3色版影像轉換成3個單色版影像
    cv::split(srcImage, channels); // 分離色彩色版(通道)
    imageROI = channels.at(0);
    cv::addWeighted(imageROI(cv::Rect(500, 250, logoImage.cols, logoImage.rows)), 1.0, 
                    logoImage, 0.5, 0, imageROI(cv::Rect(500, 250, logoImage.cols, logoImage.rows)));
    cv::merge(channels, srcImage);

    cv::namedWindow("sample");
    cv::imshow("sample", srcImage);


    // 色版(通道)合併 merge()
    // merge()函數是split()函數的逆向操作----將多個陣列合併成一個多色版的陣列。
    // 他透過組合一些給定的單色版(通道)陣列，將這些孤立的單色版陣列合併成一個多色版(通道)的陣列，從而建立出一個由多個
    // 單色版(通道)陣列組成的多色版(通道)陣列。
    // 關於組合的細節，輸出矩陣中的每個元素都將是輸出陣列的串接。其中，第i個輸入陣列的元素被視為mv[i]。
    // C一般用其中的cv::Mat::at()方法對某個色版(通道)進行存取，也就是這樣使用: channels.at(0)。
    // 上面的Mat::at()返回一個引用(reference)到指定的陣列元素，也就是說修改其中一個，另一個也會隨之改變。
    // C++: void merge(const Mat* mv, size_tcount, OutputArray dst)
    // C++: void merge(InputArrayOfArrays mv, OutputArray dst)
    // param 1: 填需要被合併的輸入矩陣或vector容器的陣列，這個mv參數中所有的矩陣必須有著一樣的尺寸和深度。
    // param 2: 當mv為一個空白的C陣列時，代表輸入的矩陣個數，這個參數顯然必須大於1。
    // param 3: 輸出矩陣，和mv[0]擁有一樣的尺寸和深度，並且色版(通道)的數量是矩陣陣列中的色版的總數。
    cv::Mat imageBlueChannel;
    cv::Mat imageGreenChannel;
    cv::Mat imageRedChannel;
    // std::vector<cv::Mat> channels;    
    // std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch5_intro_to_core_module/";
    cv::Mat srcImage5 = cv::imread(wd + "NFS01.jpg");
    // 把一個三色版(通道)影像轉換成三個單色版(通道)影像
    cv::split(srcImage5, channels); // 分離色彩色版(通道)
    imageBlueChannel = channels.at(0);  // 藍色分量
    imageGreenChannel = channels.at(1);  // 綠色分量
    imageRedChannel = channels.at(2);  // 紅色分量


    system("color 9F");
    if (MultiChannelBlending()){
        std::cout << "Success!! This is what you want !" << std::endl;
    }
    cv::waitKey(0);
    
    return 0;
}
