// 重載運算子
// 此檔案放類別的方法描述(實作)
# include "Point2D.h"

Point2D::Point2D(){
    X = 0;
    Y = 0;
}
Point2D::Point2D(int x, int y){
    X = x;
    Y = y;
}

int Point2D::getX(){
    return X;
}
int Point2D::getY(){
    return Y;
}
void Point2D::setX(int x){
    X = x;
}
void Point2D::setY(int y){
    Y = y;
}

Point2D Point2D::operator+(Point2D &p){
    int x = X + p.X;
    int y = Y + p.Y;
    Point2D tmp(x, y);  // Initialize a Point2D class (Point2D::Point2D(int x, int y))
    return tmp;  // Return a class.
}
Point2D Point2D::operator-(Point2D &p){
    int x = X - p.X;
    int y = Y - p.Y;
    Point2D tmp(x, y);  // Initialize a Point2D class (Point2D::Point2D(int x, int y))
    return tmp;  // Return a class.
}
