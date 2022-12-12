# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>

int main(){
    // 初始化變數和隨機值
    cv::Mat image(600, 600, CV_8UC3);
    cv::RNG& rng = cv::theRNG();

    // 輪詢使用者的按鍵，按下esc、Q、q鍵程式退出，否則有鍵按下便一直更新
    while(1){
        // Parameter initialization
        int count = rng.uniform(3, 103); // 隨機產生點的數量
        std::vector<cv::Point> points; //點值

        // 隨機產生點座標
        for(int i = 0; i < count; i++){
            cv::Point point;
            point.x = rng.uniform(image.cols/4, image.cols*3/4);
            point.y = rng.uniform(image.rows/4, image.rows*3/4);
            points.push_back(point);
        }

        // 給定2D點集，尋找最小面積的包圍矩形
        cv::Point2f center;
        float radius = 0;
        cv::minEnclosingCircle(cv::Mat(points), center, radius);

        // 繪製出隨機顏色的點
        image = cv::Scalar::all(0);
        for(int i = 0; i < count; i++){
            cv::circle(image, points[i], 3, cv::Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255)), cv::FILLED, cv::LINE_AA);
        }

        // 繪製出最小面積的包圍矩形
        for(int i = 0; i < 4; i++){
            cv::circle(image, center, cvRound(radius), cv::Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255)), 2, cv::LINE_AA);
        }

        // Show the image
        cv::imshow("圓形包圍範例", image);

        // Press ESC, Q, or q, and the program exit.
        char key = (char)cv::waitKey();
        if(key == 27 || key == 'q' || key == 'Q') // 'ESC'
            break;
    }

    return 0;
}