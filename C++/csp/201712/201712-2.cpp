#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

class person
{
  public:
    int no;
    bool out;
};

bool isOut(int index, int k)
{
    if (index % k == 0)
    {
        return true;
    }
    else if (index % 10 == k)
    {
        return true;
    }
    else
    {
        return false;
    }
}
int main()
{
    int n, k;
    cin >> n >> k;
    person persons[n + 1];
    int num = n;

    for (int i = 1; i <= n; i++)
    {
        persons[i].no = i;
        persons[i].out = false;
    }

    int i = 0;
    int j = 1;
    while (1)
    {
        //i+1位置淘汰
        if (isOut(j, k))
        {
            persons[i + 1].out = true;
            num--;
        }
        if (num == 1)
        {
            for (int j = 1; j <= n; j++)
            {
                if (!persons[j].out)
                {
                    cout << persons[j].no;
                    break;
                }
            }
            break;
        }
        do
        {
            i = (i + 1) % n;
        } while (persons[i + 1].out);
        j++;
    }
}