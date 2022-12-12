/* 基本圖形的繪製 */
// 1. 在影像當中定義2D點： Point 
// 2. 顏色值表示: Scalar
// 3. 繪製直線： line
// 4. 繪製橢圓： ellipse
// 5. 繪製矩形： rectangle
// 6. 繪製圓： circle
// 7. 繪製填充的多邊形： fillPoly
// 
// 匯入程式使用的標頭檔
# include <opencv2/core/core.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>

# define WINDOW_WIDTH 600 //定義視窗大小的巨集

/* Define DrawEllipse() */
// 繪製不同角度、相同尺寸的橢圓
void DrawEllipse(cv::Mat img, double angle){
    int thickness = 2;
    int lineType = 8;

    ellipse(img, 
    cv::Point(WINDOW_WIDTH/2, WINDOW_WIDTH/2), // Center of ellipse.
    cv::Size(WINDOW_WIDTH/4, WINDOW_WIDTH/16), // Size of the ellipse.
    angle, // Rotation degree of the ellipse. (0 ~ 360)
    0, 
    360, 
    cv::Scalar(255, 129, 0),  // Blue
    thickness,  // thickness (線粗) 為 2
    lineType);  // lineType 為 8 (聯通線型)
}


/* Define DrawFilledCircle() */
// 實心圓的繪製
void DrawFilledCircle(cv::Mat img, cv::Point center){
    int thickness = -1;
    int lineType = 8;

    circle(img, 
    center,          // center of the circle.
    WINDOW_WIDTH/32, // radius of the circle.
    cv::Scalar(0, 0, 255), // color: red
    thickness,             // thickness (線粗) 為 -1 ，代表實心圓      
    lineType); 
}


/* Define DrawPolygon() */
// 凹多邊形的繪製
void DrawPolygon(cv::Mat img){
    int lineType = 8;

    // 建立一些點
    cv::Point rookPoints[1][20];
    rookPoints[0][0] = cv::Point(    WINDOW_WIDTH/4,   7*WINDOW_WIDTH/8);    
    rookPoints[0][1] = cv::Point(  3*WINDOW_WIDTH/4,   7*WINDOW_WIDTH/8);
    rookPoints[0][2] = cv::Point(  3*WINDOW_WIDTH/4,  13*WINDOW_WIDTH/16);    
    rookPoints[0][3] = cv::Point( 11*WINDOW_WIDTH/16, 13*WINDOW_WIDTH/16);
    rookPoints[0][4] = cv::Point( 19*WINDOW_WIDTH/32,  3*WINDOW_WIDTH/8);
    rookPoints[0][5] = cv::Point(  3*WINDOW_WIDTH/4,   3*WINDOW_WIDTH/8);
    rookPoints[0][6] = cv::Point(  3*WINDOW_WIDTH/4,     WINDOW_WIDTH/8);
    rookPoints[0][7] = cv::Point( 26*WINDOW_WIDTH/40,    WINDOW_WIDTH/8);
    rookPoints[0][8] = cv::Point( 26*WINDOW_WIDTH/40,    WINDOW_WIDTH/4);
    rookPoints[0][9] = cv::Point( 22*WINDOW_WIDTH/40,    WINDOW_WIDTH/4);
    rookPoints[0][10] = cv::Point(22*WINDOW_WIDTH/40,    WINDOW_WIDTH/8);
    rookPoints[0][11] = cv::Point(18*WINDOW_WIDTH/40,    WINDOW_WIDTH/8);
    rookPoints[0][12] = cv::Point(18*WINDOW_WIDTH/40,    WINDOW_WIDTH/4);
    rookPoints[0][13] = cv::Point(14*WINDOW_WIDTH/40,    WINDOW_WIDTH/4);
    rookPoints[0][14] = cv::Point(14*WINDOW_WIDTH/40,    WINDOW_WIDTH/8);
    rookPoints[0][15] = cv::Point(   WINDOW_WIDTH/4,     WINDOW_WIDTH/8);
    rookPoints[0][16] = cv::Point(   WINDOW_WIDTH/4,   3*WINDOW_WIDTH/8);
    rookPoints[0][17] = cv::Point(13*WINDOW_WIDTH/32,  3*WINDOW_WIDTH/8);
    rookPoints[0][18] = cv::Point( 5*WINDOW_WIDTH/16, 13*WINDOW_WIDTH/16);
    rookPoints[0][19] = cv::Point(   WINDOW_WIDTH/4,  13*WINDOW_WIDTH/16);

    const cv::Point* ppt[1] = { rookPoints[0] };
    int npt[] = { 20 };

    cv::fillPoly(
        img, 
        ppt, // 多邊形的頂點集為ppt
        npt, // 多邊形的頂點數目為npt
        1,   // 繪製多邊形的數量
        cv::Scalar(255, 255, 255),  // 顏色定義為白色
        lineType);

}

