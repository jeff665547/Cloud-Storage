/* 影像修補 */
# include <opencv2/highgui/highgui.hpp>
# include <opencv2/imgproc/imgproc.hpp>
# include <opencv2/photo/photo.hpp>
# include <iostream>

# define WINDOW_NAME1 "Original"
# define WINDOW_NAME2 "Procesed"

/* Global Variable Declarartion */
cv::Mat srcImage1, inpaintMask;
cv::Point previousPoint(-1, -1);  // 原來的點座標

static void On_Mouse(int event, int x, int y, int flags, void *){
    // 滑鼠左鍵彈起訊息
    if(event == cv::EVENT_LBUTTONUP || !(flags & cv::EVENT_FLAG_LBUTTON)){
        previousPoint = cv::Point(-1, -1);
    }else if(event == cv::EVENT_LBUTTONDOWN){
        previousPoint = cv::Point(x, y);
    }else if(event == cv::EVENT_MOUSEMOVE && (flags & cv::EVENT_FLAG_LBUTTON)){

        cv::Point pt(x, y);
        if(previousPoint.x < 0){
            previousPoint = pt;
        }
        // 繪製白色線條
        cv::line(inpaintMask, previousPoint, pt, cv::Scalar::all(255), 5, 8, 0);
        cv::line(srcImage1, previousPoint, pt, cv::Scalar::all(255), 5, 8, 0);
        previousPoint = pt;
        cv::imshow(WINDOW_NAME1, srcImage1);
    }
}

int main(int argc, char** argv){

    std::cout << "\tpress ESC to exit the program." << std::endl;
    std::cout << "\tpress 2 to restore the image." << std::endl;
    std::cout << "\tpress 1 or space to inpaint the image." << std::endl;

    // Load the raw image and initialize the mask.
    std::string wd = "C:/Users/jeff/Desktop/ProjectTemplate/src/Example/app/OpenCV/ch8_imgcontour_inpaint/";
    cv::Mat srcImage = cv::imread(wd + "NFS01.jpg", -1);

    if(!srcImage.data){
        std::cout << "Loaded failed!" << std::endl;
        return false;
    }
    srcImage1 = srcImage.clone();
    inpaintMask = cv::Mat::zeros(srcImage1.size(), CV_8U);

    // Show the original plot
    cv::imshow(WINDOW_NAME1, srcImage1);

    // set the mouse callback message
    cv::setMouseCallback(WINDOW_NAME1, On_Mouse, 0);

    // query the input
    while(1){
        // get the keypad
        char c = (char)cv::waitKey();

        // press ESC, and quit the program
        if(c == 27){
            break;
        }

        // press 2, restore the image
        if(c == '2'){
            inpaintMask = cv::Scalar::all(0);
            srcImage.copyTo(srcImage1);
            cv::imshow(WINDOW_NAME1, srcImage1);
        }

        // press 1 or space to conduct the image inpaint.
        if(c == '1' || c == ' '){
            cv::Mat inpaintedImage;
            cv::inpaint(srcImage, inpaintMask, inpaintedImage, 3, cv::INPAINT_TELEA);
            cv::imshow(WINDOW_NAME2, inpaintedImage);
        }
    }

    return 0;
}