#include "C++_basic_objectadvc_inheritance.h"

class Point3D : public Point2D{
    public:
        Point3D() {
            _z = 0;
        }
        // 建構函式，同時指定呼叫父類別建構函式
        Point3D(int x, int y, int z) : Point2D(x, y), _z(z) {
        }
        int z(){
            return _z;
        }
        void z(int z){
            _z = z;
        }

    private:
        int _z;
};

class Cubic : public Rectangle{
    public:
        Cubic(){
            _z = 0;
            _length = 0;
        }

        Cubic(int x, int y, int z, int length, int width, int height)
        : Rectangle(x, y, width, height) , _z(z), _length(length){
        }

        int length() {
            return _length;
        }

        // 受保護的(protected)成員差別只有差在這，
        // 函式在調用時，可以直接打父類別的變數名稱來取用變數成員的資料。
        int volumn() {
            return _length*_width*_height;
        }

    protected:
        int _z;
        int _length;
};

