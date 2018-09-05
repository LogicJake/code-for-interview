#include <iostream>
using namespace std;

int main()
{
    int money;
    cin >> money;
    int fiveNum = 0;
    int threeNum = 0;

    fiveNum = money / 50;
    money = money % 50;

    threeNum = money / 30;
    money = money % 30;

    cout << fiveNum * 7 + threeNum * 4 + money / 10;
    return 0;
}
