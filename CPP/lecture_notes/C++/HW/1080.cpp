#include <iostream>

struct Pokemon{
    char Name[100];
    int Lv;
    int Hp;
};

int main(){

    int n, m;
    std::cin >> n;

    Pokemon *arr;

    arr = new Pokemon [n];

    for (size_t i = 0; i < n; i++){
        std::cin >> arr[i].Name;
        std::cin >> arr[i].Lv;
        std::cin >> arr[i].Hp;
    }
    std::cin >> m;

    Pokemon tmp;
    if(m == 1){
        for(size_t j = n; j > 1; j--){
            for(size_t i = 0; i < j - 1; i++){
                if(arr[i].Name[0] > arr[i+1].Name[0]){
                    tmp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = tmp;
                }else if(arr[i].Name[0] == arr[i+1].Name[0]){
                    if(arr[i].Name[1] > arr[i+1].Name[1]){
                        tmp = arr[i];
                        arr[i] = arr[i+1];
                        arr[i+1] = tmp;
                    }
                }
            }
        }
    }else if(m == 2){
        for(size_t j = n; j > 1; j--){
            for(size_t i = 0; i < j - 1; i++){
                if(arr[i].Lv > arr[i+1].Lv){
                    tmp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = tmp;
                }
            }
        }
    }else if(m == 3){
        for(size_t j = n; j > 1; j--){
            for(size_t i = 0; i < j - 1; i++){
                if(arr[i].Hp > arr[i+1].Hp){
                    tmp = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = tmp;
                }
            }
        }
    }

    for (size_t i = 0; i < n; i++){
        std::cout << "Name: " << arr[i].Name << std::endl;
        std::cout << "Lv: " << arr[i].Lv << std::endl;
        std::cout << "HP: " << arr[i].Hp << std::endl;
        std::cout << std::endl;
    }
}