// function template
#include <iostream>
using namespace std;

template <class T, int N>
void foo(void)
{
  std::cout << N << std::endl;
}

constexpr int goo(void) {
  int x = 1;
  for (int i = 0; i != 10; ++i)
    x += i;
  return x;
}

int main () {

  // foo<int,goo()>();
  std::cout << goo() << std::endl;


  return 0;
}