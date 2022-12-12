# include "10_2_1.h"

class Point2D{
    public:
        Point2D(){
            X = 0;
            Y = 0;
        }
        Point2D(int x, int y){
            X = x;
            Y = y;
        }

        int getX(){
            return X;
        }
        int getY(){
            return Y;
        }

        void setX(int x){
            X = x;
        }
        void setY(int y){
            Y = y;
        }
    
    private:
        int X;
        int Y;
};
