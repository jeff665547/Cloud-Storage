// Convex Hull 凸包
// 簡單來說，給定二維平面上的點集，凸包就是將最外層的點連接起來構成的凸邊形，
// 它是能包含點集中所有點的。
// 理解物體形狀或輪廓的一種比較有用的方法便是先計算一個物體的凸包，然後計算其凸缺陷(convexity defects)。
# include <opencv2/imgproc/imgproc.hpp>
# include <opencv2/highgui/highgui.hpp>
# include <iostream>

int main(){

    cv::Mat image(600, 600, CV_8UC3);
    cv::RNG& rng = cv::theRNG();

    // for loop, press ESC, Q, q 鍵程式退出，否則有鍵按下便一直更新
    while(1){
        // parameter initialization
        char key; 
        int count = (unsigned) rng%100 + 3; // 隨機產生點的數量
        std::vector<cv::Point> points; // 點值

        // Random generate points.
        for(int i = 0; i < count; i++){
            cv::Point point;
            point.x = rng.uniform(image.cols/4, image.cols*3/4);
            point.y = rng.uniform(image.rows/4, image.rows*3/4);
            points.push_back(point);
        }

        // Test the hull convex.
        std::vector<int> hull;
        cv::convexHull(cv::Mat(points), hull, true);

        // Paint the random color points.
        image = cv::Scalar::all(0);
        for(int i = 0; i < count; i ++){
            cv::circle(image, points[i], 3, cv::Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255)), cv::FILLED, cv::LINE_AA);
        }

        // Prepare the parameters
        int hullcount = (int)hull.size(); // 凸包的邊數
        cv::Point point0 = points[hull[hullcount - 1]]; // 連接凸包邊的座標點

        // 繪製凸包的邊
        for(int i = 0; i < hullcount; i++){
            cv::Point point = points[hull[i]];
            cv::line(image, point0, point, cv::Scalar(255, 255, 255), 2, cv::LINE_AA);
            point0 = point;
        }

        // Show the processed image.
        cv::imshow("Hull Convex example", image);

        // Press ESC, Q or q to exit the program.
        key = (char)cv::waitKey();
        if(key == 27 || key == 'q' || key == 'Q')
            break;

    }

    return 0;
}