// 重載運算子
// 此檔案放類別的定義描述
class Point2D{
    public:
        Point2D();
        Point2D(int x, int y);
        int getX();
        int getY();
        void setX(int x);
        void setY(int y);
        Point2D operator+(Point2D &p); // 重載+運算子
        Point2D operator-(Point2D &p); // 重載-運算子
    
    private:
        int X;
        int Y;
};
