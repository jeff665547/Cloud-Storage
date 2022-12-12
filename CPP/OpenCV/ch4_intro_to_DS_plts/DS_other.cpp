# include <opencv2/opencv.hpp>
# include <iostream>
# include <opencv2/core.hpp>

int main(){

    // Define and output 2D point.
    cv::Point2f p(6, 2);
    std::cout << "[2D point] p = " << p << ";\n" << std::endl;

    // Define and output 3D point.
    cv::Point3f p3f(8, 2, 0);
    std::cout << "[3D point] p3f = " << p3f << ";\n" << std::endl;

    // Define and output the std::vector based on the cv::Mat format
    std::vector<float> v;
    v.push_back(3);
    v.push_back(5);
    v.push_back(7);

    // std::cout << "[original vector] vec = " << v << ";\n" << std::endl; // This will lead to error since the operand should not be a vector.
    std::cout << "[vector based on the Mat] shortvec = " << cv::Mat(v) << std::endl << std::endl;

    // Define and output the std::vector point
    std::vector<cv::Point2f> points(20);
    for (size_t i = 0; i < points.size(); ++i)
    points[i] = cv::Point2f((float)(i * 5), (float)(i * 7));

    std::cout << "[2D points vector] points = " << points << ";"; 

    // Frequently used data structure and function
    // Point: Point類別，Point類別資料結構表示了二維坐標系下的點，即由其影像座標x和y指定的2D點。
    cv::Point point;
    point.x = 10;
    point.y = 8;

    cv::Point point2 = cv::Point(10, 8);
    // 另外，在OpenCV中有如下定義：
    typedef cv::Point_<int> Point2i;
    typedef cv::Point2i Point;
    typedef cv::Point_<float> Point2f;
    // 所以，Point_<int>、Point2i、Point互相等價，Point_<float>、Point2f互相等價。


    // Color: Scalar類別，Scalar()表示具有4個元素的陣列，在OpenCV中被大量用於傳遞像素值。
    // e.g. RGB顏色值。而RGB顏色值為3個參數，對於Scalar函數來說，如果用不到第四個參數，
    // 則不需要寫出來。若只寫三個參數，OpenCV會認為我們就想表示三個參數。
    cv::Scalar(122, 129, 210); // 122 為藍色分量，129 為綠色分量，210 為紅色分量。
    // Scalar類別的源頭為Scalar_類別，而Scalar_類別是Vec4x的一個變種，我們常用的Scalar其實就是Scalar_<double>,
    // 這就說明了為什麼有很多函數的參數可以是Mat也可以是Scalar。

    // Size: Size類別，在OpenCV中有如下定義:
    typedef cv::Size_<int> Size2i; // Size_是個模板類別，在這裡Size_<int>表示其類別體內部的模板所代表的類型為int，並且將她取個新名字Size2i
    typedef Size2i Size;       // 給已知的資料類型Size2i起個新名字，叫Size，因此，Size_<int>、Size2i、Size這三個類型名等價。
    cv::Size(5, 5); // 建構出的Size寬度和高度都為5，即xxx.width和xxx.height都為5

    // Rect: Rect類別，Rect類別的成員變數有x、y、width、height，分別為左上角點的座標和矩形的寬和高。常用的成員函數有:Size()返回值為Size;
    // area()返回矩形的面積；contains(Point)判斷點是否在矩形內；inside(Rect)函數判斷矩形是否在該矩形內；tl()返回左上角點座標；br()返回右下角點座標。
    // 另外，如果想求兩個矩形的交集和聯集，可以用如下格式：
    cv::Rect rect1, rect2;
    cv::Rect interrect = rect1 & rect2;
    cv::Rect unionrect = rect1 | rect2;

    // 如果想讓矩形進行平移操作和縮放操作，可以這樣寫:
    cv::Point pt = cv::Point(10, 8);
    cv::Size sz = cv::Size(5, 6);
    // cv::Size rect = cv::Rect(10, 3, 100, 100);
    // cv::Rect rectShift = rect + pt;
    // cv::Rect rectScale = rect + sz;

    // 顏色空間轉換：cvtColor()函數
    // cvtColor()函數是OpenCV裡的顏色空間轉換函數，可以實現RGB顏色向HSV、HSI等顏色空間的轉換，也可以轉換為灰階影像。
    // void cvtColor(InputArray src, OutputArray dst, int code, int dstCn = 0)
    // param 1: 輸入影像
    // param 2: 輸出影像
    // param 3: 顏色空間轉換的識別字，e.g. COLOR_BGR2BGRA，其中COLOR為巨集名稱
    // param 4: 目標影像的色板(通道)數，如果參數為0，代表輸出影像使用輸入影像的色板(通道)數。
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch4_intro_to_DS_plts/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg"), dstImage;
    // cv::cvtColor(srcImage, dstImage, CV_GRAY2BGR); // (OpenCV 2) 轉換原始圖為灰階圖。
    cv::cvtColor(srcImage, dstImage, cv::COLOR_BGR2GRAY); // (OpenCV 3) 轉換原始圖為灰階圖。

    cv::imshow("After: ", dstImage);
    cv::waitKey(0);

    // 其他常用的小知識 (@ OpenCV中的Core模組)
    // 1. Matx是個羽量級的Mat，必須在使用前規定好大小，比如一個2*3的float型的Matx，可以宣告Matx23f.
    // 2. Vec是Matx的一個衍生類別，是一個一維的Matx，跟vector很相似。
    // 3. Range類別其實就是為了使OpenCV的使用更像MATLAB而產生的。
    //    如:Range::all()其實就是MATLAB裡的符號。而Range(a, b)其實就是MATLAB中的 a : b ，注意這裡的a和b都是整數型。
    // 4. OpenCV中防止記憶體溢出的函數有alignPtr、alignSize、allocate、deallocate、fastMalloc、fastFree等。
    // 5. <math.h>裡的一些函數使用起來很方便，
    //    有計算向量角度的函數fastAtan2、
    //    計算立方根的函數cubeRoot、
    //    向上取整數函數cvCeil、
    //    向下取整數函數cvFloor、
    //    四捨五入函數cvRound、
    //    判斷引數是否無窮大cvIsInf、
    //    判斷引數是否不是一個數cvIsNaN
    // 6. 顯示文字相關的函數有getTextSize、cvInitFont、putText
    // 7. 作圖相關的函數有circle、clipLine、ellipse、ellipse2Poly、line、rectangle、polylines、LineIterator。
    // 8. 填充相關的函數有fillConvexPoly、fillPoly。
    // 9. 初始化亂數狀態的產生器：RNG。


    return 0;
}