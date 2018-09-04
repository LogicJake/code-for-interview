#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int number[n];
    for (int i = 0; i < n; i++)
    {
        cin >> number[i];
    }

    for (int i = 0; i < n; i++)
    {
        int num = 0;

        int endIndex = sqrt(number[i]);

        if (endIndex * endIndex == number[i])
        {
            num++;
            endIndex--;
        }

        for (int j = 1; j <= endIndex; j++)
        {
            if (number[i] % j == 0)
                num += 2;
        }
        cout << num << endl;
    }
}