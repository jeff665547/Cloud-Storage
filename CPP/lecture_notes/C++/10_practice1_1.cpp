#include <iostream>
#include "10_practice1_1.h"

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

Point2D Point2D::operator+(int n){
    int x, y;
    x = X + n;
    y = Y + n;
    Point2D temp(x, y);
    return temp;
}

Point2D Point2D::operator-(Point2D &p){
    int x, y;
    x = X - p.X;
    y = Y - p.Y;
    Point2D temp(x, y);
    return temp;
}

Point2D Point2D::operator*(Point2D &p){
    int x, y;
    x = X*p.X;
    y = Y*p.Y;
    Point2D temp(x, y);
    return temp;
}