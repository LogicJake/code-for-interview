#include <iostream>
using namespace std;

void deleteSame(int a[], int len)
{
    int pos = 0;
    while (pos != len)
    {
        int num = 0;
        int color = a[pos];
        int checkpos = pos;

        while (checkpos != len)
        {
            if (a[checkpos] == color)
            {
                num++;
                checkpos++;
            }
            else
                break;
        }

        //消除连续3个
        if (num >= 3)
        {
            for (int i = pos; i < pos + num; i++)
            {
                a[i] = 0;
            }

            //因为总会+1，所以num-1
            pos += num - 1;
        }
        pos++;
    }
}

int main()
{
    int n, m;
    cin >> n >> m;

    int a[n][m];
    int b[m][n];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
            b[j][i] = a[i][j];
        }
    }

    //按行消除
    for (int i = 0; i < n; i++)
    {
        deleteSame(a[i], m);
    }

    //按列消除
    for (int i = 0; i < m; i++)
    {
        deleteSame(b[i], n);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (a[i][j] == 0 || b[j][i] == 0)
            {
                cout << 0 << " ";
            }
            else
            {
                cout << a[i][j] << " ";
            }
        }
        cout << endl;
    }
}