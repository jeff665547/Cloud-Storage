#include <iostream>
#include <string>

class Pokemon{
    public:

        Pokemon();
        Pokemon(std::string name, int lv, int hpmax, int hpcurrent);
        ~Pokemon();
        void ShowInfo();
        void Attack(std::string target);  // 攻擊
        void Defence(std::string atkp);  // 防禦
        void Cure();  // 治癒

    private:
        std::string Name;
        int Lv;
        int HpMax;
        int HpCurrent;
};