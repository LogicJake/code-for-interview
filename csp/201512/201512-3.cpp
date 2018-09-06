#include <iostream>
#include <vector>
using namespace std;

int m, n, q;
char **pic;

void draw()
{
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = 0; j < m; j++)
        {
            cout << pic[i][j];
        }
        cout << endl;
    }
}

void fill(int x, int y, char c)
{
    if (x >= m || x < 0 || y >= n || y < 0 || pic[y][x] == c || pic[y][x] == '-' || pic[y][x] == '|' || pic[y][x] == '+')
        return;
    pic[y][x] = c;

    fill(x, y + 1, c);
    fill(x, y - 1, c);
    fill(x + 1, y, c);
    fill(x - 1, y, c);
}

void drawLine(int x1, int y1, int x2, int y2)
{
    if (y1 == y2)
    {
        int start = x1 > x2 ? x2 : x1;
        int end = x1 > x2 ? x1 : x2;

        for (int i = start; i <= end; i++)
        {
            if (pic[y1][i] == '|' || pic[y1][i] == '+')
                pic[y1][i] = '+';
            else
                pic[y1][i] = '-';
        }
    }
    else
    {
        int start = y1 > y2 ? y2 : y1;
        int end = y1 > y2 ? y1 : y2;

        for (int i = start; i <= end; i++)
        {
            if (pic[i][x1] == '-' || pic[i][x1] == '+')
                pic[i][x1] = '+';
            else
                pic[i][x1] = '|';
        }
    }
}

int main()
{
    cin >> m >> n >> q;
    pic = new char *[n];
    for (int i = 0; i < n; i++)
    {
        pic[i] = new char[m];
        for (int j = 0; j < m; j++)
        {
            pic[i][j] = '.';
        }
    }
    for (int i = 0; i < q; i++)
    {
        int type;
        cin >> type;

        //填充操作
        if (type == 1)
        {
            int x, y;
            char c;
            cin >> x >> y >> c;

            fill(x, y, c);
        }
        //画线操作
        else if (type == 0)
        {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            drawLine(x1, y1, x2, y2);
        }
    }

    draw();
}