/* Define DrawLine() */
// 線的繪製
void DrawLine(cv::Mat img, cv::Point start, cv::Point end){
    int thickness = 2;
    int lineType = 8;
    cv::line(img, 
    start,
    end,
    cv::Scalar(0, 0, 0), 
    thickness,
    lineType);
}

/* Define main() */
// 先建立空白的Mat影像，然後使用函數繪製化學中的原子範例圖，接著繪製城堡，最後顯示繪製出的影相。
// 
// 定義一些輔助巨集
# define WINDOW_NAME1 "Plot 1" // 為視窗標題定義的巨集
# define WINDOW_NAME2 "Plot 2" // 為視窗標題定義的巨集
# define WINDOW_WIDTH 600 // 定義視窗大小的巨集

int main( void ){
    
    // 建立空白的cv::Mat影像 (空白畫布)
    cv::Mat atomImage = cv::Mat::zeros( WINDOW_WIDTH, WINDOW_WIDTH, CV_8UC3 );
    cv::Mat rookImage = cv::Mat::zeros( WINDOW_WIDTH, WINDOW_WIDTH, CV_8UC3 );

    // 1. Plot the atom
    // 1.1 Plot the ellipse.
    DrawEllipse( atomImage, 90 );
    DrawEllipse( atomImage, 0 );
    DrawEllipse( atomImage, 45 );
    DrawEllipse( atomImage, -45);

    // 1.2 Plot the center of the atom (circle).
    DrawFilledCircle( atomImage , cv::Point(WINDOW_WIDTH/2, WINDOW_WIDTH/2) );

    // 2. Plot the castle.
    // 2.1 Plot the ellipse.
    DrawPolygon( rookImage );

    // 2.2 Plot the rectangle.
    rectangle(rookImage, 
              cv::Point(0, 7*WINDOW_WIDTH/8 ),
              cv::Point( WINDOW_WIDTH, WINDOW_WIDTH),
              cv::Scalar(0, 255, 255), 
              -1,
              8);

    // 2.3 Plot some segements
    DrawLine(rookImage, cv::Point(0, 15*WINDOW_WIDTH/16), cv::Point(WINDOW_WIDTH, 15*WINDOW_WIDTH/16) );
    DrawLine(rookImage, cv::Point(WINDOW_WIDTH/4, 7*WINDOW_WIDTH/8), cv::Point(WINDOW_WIDTH/4, WINDOW_WIDTH) );
    DrawLine(rookImage, cv::Point(WINDOW_WIDTH/2, 7*WINDOW_WIDTH/8), cv::Point(WINDOW_WIDTH/2, WINDOW_WIDTH) );
    DrawLine(rookImage, cv::Point( 3*WINDOW_WIDTH/4, 7*WINDOW_WIDTH/8), cv::Point(3*WINDOW_WIDTH/4, WINDOW_WIDTH) );

    // 3. Show the two images.
    cv::imshow(WINDOW_NAME1, atomImage);
    cv::moveWindow(WINDOW_NAME1, 0, 200);
    cv::imshow(WINDOW_NAME2, rookImage);
    cv::moveWindow(WINDOW_NAME2, WINDOW_WIDTH, 200);

    cv::waitKey(0);
    return(0);
}
