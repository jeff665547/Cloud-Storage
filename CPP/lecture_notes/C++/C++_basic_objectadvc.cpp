// C++ 類別的朋友關係、重載運算子、繼承
/* 類別: 朋友關係friend */
// *在定義類別成員時，
//  私有成員只能被同一個類別定義的成員存取，
//  不可以直接由外界進行存取。
// *然而有些時候，
//  您希望提供私有成員給某些外部函式或類別來存取，
//  這時您可以設定類別的「好友」，
//  這些好友才可以直接存取私有成員。
// *使用friend通常是基於效率的考量，
//  以直接存取私有成員而不透過函式呼叫的方式，
//  來省去函式呼叫的負擔。
// *思考:由建立出兩個正方型物件，
//  並算出其面積之範例，
//  你需要提供一個"函式"讓使用者可以比較兩正方型之大小，
//  該如何達到此功能？
// *思考：由建立出兩個正方型物件，
//  並算出其面積之範例，
//  你需要提供一個"尺類別"讓使用者可以比較兩正方型之大小，
//  該如何達到此功能？
#include <iostream>

// 外部函式存取
class Square{
    
    public:
        Square(int n){
            len = n;
        }
        int getLen(){
            return len;
        }
        int area(){
            return len*len;
        }

        // 使用friend關鍵字來設定類別的好友函式，
        // 該好友可以直接存取該類別的私有成員。
        friend int compare(Square &s1, Square &s2);

    private:
        int len;
};

// 外部函式: 比較兩正方型之大小
int compare(Square &s1, Square &s2){
    
    // 可直接取得私有成員
    if(s1.len == s2.len){
        return 0;
    }else if(s1.len > s2.len){
        return 1;
    }else{
        return -1;
    }

    return 0;
}

// 外部類別存取
class Square2{
    public:
        Square2(int n){
            len = n;
        }
        int getLen(){
            return len;
        }
        int area(){
            return len*len;
        }

        // 使用friend關鍵字來設定一類別為另一類別的好友，
        friend class Ruler;

    private:
        int len;
};

// 外部類別: Ruler
class Ruler{
    public:
        Ruler(int n){
            len = n;
        }
        void compareSquare(Square2 &s1, Square2 &s2){
            // 可直接存取私有成員
            if((len < s1.len) || (len < s2.len)){
                std::cout << "Ruler is too short. It cannot be measured." << std::endl;
            }else{
                if(s1.len > s2.len){
                    std::cout << "s1 is larger." << std::endl;
                }else if(s1.len == s2.len){
                    std::cout << "s1 is the same as s2." << std::endl;
                }else{
                    std::cout << "s2 is larger." << std::endl;
                }
            }
        }
    
    private:
        int len;
};


/* 重載運算子 */
// *在C++中，預設除了基本資料型態可以使用運算子進行運算，
//  例如int、double、char等，如果您要將兩個物件相加，
//  預設上是不可行的。
// *然而很多情況下，您會想要將兩個物件的某些屬性值相加，
//  並傳回運算後的結果。
// *例如座標相加，如果您定義了Point2D類別，
//  當中有x與y兩個屬性成員，
//  您會想要透過+或-運算子的動作得到座標相加或相減的動作，
//  在C++中，這可以透過重載運算子來達到目的。
// *運算子的重載其實是函式重載的一個延伸應用，
//  您指定要重載哪一個運算子，
//  並在類別中定義運算子如何動作。
// 
// 用法:
// 運算子重載的語法宣告如下:
// 傳回值 類別名稱::operator#(參數列){
//    實作重載內容
//  }
// 其中#中需指明您要重載的運算子，
// 例如重載一個+運算子，#處就替換為+運算子。
// 
// 以下範例實作一個Point2D類別, 
// 將類似定義描述在Point2D.h, 
// 類別的方法描述在Point2D.cpp, 
// 主程式描述在main.cpp
#include "Point2D.h"

