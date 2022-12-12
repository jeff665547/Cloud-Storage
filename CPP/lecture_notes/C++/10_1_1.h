class Point2D{

    public:
        Point2D();
        Point2D(int x, int y);
        int getX();
        int getY();
        Point2D operator+(Point2D &p); // 重載+運算子
        Point2D operator-(Point2D &p); // 重載-運算子
        Point2D operator*(Point2D &p); // 重載*運算子
        Point2D operator+(int m); // 重載+運算子

    private:
        int X;
        int Y;
};