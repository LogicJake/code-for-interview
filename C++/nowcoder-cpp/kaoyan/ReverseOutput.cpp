#include <iostream>
using namespace std;

int main()
{
    string input;
    while (cin >> input)
    {
        for (int i = 3; i >= 0; i--)
        {
            cout << input[i];
        }
    }
}