/* 繼承 Inheritance */
/* 繼承的基礎 */
// 繼承(Inheritance)是物件導向程式設計的一種進階觀念，
// 繼承就是物件的再利用，當定義好一個類別後，
// 其他類別可以繼承這個類別的成員資料和函數。
// 
// 語法: 
// class 子類別名稱: 繼承權限 父類別名稱{
//        
// }
// 在繼承的關係中
// 被繼承的類別:
//     「父類別」（Parent class）或「基礎類別」（Base class）
// 繼承父類別的類別:
//     「子類別」（Child class）或「衍生類別」（Derived class）
// 
// e.g. Parent class: car class, Child class: racingcar class
// 
// 類別繼承也是在模擬真實世界，
// e.g.: 學生和老師都是人，
// 我們可以先定義Person類別來模擬人類，
// 然後擴充Person類別建立Student類別來模擬學生，
// Teacher類別來模擬老師。

class Person{  // 父類別
    public:
        void inputPerson(){

            std::cout
            << "\ngood: " << std::cin.good()
            << "\nbad:  " << std::cin.bad()
            << "\neof:  " << std::cin.eof()
            << "\nfail: " << std::cin.fail()
            << std::endl;

            char str[128];
            std::cout << std::endl;
            std::cout << "Inheritance" << std::endl;
            std::cout << "<Enter Personal information>" << std::endl;
            std::cout << "Name: ";
            
            
            // fflush(stdin);
            // std::cin.getline(str, 128);
            // std::getline(cin str);
            std::cin >> str;
            Name = str;
            
            // std::cout
            // << "\ngood: " << std::cin.good()
            // << "\nbad:  " << std::cin.bad()
            // << "\neof:  " << std::cin.eof()
            // << "\nfail: " << std::cin.fail()
            // << std::endl;
            std::cout << "Phone: ";
            std::cin >> Phone;
            std::cout << "Email: ";
            std::cin >> Email;

        }

        void outputPerson(){
            
            std::cout << "<Personal Information>" << std::endl;
            std::cout << "Name: " << Name << std::endl;
            std::cout << "Phone: " << Phone << std::endl;
            std::cout << "Email: " << Email << std::endl;
            
        }
    
    private:
        std::string Name;
        std::string Phone;
        std::string Email;
};

class Student: public Person{ // 繼承, 子類別 Student

    public: 
        void inputStudent(){
            std::cout << "<Enter Student Information>" << std::endl;
            std::cout << "Student ID: ";
            std::cin >> StudentID;
            std::cout << "Department: ";
            std::cin >> Department;
        }
        void outputStudent(){
            std::cout << "Student Information" << std::endl;
            std::cout << "Student ID: " << StudentID << std::endl;
            std::cout << "Department: " << Department << std::endl;
        }
    
    private:
        std::string StudentID;
        std::string Department;
};

class Teacher: public Person{// 繼承, 子類別 Teacher
    public:
        void inputTeacher(){
            std::cout << "<Enter Teacher Information>" << std::endl;
            std::cout << "Title: ";
            std::cin >> Title;
            std::cout << "Department: " ;
            std::cin >> Department;
        }
        void outputTeacher(){
            std::cout << "Teacher information" << std::endl;
            std::cout << "Title: " << Title << std::endl;
            std::cout << "Department: " << Department << std::endl;
        }
    private:
        std::string Title;
        std::string Department;
};

/* 子類別的建構與解構式 */
// *您可以宣告這些成員為「受保護的成員」(protected member)，
//  保護的意思表示存取它有條件限制以保護該成員。
// *當您將類別成員宣告為受保護的成員之後，
//  繼承它的類別就可以直接使用這些成員，
//  但這些成員仍然受到類別的保護，不可被物件直接呼叫使用。
// -建構式與解構式呼叫順序
// *當建立子類別的物件呼叫子類別的建構式時，
//  它會先初始化父類別的成員，也就是呼叫父類別的建構式。
//  如果子類別沒有建構式，在建立物件時，
//  預設建構式就會呼叫父類別的預設建構式。
// *在呼叫子類別的建構式前，會先呼叫父類別的建構式，
//  而解構式剛好與建構式是相反順序，
//  也就是子類別的解構式是在父類別的解構式之前呼叫。
// -子類別傳遞參數給父類別
// *當父類別擁有重載建構式時，在子類別可以傳遞參數給父類別的建構式。
// *建構式的 : 運算子後是傳遞給父類別建構式的參數，如果父類別不只一個，
//  請使用, 號分隔。
// *其中傳遞給父類別參數的值，就是傳入子類別建構式的參數值。
// *在繼承時使用 : 運算子，並指定其繼承方式，在繼承的權限關係上，
//  公開繼承是最常見的。
//
//  為了示範方便，本程式碼把所有例子集合起來，照理來說底下應該要獨自成一個檔案，
//  ，並藉由 Point3D.h 連起來。
// e.g. 公開繼承
// #include "Point2D.h"

