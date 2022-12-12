#include <iostream>
#include <string>

class Pokemon{
    public:
        Pokemon();
        Pokemon(std::string name, int lv, int hpmax);
        ~Pokemon();
        int Attack(Pokemon &op);
        void Defence();
        void Cure();
        void setData(std::string name, int lv, int hp);
        void ShowInfo();

    private:
        std::string Name;
        int Lv;
        int HpMax;
        int HpCurrent;
};

Pokemon::Pokemon(){
    Name = "none";
    Lv = 0;
    HpMax = 0;
    HpCurrent = 0;
}

Pokemon::Pokemon(std::string name, int lv, int hpmax){
    Name = name;
    Lv = lv;
    HpMax = hpmax;
    HpCurrent = hpmax;
}

Pokemon::~Pokemon(){

}

void Pokemon::setData(std::string name, int lv, int hp){
    Name = name;
    Lv = lv;
    if(hp >=0 ){
        HpCurrent = hp;
    }else{
        HpCurrent = 0;
    }
}

void Pokemon::ShowInfo(){
    std::cout << "Name: " << Name << std::endl;
    std::cout << "Lv: " << Lv << std::endl;
    std::cout << "HP: " << HpCurrent << "/" << HpMax << std::endl;
}

int Pokemon::Attack(Pokemon &op){
    if(op.HpCurrent > 0){
        std::cout << Name << " Attack " << op.Name << " " << Lv << " Points." << std::endl;

        if(op.HpCurrent - Lv <= 0){
            std::cout << op.Name << " Seriously Injured." << std::endl;
            std::cout << Name << " Win, " << op.Name << " Lose." << std::endl;
            std::cout << op.Name << " is unable to attack." << std::endl;
            op.setData(op.Name, op.Lv, op.HpCurrent - Lv);
            
            return 1;
        }else{
            op.setData(op.Name, op.Lv, op.HpCurrent - Lv);
            
            return 0;
        }
    }
    return 1;
}

void Pokemon::Cure(){
    HpCurrent = HpMax;
}

void Pokemon::Defence(){
    std::cout << std::endl;
}

int main(){

    int n;
    std::cin >> n;
    Pokemon *arr, *backup_arr;
    arr = new Pokemon [n];
    backup_arr = new Pokemon [n];

    for(size_t i = 0; i < n; i++){
        std::string input_name;
        int input_lv;
        int input_hp;

        std::cin >> input_name;
        std::cin >> input_lv;
        std::cin >> input_hp;

        Pokemon tmp(input_name, input_lv, input_hp);
        arr[i] = tmp;
        backup_arr[i] = tmp;
    }

    for(size_t i = 0; i < n; i++){

        Pokemon Mewtwo("Mewtwo", 30, 300);

        std::cout << '#' << i + 1 << std::endl;

        int flag;
        while(true){
            flag = arr[i].Attack(Mewtwo);
            if(flag){
                Mewtwo.ShowInfo();
                arr[i].ShowInfo();
                break;
            }
            flag = Mewtwo.Attack(arr[i]);
            if(flag){
                Mewtwo.ShowInfo();
                arr[i].ShowInfo();
                break;
            }
        }

        std::cout << std::endl;
    }

    return 0;
}