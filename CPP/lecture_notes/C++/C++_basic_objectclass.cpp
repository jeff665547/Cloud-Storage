// C++ 物件導向
// 以物件為基礎的程式設計，將程式中互動的單元視為一個個的物件。
/* 封裝（Encapsulation） */
// *封裝物件資訊是第一步，您要瞭解如何使用類別定義物件的屬性、方法(行為)
// *類別是建構物件時所依賴的規格書。
//  例如設計一個物件: 人
//  屬性: 姓名, 身高, 體重
//  行為: 輸入資料, 輸出資料
// *類別class是C++中用來封裝資料的關鍵字
// *當使用類別來定義一個物件時，
//  需要考慮這個物件可能擁有的「屬性」與「方法」成員。
// *屬性是物件的靜態描述。
// *方法是可施加於物件上的動態操作。
// *使用類別定義出這個物件的規格書，
//  之後就可依這個規格書製作出一個個的物件實例，
//  並在製作過程中設定個別物件的專屬特性資料。
// *Tips:
//  屬性->宣告要存放的資料(每個物件有自己的屬性)
//  方法->寫要執行的函式(通常用來操作物件的屬性)
//
// 用法:
// class 類別名稱{
//
//     public:
//         類別名稱();        // 建構式，用來做物件的初始化
//         ~類別名稱();       // 解構式，用來做物件的善後工作
//         公開的方法或屬性;
//     protected:            // 只有在同一繼承架構下才可以使用的資料
//         受保護的方法或屬性;
//     private:              // 只有在此類別中可以使用的資料
//         私有的方法或屬性;
// 
// };
//
/* 資料的權限 */
// *public這個關鍵字，
//  它表示以下所定義的成員可以使用物件名稱直接被呼叫，
//  稱之為「公開成員」。
// *private關鍵字下的則是「私有成員」，
//  不可以透過物件名稱直接呼叫。
// *在類別封裝時，有一個基本原則是: 資訊的最小化公開。
//  如果屬性可以不公開就不公開，如果要取得或設定物件的某些屬性，
//  也是儘量透過方法成員來進行。
// *private將成員設定成無法從類別外任意存取，這種成員稱之為private成員。
// 
// *思考: 由上面輸入兩個人資料(姓名, 身高, 體重)並印出的範例, 
//  你希望Person產生的物件只能用input與output函式來輸入輸出資料，
//  該如何達到此功能？
//
// 
//  使用private成員。
//
/* 物件的產生與使用 */
//
// 使用類別宣告物件
// 語法:
//  類別名稱 物件名稱; 
//  e.g. Car car1, car2;
//  類別名稱 物件名稱( 參數1, 參數2 ,參數3, ..., 參數n);
//  e.g. Car car1(123, 20.5);
// 物件可以透過.來使用或存取該方法或屬性
// (類似C語言的struct)
// e.g. car1.num = 10;     存取屬性
// e.g. car1.show();       使用方法
// 若為物件指標，可透過->來使用或存取該方法或屬性
// (在一般情況下，用點運算子 “ . ” 來訪問物件成員，
// 當用指向物件的指標來訪問物件成員時，就要用 “ -> ” 操作符。)
// e.g. ptr -> show();
// e.g. 
#include <iostream>
#include <string>

class Person{
    public:
        void input(){
            std::cin >> name;
            std::cin >> height;
            std::cin >> weight;
        }

        /*在這邊定義等價於下方先宣告並且在外面補定義(類別的方法之描述)*/
        void output();
        // void output(){
        //     std::cout << "Name: " << name << std::endl;
        //     std::cout << "Height: " << height << " cm" << std::endl;
        //     std::cout << "Weight: " << weight << " kg" << std::endl;
        // }

        std::string name;
        int height;
        int weight;
};

/* 類別的方法之描述 */
// 實作一個類別方法的內容(類似寫一個函式)
// 除了寫在類別定義中, 也可拿到類別定義以外的地方描述
// 
// 用法: 
// 資料型態 類別名稱::方法名稱( 參數1, 參數2, ... ,參數n ){
//    程式碼
// }
void Person::output(){
    std::cout << "Name: " << name << std::endl;
    std::cout << "Height: " << height << " cm" << std::endl;
    std::cout << "Weight: " << weight << " kg" << std::endl;
}


