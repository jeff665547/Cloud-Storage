class Point2D{
    public:
        Point2D();
        Point2D(int x, int y);

        void setX(int x);
        void setY(int y);
        int getX();
        int getY();
        Point2D operator+(int n);
        Point2D operator-(Point2D &p);
        Point2D operator*(Point2D &p);

    private:
        int X;
        int Y;
};