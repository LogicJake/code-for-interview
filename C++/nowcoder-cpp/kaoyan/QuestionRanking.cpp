#include <iostream>
using namespace std;
class student
{
  public:
    string name;
    int score;
    bool operator>(const student &obj);
    bool operator<(const student &obj);
    bool operator==(const student &obj);
};

bool student::operator<(const student &obj)
{
    if (score < obj.score)
        return true;
    else
        return false;
}

bool student::operator==(const student &obj)
{
    if (score == obj.score)
        return true;
    else
        return false;
}

bool student::operator>(const student &obj)
{
    if (score > obj.score)
        return true;
    else
        return false;
}

void bubble_sort_1(student arr[], int len)
{
    int i, j;
    student temp;
    for (i = 0; i < len - 1; i++)
        for (j = 0; j < len - 1 - i; j++)
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
}

void bubble_sort_0(student arr[], int len)
{
    int i, j;
    student temp;
    for (i = 0; i < len - 1; i++)
        for (j = 0; j < len - 1 - i; j++)
            if (arr[j] < arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
}

int main()
{
    int m, n;
    cin >> m >> n;

    student a[m];
    for (int i = 0; i < m; i++)
    {
        cin >> a[i].name >> a[i].score;
    }

    if (n == 0)
    {
        bubble_sort_0(a, m);
    }
    else
    {
        bubble_sort_1(a, m);
    }

    for (int i = 0; i < m; i++)
    {
        cout << a[i].name << " " << a[i].score << endl;
    }
}