/* 資料的權限 */
class Person2{
    public:
        void input(){
            std::cin >> name;
            std::cin >> height;
            std::cin >> weight;
        }

        void output(){
            std::cout << "Name: " << name << std::endl;
            std::cout << "Height: " << height << " cm" << std::endl;
            std::cout << "Weight: " << weight << " kg" << std::endl;
        }

    private:
        std::string name;
        int height;
        int weight;

};

/* 建構式與解構式 */
// *在定義類別時，您可以使用建構函式(Constructor)來進行物件的初始化
// *而在物件釋放資源之前，您也可以使用解構函式(Destructor)
//  來進行一些善後的工作
// *思考: 由上一個輸入兩個人資料(姓名, 身高, 體重)
//  並印出的範例，你希望一開始姓名為No name, 身高與體重為0，
//  該如何達到此功能？
// 
//
//  => 建構式 (初始化)
// 建構式
class Person3{
    public:
        Person3(){ // 建構式，名稱與class相同
            name = "No name";
            height = 0;
            weight = 0;
        }
        void input(){
            std::cin >> name;
            std::cin >> height;
            std::cin >> weight;
        }

        void output(){
            std::cout << "Name: " << name << std::endl;
            std::cout << "Height: " << height << " cm" << std::endl;
            std::cout << "Weight: " << weight << " kg" << std::endl;
        }

    private:
        std::string name;
        int height;
        int weight;

};

// 重載建構式
class Person4{
    public:
        Person4(){ // 建構式，名稱與class相同
            name = "No name";
            height = 0;
            weight = 0;
        }
        Person4(std::string n, int h, int w){  // 重載建構式。
            name = n;
            height = h;
            weight = w;
        }
        void input(){
            std::cin >> name;
            std::cin >> height;
            std::cin >> weight;
        }

        void output(){
            std::cout << "Name: " << name << std::endl;
            std::cout << "Height: " << height << " cm" << std::endl;
            std::cout << "Weight: " << weight << " kg" << std::endl;
        }

    private:
        std::string name;
        int height;
        int weight;
};

// 解構式
class Person5{
    public:
        Person5(){ // 建構式，名稱與class相同。
            name = "No name";
            height = 0;
            weight = 0;
        }
        ~Person5(){  // 解構式。
            std::cout << "ByeBye!" << std::endl;
        }
        void input(){
            std::cin >> name;
            std::cin >> height;
            std::cin >> weight;
        }

        void output(){
            std::cout << "Name: " << name << std::endl;
            std::cout << "Height: " << height << " cm" << std::endl;
            std::cout << "Weight: " << weight << " kg" << std::endl;
        }

    private:
        std::string name;
        int height;
        int weight;
};


int main(){

    std::cout << "pointer 1, pointer 2" << std::endl;
    Person p1;
    Person p2;

    p1.input();
    p1.output();
    p2.input();
    p2.output();

    std::cout << "pointer 3, pointer 4" << std::endl;
    // 資料的權限
    Person2 p3;
    Person2 p4;

    p3.input();
    // p1.height = 0;      
    // 這行不能執行!
    p3.output();
    p4.input();
    p4.output();

    std::cout << "pointer 5, pointer 6" << std::endl;
    // 建構式與解構式
    Person3 p5;
    Person3 p6;

    // p5.input();   // p5沒輸入
    p5.output();     // p5印出No name
    p6.input();
    p6.output();

    std::cout << "pointer 7, pointer 8" << std::endl;
    // 重載建構式
    Person4 p7;
    Person4 p8("Andy", 180, 80);  // 呼叫重載建構式

    p7.output();
    p8.output();

    std::cout << "pointer 9" << std::endl;
    // 解構式
    Person5 p9;

    p9.output();  
    std::cout << "======= End =======" << std::endl;

    return 0; // p9釋放前執行解構式(印出ByeBye)
}

// 如何設計類別?
//
// 思考(以功能角度)
// 每個物件需要什麼資料?
// 每個物件需要什麼方法來操作資料?
//
// 進階思考(以使用者角度)
// 如何讓使用類別的人方便簡單使用
// 如何避免使用類別的人因資料操作不當而產生錯誤

