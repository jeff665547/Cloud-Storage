# include <iostream>
# define PEOPLE 2
// Struct and File IO
// 使用時機: 需要更方便管理以及更有效率的方法來儲存資料
// 通常一個簡單之變數或陣列不足以用來儲存複雜之記錄。
// C語言中有結構體(Structure)的架構，能讓一個變數擁有許多不同的形態
// 其允許使用者宣告資料實體，將不同形式之元素儲存在一起。
// 結構是一種由程式設計師自訂之資料型態。
// 用法:
// struct 結構名稱標籤{
//   資料型態 資料變數成員1;
//   資料型態 資料變數成員2;
//   ‧‧‧‧‧‧‧‧
//   };
// 
// 結構的標籤名稱(tag)
//     可看成是一個程式設計師自訂的新型態。
// 結構的成員(member)
//     其資料型態可以使用int, float 及char。
//     也可用陣列與指標或是另外一個結構。
// 
// 範例情境: 用程式存一群人的姓名、身高、體重
// 建立一個名為Person的資料型態
struct Person{
    char name[80];
    int height;
    int weight;
};
// 建立的Person資料型態是會以連續的方式將資料儲存在記憶體中
//
// 宣告一個結構實體之語法
// struct 結構名稱標籤 結構實體名稱;
// struct結構名稱標籤結構實體名稱= {初始值1,初始值2, ...}
// 
// 結構中成員的使用之語法
//   結構實體之成員的直接存取
//     結構實體.成員名稱
//   結構指標之成員的直接存取
//     結構指標->成員名稱 or (*結構指標).成員名稱


/* typedef */
// typedef可以把所有C語言中的型態改用程式設計師自己取的名字來取代
// e.g. 
typedef unsigned char UINT8; // 將unsigned char型態用UINT8來命名
typedef unsigned short UINT16; // 將unsigned short型態用UINT16來命名
typedef unsigned long UINT32; // 將unsigned long型態用UINT32來命名
// 用“ typedef ”來自訂一個型態，常用在結構上
// e.g.
struct _Person{
    char name[80];
    int height;
    int weight;
};
typedef struct _Person Person2; // 利用Person2來取代_Person。

