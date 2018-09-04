#include <iostream>
using namespace std;
int n, m;

int find(string server[], int start, string target)
{
    while (start != m)
    {
        if (server[start] == target)
            return start;
        start++;
    }
    return -1;
}

//找出每个proxy在当前位置后出现的地方，尝试找出出现最晚的proxy
string selectProxy(int index, string proxys[], string servers[])
{
    string currentServerIp = servers[index];

    int maxPos = 0;
    string selectProxy;
    for (int i = 0; i < n; i++)
    {
        int nextPos = find(servers, index, proxys[i]);

        //在之后都不会出现在server中的proxy是毫无疑问的最佳proxy
        if (nextPos == -1)
        {
            selectProxy = proxys[i];
            return selectProxy;
        }

        if (nextPos - index > maxPos)
        {
            maxPos = nextPos - index;
            selectProxy = proxys[i];
        }
    }

    //最佳的proxy是现在的server地址，没有合适的proxy使用
    if (maxPos == 0)
    {
        return "no pooxy";
    }
    return selectProxy;
}

int main()
{
    cin >> n;
    string proxys[n];

    for (int i = 0; i < n; i++)
    {
        cin >> proxys[i];
    }

    cin >> m;
    string servers[m];

    for (int i = 0; i < m; i++)
    {
        string serverIp;
        cin >> serverIp;
        servers[i] = serverIp;
    }

    int num = 0;
    string currentProxy = "";
    bool fail = false;
    for (int i = 0; i < m; i++)
    {
        if (servers[i] == currentProxy || currentProxy == "")
        {
            currentProxy = selectProxy(i, proxys, servers);
            if (currentProxy == "no pooxy")
            {
                fail = true;
                break;
            }

            num++;
        }
    }

    if (fail)
    {
        cout << -1;
    }
    else
    {
        cout << num - 1;
    }
}