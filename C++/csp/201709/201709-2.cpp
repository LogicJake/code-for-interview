#include <iostream>
#include <queue>
using namespace std;

class queueNode
{
  public:
    int id;
    int time;
    bool operator<(const queueNode &obj)
    {

        if (obj.time < time)
        {
            return true;
        }
        else if (obj.time == time && obj.id < id)
        {
            return true;
        }

        return false;
    }
    queueNode(int a, int b)
    {
        id = a;
        time = b;
    }
};

//返回最左边空位置
int getReturnPos(int a[], int size)
{
    for (int i = 1; i <= size; i++)
    {
        if (a[i] == -1)
        {
            return i;
        }
    }
    return -1;
}

//返回需要借钥匙的位置
int getBorrowPos(int a[], int size, int id)
{
    for (int i = 1; i <= size; i++)
    {
        if (a[i] == id)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int n, k;
    cin >> n >> k;
    int pos[n + 1]; //钥匙放置位置

    priority_queue<queueNode> borrowQueue; //借队列
    priority_queue<queueNode> returnQueue; //还队列
    for (int i = 1; i < n + 1; i++)
    {
        pos[i] = i;
    }

    for (int i = 0; i < k; i++)
    {
        int w, s, c;
        cin >> w >> s >> c;
        queueNode bNode(w, s);
        queueNode rNode(w, s + c);

        borrowQueue.push(bNode);
        returnQueue.push(rNode);
    }

    while (!borrowQueue.empty() && !returnQueue.empty())
    {
        //优先还完所有钥匙
        while (borrowQueue.top().time >= returnQueue.top().time)
        {
            int returnPos = getReturnPos(pos, n);
            pos[returnPos] = returnQueue.top().id;
            returnQueue.pop();
        }
        if (borrowQueue.top().time < returnQueue.top().time)
        {
            int borrowPos = getBorrowPos(pos, n, borrowQueue.top().id);
            pos[borrowPos] = -1;
            borrowQueue.pop();
        }
    }

    //把钥匙还完
    while (!returnQueue.empty())
    {
        int returnPos = getReturnPos(pos, n);
        pos[returnPos] = returnQueue.top().id;
        returnQueue.pop();
    }

    for (int i = 1; i < n + 1; i++)
    {
        cout << pos[i] << " ";
    }
}
