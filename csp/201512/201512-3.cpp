#include <iostream>
using namespace std;

int m, n, q;
char **pic;

int *transformation(int x, int y)
{
    int res[2];
    int x1, y1;
    y1 = x;
    x1 = n - 1 - y;
    res[0] = x1;
    res[1] = y1;
    return res;
}

void draw()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << pic[i][j] << " ";
        }
        cout << endl;
    }
}

void fill(int x, int y, char c)
{
    int *res = transformation(x, y);
    if (pic[res[0]][res[1]] == c || pic[res[0]][res[1]] == '-' || pic[res[0]][res[1]] == '|' || pic[res[0]][res[1]] == '+' || x >= m || x < 0 || y >= n || y < 0)
        return;
    pic[res[0]][res[1]] = c;
    cout << res[0] << " " << res[1] << endl;
    draw();
    return;

    fill(x, y + 1, c);
    fill(x, y - 1, c);
    fill(x + 1, y, c);
    fill(x - 1, y, c);
}

int main()
{
    cin >> m >> n >> q;
    char **pic;
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
            char c;
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            if (y1 == y2)
            {
                c = '-';
                if (x1 < x2)
                {
                    for (int i = x1; i <= x2; i++)
                    {
                        int *a = transformation(i, y1);

                        if (pic[a[0]][a[1]] == '|')
                        {
                            pic[a[0]][a[1]] = '+';
                        }
                        else
                            pic[a[0]][a[1]] = c;
                    }
                }
                else
                {
                    for (int i = x2; i <= x1; i++)
                    {
                        int *a = transformation(i, y1);

                        if (pic[a[0]][a[1]] == '|')
                        {
                            pic[a[0]][a[1]] = '+';
                        }
                        else
                            pic[a[0]][a[1]] = c;
                    }
                }
            }
            else
            {
                c = '|';
                if (y1 < y2)
                {
                    for (int i = y1; i <= y2; i++)
                    {
                        int *a = transformation(x1, i);

                        if (pic[a[0]][a[1]] == '-')
                        {
                            pic[a[0]][a[1]] = '+';
                        }
                        else
                            pic[a[0]][a[1]] = c;
                    }
                }
                else
                {
                    for (int i = y2; i <= y1; i++)
                    {
                        int *a = transformation(x1, i);

                        if (pic[a[0]][a[1]] == '-')
                        {
                            pic[a[0]][a[1]] = '+';
                        }
                        else
                            pic[a[0]][a[1]] = c;
                    }
                }
            }
        }
    }
}