int main(){

    struct Person p1; // 結構實體之成員的直接存取
    struct Person p2;
    struct Person *p3; // 結構指標之成員的直接存取
    p3 = &p2;

    // 結構實體之成員的直接存取
    std::cin >> p1.name >> p1.weight >> p1.height;
    std::cout << "Name:\t" << p1.name << std::endl
    << "Height:\t" << p1.height << std::endl
    << "Weight:\t" << p1.weight << std::endl;

    // 結構指標之成員的直接存取
    std::cin >> (*p3).name >> (*p3).weight 
    >> p3 -> height;
    std::cout << "Name:\t" << p2.name << std::endl
    << "Height:\t" << p2.height << std::endl
    << "Weight:\t" << p2.weight << std::endl;

    // 結構陣列
    struct Person P[PEOPLE]; // 也可以直接在陣列中打2
    int i;
    for(i = 0; i < PEOPLE; i++){
        std::cin >> P[i].name;
        std::cin >> P[i].height;
        std::cin >> P[i].weight;
        std::cout << "Name:\t" << P[i].name << std::endl
        << "Height:\t" << P[i].height << std::endl
        << "Weight:\t" << P[i].weight << std::endl;
    }

    /* typedef */
    UINT8 a = 1;
    UINT16 b = 2;
    UINT32 c = 3;

    // 用“ typedef ”來自訂一個型態，常用在結構上
    Person2 p4; 
    std::cin >> p4.name >> p4.weight >> p4.height;
    std::cout << "Name:\t" << p4.name << std::endl
    << "Height:\t" << p4.height << std::endl
    << "Weight:\t" << p4.weight << std::endl;


    /* 檔案處理 in C: */
    // e.g. 從input.txt讀一字串到str，再把字串從str寫到output.txt
    FILE *in, *out;     // in, out為檔案指標
    char str[80];

    in = fopen("input.txt", "r");  // 開啟input.txt
    fscanf(in, "%s", str);         // 讀檔
    fclose(in);                    // 關閉input.txt

    out = fopen("output.txt", "w");  // 開啟output.txt
    fprintf(out, "%s", str);         // 寫檔
    fclose(out);                     // 關閉output.txt

    // fopen(): 開檔
    // 檔案使用前需要先開啟，開檔結果需要檔案指標FILE紀錄相關資訊，之後即可使用該指標讀寫檔
    // 用法:
    // 檔案指標 = fopen("檔名", "模式");
    //    檔名：檔案指標，指的是欲開啟的檔案名稱。
    //    模式：檔案使用模式，指的是檔案被開啟之後，它的使用方式。
    // 
    // 模式種類:
    // "r" => 開啟一個文字檔(text)，供程式讀取。
    // "w" => 開啟一個文字檔(text)，
    //        供程式將資料寫入此檔案內。
    //        如果磁碟內不包含這個檔案，
    //        則系統會自行建立這個檔案。
    //        如果磁碟內包含這個檔案，
    //        則此檔案內容會被覆蓋而消失。
    //
    // "rb" => 開啟一個二元檔(binary)，供程式讀取。
    // "wb" => 開啟一個二元檔，
    //         供程式將資料寫入此檔案內。
    //         如果磁碟內不包含這個檔案，
    //         則系統會自行建立這個檔案。
    //         如果磁碟內包含這個檔案，
    //         此檔案內容會被蓋過而消失。

    // 判斷檔案開啟是否正確
    // 使用fopen若開檔失敗，會回傳一個NULL結果
    // 常用來判斷檔案是否存在
    in = fopen("input.txt", "r");  // 開啟input.txt
    if(in == NULL){
        printf("failed to open file!\n");
    }

    // fclose(): 關檔
    // 用於關閉檔案，如果fclose()執行失敗，它的傳回值是非零值。
    // 用法:
    // fclose(檔案指標);
    // 在C語言中關閉檔案主要有三個目的:
    // 1. 檔案在關閉前會將檔案緩衝區資料寫入磁碟檔案內，
    //    否則檔案緩衝區資料會遺失。
    //    (檔案在關閉前會將檔案緩衝區資料寫入磁碟檔案內，否則檔案緩衝區資料會遺失。)
    // 2. 檔案需要換個模式開啟時(例:先寫後讀)。
    // 3. 解除已開啟檔案的鎖定狀態。
    // 通常，在呼叫fclose之前，檔案的內容不會真正的被寫到磁碟機上


    // fprintf(): 寫檔
    // 將資料，以格式化方式寫入某檔案內，屬於存檔步驟。
    // 用法:
    // fprintf(檔案指標,"格式化輸出內容", 參數1, 參數2, ... 參數n);
    // 此格式化輸出內容與參數的使用，格式和printf()使用格式相同。
    // 資料從後方的參數1, 參數2, 參數3, ...傳到前面的檔案指標。
    // e.g. 將陣列個數與內容寫入指定名稱之檔案
    FILE *file;
    int aa[5] = {10, 20, 30, 40, 50};
    char str2[80];
    int t, n = 5;
    
    // 開檔
    printf("input file name: ");
    scanf("%s", &str2);
    file = fopen(str2, "w");
    
    // 寫檔
    fprintf(file, "%d\n", n);
    for(t = 0; t < n; t++){
        fprintf(file, "%d ", aa[t]);
    }
    
    // 關檔
    fclose(file);

    // fscanf(): 讀檔
    // 從某個檔案讀取資料，並且接著對資料做後續動作。
    // 用法:
    // fscanf(檔案指標,"格式化輸入內容", &參數1, &參數2, ..., &參數n);
    // 此格式化輸入內容與參數的使用，格式和scanf( )使用格式相同。
    // 資料從檔案指標傳到後方的參數1, 參數2, 參數3, ...
    // e.g. 將指定名稱之檔案的陣列個數與內容讀出並印到螢幕上
    FILE *file2;
    int bb[100];
    char str3[80];
    int kk, nn;

    //開檔
    printf("input file name: ");
    scanf("%s", &str3);
    file2 = fopen(str3, "r");
    if(file2 == NULL){
        printf("open file fail!\n");
        return 0;
    }
    //讀檔
    fscanf(file2, "%d", &nn);
    for(kk = 0; kk < nn; kk++){
        fscanf(file2, "%d ", &bb[kk]);
    }
    //輸出
    printf("%d\n", nn);
    for(kk = 0; kk < nn; kk++){
        printf("%d ", bb[kk]);
    }
    printf("\n");
    //關檔
    fclose(file2);

    // 判斷檔案是否結束
    // 用法: feof(檔案指標);
    FILE *input;
    char str4[80];
    char ch;  
    scanf("%s", &str4);
    // 開檔
    input = fopen(str4,"r");
    if ( input == NULL ){
        printf("open input.txt fail!\n");
        return 0;
    }
    while(1){
        fscanf(input, "%c", &ch); 
        if( feof(input) )  // 檔案結束就跳出迴圈
            break;
        printf("%c", ch);
    }

    /* 檔案處理 in C++: */
    

    return 0;
}