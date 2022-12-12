#include <iostream>

class Shape{
    protected:
        int width, height;
    public:
        Shape( int a = 0, int b = 0){
            width = a;
            height = b;
        }
        /*virtual*/ int area(){
            std::cout << "Parent class area: " << std::endl;
            return 0;
        }
};

class Rectangle: public Shape{
    public:
        Rectangle(int a = 0, int b = 0): Shape(a, b) { }
        // Rectangle建構式的:運算子後是傳遞給父類別建構式(Shape)的參數，如果父類別不只一個，請使用,號分隔。
        // 在這之中傳遞給父類別(Shape)參數的值，就是傳入子類別建構式(Rectangle)的參數值。
        int area(){
            std::cout << "Rectangle class area: " << std::endl;
            return (width * height);
        }
};

class Triangle: public Shape{
    public:
        Triangle(int a = 0, int b = 0): Shape(a, b){ }
        // Triangle建構式的:運算子後是傳遞給父類別建構式(Shape)的參數，如果父類別不只一個，請使用,號分隔。
        // 在這之中傳遞給父類別(Shape)參數的值，就是傳入子類別建構式(Triangle)的參數值。
        int area(){
            std::cout << "Triangle class area: " << std::endl;
            return (width * height / 2 );
        }
};

// 上面的程式碼被編譯和執行時，它會產生下列結果:
// Parent class area:
// Parent class area:
// 導致錯誤輸出的原因是，呼叫函式 area() 被編譯器設定為基礎類別中的版本，
// 這就是所謂的靜態多型，或靜態連結-函式呼叫在程式執行前就準備好了。
// 有時候這也被稱為早繫結，因為 area() 函式在程式編譯期間就已經設定好了。

// 虛擬函式
// 虛擬函式是在基礎類別中使用關鍵字 virtual 宣告的函式。
// 在衍生類別中重新定義基類中定義的虛擬函式時，會告訴編譯器不要靜態連結到該函式。
// 我們想要的是在程式中任意點可以根據所呼叫的物件型別來選擇呼叫的函式，
// 這種操作被稱為動態連結，或後期繫結。
// 在父類別的方法中加入了關鍵字virtual則會產生以下結果:
// Rectangle class area:
// Triangle class area:

// 純虛擬函式
// 您可能想要在基類中定義虛擬函式，
// 以便在衍生類別中重新定義該函式更好地適用於物件，
// 但是您在基礎類別中又不能對虛擬函式給出有意義的實現，
// 這個時候就會用到純虛擬函式。
// e.g. virtual int area() = 0;
// 上面設為 = 0 是告訴編譯器，函式沒有主體，上面的虛擬函式是純虛擬函式。

// 哪些函式不能設定為虛擬函式
// 設定虛擬函式須注意：
// 1：只有類的成員函式才能說明為虛擬函式；
// 2：靜態成員函式不能是虛擬函式；
// 3：行內函數不能為虛擬函式；
// 4：建構函式不能是虛擬函式；
// 5：解構函式可以是虛擬函式，而且通常宣告為虛擬函式。

// 一個類別中如果含有純虛擬函式，則該類別為一「抽象類別」(Abstract class)，
// 該類別只能被繼承，而不能用來直接生成實例，
// 如果試圖使用一個抽象類別來生成實例，則會發生編譯錯誤。
// e.g.
class AbstractCircle {
    public: 
        void radius(double radius){
            _radius = radius;
        }
        double radius(){
            return _radius;
        }
        // 宣告虛擬函式
        virtual void render() = 0;

    protected:
        double _radius;
};

class HollowCircle : public AbstractCircle{
    public:
        void render() {
            std::cout << "Draw a radius "
            << _radius << " hollow circle."
            << std::endl;
        }
};

class ConcreteCircle : public AbstractCircle{
    public:
        void render(){
            std::cout << "Draw a radius " << _radius
            << " concrete circle" << std::endl;
        }
};

void render(AbstractCircle &circle){
    circle.render();
}

int main2(){

    ConcreteCircle concrete;
    concrete.radius(10.0);
    render(concrete);

    HollowCircle hollow;
    hollow.radius(20.0);
    render(hollow);

    return 0;
}

int main(){
    
    Shape *shape;  
    // 宣告一個指標指向Shape類及其子類別(衍生類)，
    // 此時只配一個記憶體位置紀錄另一個記憶體位置，
    // 但紀錄的這個記憶體位置並沒有實際的東西，
    // 需要等到後續的definition結果才會出來。
    Rectangle rec(10, 7);
    Triangle tri(10, 5);

    // 儲存矩形的地址
    shape = &rec;
    // 呼叫矩形的求面積函式 area
    shape -> area();

    // 儲存三角形的地址
    shape = &tri;
    // 呼叫三角形的求面積函式 area
    shape -> area();

    main2();

    return 0;
}