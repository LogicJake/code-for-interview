#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

void Qsort(int a[], int low, int high)
{
    if (low >= high)
    {
        return;
    }
    int first = low;
    int last = high;
    int key = a[first]; /*用字表的第一个记录作为枢轴*/

    while (first < last)
    {
        while (first < last && a[last] >= key)
        {
            --last;
        }

        a[first] = a[last]; /*将比第一个小的移到低端*/

        while (first < last && a[first] <= key)
        {
            ++first;
        }

        a[last] = a[first];
        /*将比第一个大的移到高端*/
    }
    a[first] = key; /*枢轴记录到位*/
    Qsort(a, low, first - 1);
    Qsort(a, first + 1, high);
}

int main()
{

    int n;
    cin >> n;
    int m[n];

    for (int i = 0; i < n; i++)
    {
        cin >> m[i];
    }

    Qsort(m, 0, n-1);

    int min = 9999999;
    for (int i = 0; i < n - 1; i++)
    {
        if (abs(m[i + 1] - m[i]) < min)
            min = abs(m[i + 1] - m[i]);
    }
    cout << min;
}