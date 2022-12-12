// setMouseCallback() 用於為指定的視窗設定滑鼠回呼函數。
// void setMouseCallback(const string& winname, MouseCallback onMouse, void* userdata = 0)
// param 1: winname 指視窗的名字
// param 3: userdata，用戶定義的傳遞到回呼函數的參數，有預設值為0。
// param 2: onMouse 為指定視窗裡每次滑鼠事件發生的時候，被使用的函數指標。這個函數的原型的大概形式為
// void Foo(int event, int x, int y, int flags, void* param)。其中
//      param 1: event是EVENT_+變數之一，
//      param 2 & 3: x和y是滑鼠指標在影像座標系(注意: 不是視窗座標系)中的座標值，
//      param 4: flags是EVENT_FLAG的組合，
//      param 5: param是使用者定義的傳遞到SetMouseCallback函式呼叫的參數。
// 如: EVENT_MOUSEMOVE為滑鼠移動訊息、EVENT_LBUTTONDOWN為滑鼠左鍵按下訊息等。
// 
// 下方範例程式中的on_MouseHandle就是滑鼠訊息回呼函數。
// 其中一個switch語句指出了各種類型的滑鼠訊息，如
// 滑鼠移動訊息EVENT_MOUSEMOVE、左鍵按下訊息EVENT_LBUTTONDOWN、左鍵抬起訊息EVENT_LBUTTONUP，
// 並對其進行了處理，以得到隨機顏色的矩形繪製功能。

# include <opencv2/opencv.hpp>

# define WINDOW_NAME "Program Window"   // 為視窗標題定義的巨集

/* global functioin declaration */
void on_MouseHandle(int event, int x, int y, int flags, void* param);
void DrawRectangle(cv::Mat& img, cv::Rect box);
void ShowHelpText();

/* global variable declaration */
cv::Rect g_rectangle;
bool g_bDrawingBox = false; // 是否進行繪製(g_b => global bool)
cv::RNG g_rng(12345);  // random number generator

/* on_MouseHandle() 函數 */
void on_MouseHandle(int event, int x, int y, int flags, void* param){
    cv::Mat& image = *(cv::Mat*) param;
    switch(event){
        // 滑鼠移動訊息
        case cv::EVENT_MOUSEMOVE:
        {
            if(g_bDrawingBox) // 如果是否進行繪製的識別字為真，則記錄下長和寬到RECT型變數中
            {
                g_rectangle.width = x - g_rectangle.x;
                g_rectangle.height = y - g_rectangle.y;
            }
        }
            break;
        
        // 左鍵按下訊息
        case cv::EVENT_LBUTTONDOWN:
        {
            g_bDrawingBox = true;
            g_rectangle = cv::Rect(x, y, 0, 0); // 紀錄起始點
        }
            break;

        // 左鍵鬆開訊息
        case cv::EVENT_LBUTTONUP:
        {
            g_bDrawingBox = false; // 設識別字為false
            // 對寬和高小於0的處理
            if( g_rectangle.width < 0 ){
                g_rectangle.x += g_rectangle.width;
                g_rectangle.width *= -1;
            }
            if( g_rectangle.height < 0 ){
                g_rectangle.y += g_rectangle.height;
                g_rectangle.height *= -1;
            }
            // 使用函數進行繪製
            DrawRectangle( image, g_rectangle );
        }
            break;
    }
}

/* DrawRectangle() 函數 */
void DrawRectangle(cv::Mat& img, cv::Rect box){
    cv::rectangle(img, box.tl(), box.br(), cv::Scalar(g_rng.uniform(0, 255), g_rng.uniform(0, 255), g_rng.uniform(0, 255))); // 隨機顏色
}

/* main() 函數 */
int main(int argc, char** argv){
    // 1. prepare parameters
    g_rectangle = cv::Rect(-1, -1, 0, 0);
    cv::Mat srcImage(600, 800, CV_8UC3), tempImage;
    srcImage.copyTo(tempImage); // 複製來源圖到臨時變數
    g_rectangle = cv::Rect(-1, -1, 0, 0);
    srcImage = cv::Scalar::all(0); // cv::Scalar 被用來設置opencv中圖片的顏色，all為將裡面的elements全部設為0

    // 2. 設定滑鼠操作回呼函數
    cv::namedWindow(WINDOW_NAME);
    cv::setMouseCallback(WINDOW_NAME, on_MouseHandle, (void*)&srcImage); // 畫圖畫在srcImage上面

    // 3. 程式主迴圈，當進行繪製的識別字為真時，進行繪製
    for(;;){
        srcImage.copyTo(tempImage); // 複製來源圖到臨時變數
        if (g_bDrawingBox){
            DrawRectangle( tempImage, g_rectangle ); 
            // 當進行繪製的識別字為真，則進行繪製
            // 滑鼠壓下去或是移動的時候進行繪製，但此時是繪製在tempImage上面。
            // 滑鼠鬆開的時候進行繪製，而且鬆開之後是繪製在srcImage上面。
            // 接著再利用for迴圈把srcImage複製給tempImage。
        }
        cv::imshow( WINDOW_NAME, tempImage ); 
        if (cv::waitKey(10) == 27) break; // 按下ESC鍵，程式退出
    }
    
    return 0;
}