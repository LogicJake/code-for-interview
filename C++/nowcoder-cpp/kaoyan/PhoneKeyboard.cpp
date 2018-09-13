#include <iostream>
#include <math.h>
#include <map>
using namespace std;
int keyMap[26] = {
    1, 1, 1,    // a, b, c
    2, 2, 2,    // d, e, f
    3, 3, 3,    // g, h, i
    4, 4, 4,    // j, k, l
    5, 5, 5,    // m, n, o
    6, 6, 6, 6, // p, q, r, s
    7, 7, 7,    // t, u, v
    8, 8, 8, 8  // w, x, y, z
};

int keyTime[26] = {
    1, 2, 3,
    1, 2, 3,
    1, 2, 3,
    1, 2, 3,
    1, 2, 3,
    1, 2, 3, 4,
    1, 2, 3,
    1, 2, 3, 4};

bool inSameKey(char a, char b)
{
    int index1 = a - 'a';
    int index2 = b - 'a';
    return keyMap[index1] == keyMap[index2];
}

int getTime(char a)
{
    return keyTime[a - 'a'];
}
int main()
{
    string input;
    // while (cin >> input)
    {
        cin>>input;
        int timeTotal = 0;
        for (int i = 0; i < input.length(); i++)
        {
            timeTotal += getTime(input[i]);
            if (i != input.length() - 1)
            {
                if(inSameKey(input[i],input[i+1]))
                    timeTotal += 2;
            }
        }
        cout<<timeTotal;
    }
}