class Point3D : public Point2D{
    public: 
        Point3D(){
            Z = 0;
        }
        Point3D(int x, int y, int z) : Point2D(x, y){
            Z = z;
        }
        int getZ(){
            return Z;
        }
        void setZ(int z){
            Z = z;
        }
    private:
        int Z;
};

/* 3種繼承方式 */
// 公開繼承 語法:
// class B : public A{ 
//  // 實作
// };
// *公開繼承時使用public來繼承基底類別，
//  繼承下來的成員在衍生類別中的權限變為如下
//  
//  基底類別 => 衍伸類別
//  private => 不繼承
//  protected => protected
//  public => public
//
// 
// 保護繼承 語法:
// class B : protected A{ 
//  // 實作
// };
// *保護繼承時使用protected來繼承基底類別，
//  繼承下來的成員在衍生類別中的權限變為如下
//  
//  基底類別 => 衍伸類別
//  private => 不繼承
//  protected => protected
//  public => protected
//
//
// 私有繼承 語法:
// class B : private A{ 
//  // 實作
// };
// *私有繼承時使用private來繼承基底類別，
//  繼承下來的成員在衍生類別中的權限變為如下
//  
//  基底類別 => 衍伸類別
//  private => 不繼承
//  protected => private
//  public => private

int main(){

    Square s1(10);
    Square s2(20);

    std::cout << "s1:len = " << s1.getLen() << ", area = " 
    << s1.area() << std::endl;
    std::cout << "s2:len = " << s2.getLen() << ", area = " 
    << s2.area() << std::endl;

    // 主程式可呼叫 compare(s1, s2) 比較兩方形大小
    switch(compare(s1, s2)){

        case 1:
            std::cout << "s1 is larger." << std::endl;
        case 0:
            std::cout << "s1 is the same as s2." << std::endl;
        case -1:
            std::cout << "s2 is larger." << std::endl;
            break;

    }

    // 主程式可建立 Ruler 物件比較兩方型大小
    Square2 s3(10);
    Square2 s4(20);
    Ruler r(30);

    std::cout << "s3:len = " << s3.getLen() << ", area = " 
    << s3.area() << std::endl;
    std::cout << "s4:len = " << s4.getLen() << ", area = "
    << s4.area() << std::endl;

    r.compareSquare(s3, s4);


    /* 重載運算子 */
    Point2D p1(5, 5);
    Point2D p2(10, 10);
    Point2D p3;

    p3 = p1 + p2;
    std::cout << "p3(x, y) = (" << p3.getX() << "," << p3.getY() << ")" << std::endl;

    p3 = p2 - p1;
    std::cout << "p3(x, y) = (" << p3.getX() << "," << p3.getY() << ")" << std::endl;
    
    /* 繼承的基礎 */
    std::cout << "This is a student." << std::endl;
    Student stu1;
    stu1.inputPerson();
    stu1.inputStudent();
    std::cout << std::endl;
    stu1.outputPerson();
    stu1.outputStudent();

    std::cout << "This is a teacher." << std::endl;
    Teacher teach1;
    teach1.inputPerson();
    teach1.inputTeacher();
    std::cout << std::endl;
    teach1.outputPerson();
    teach1.outputTeacher();

    std::cout << std::endl;
    /* 子類別的建構與解構式 */
    Point3D p11(1, 3, 4);
    Point3D p22;
    
    std::cout << "p11: (" << p11.getX() << "," << p11.getY() << "," << p11.getZ() << ")" << std::endl;

    p22.setX(5);
    p22.setY(7);
    p22.setZ(8);

    std::cout << "p22: (" << p22.getX() << "," << p22.getY() << "," << p22.getZ() << ")" << std::endl;

    return 0;
}