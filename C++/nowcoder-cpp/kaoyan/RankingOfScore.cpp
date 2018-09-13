#include <algorithm>
#include <iostream>
using namespace std;

class student
{
  public:
    int id;
    int score;
    bool operator<(const student &obj)
    {

        if (score < obj.score)
        {
            return true;
        }
        else if (score == obj.score && id < obj.id)
        {
            return true;
        }
        return false;
    }

    bool operator>(const student &obj)
    {

        if (score > obj.score)
        {
            return true;
        }
        else if (score == obj.score && id > obj.id)
        {
            return true;
        }
        return false;
    }
};

void quickSort(student s[], int low, int high)
{
    student key = s[low];

    if (low >= high)
    {
        return;
    }
    int i = low;
    int j = high;
    while (i < j)
    {
        while (i < j && s[j] > key)
        {
            j--;
        }
        s[i] = s[j];
        while (i < j && s[i] < key)
        {
            i++;
        }
        s[j] = s[i];
    }

    s[i] = key;

    quickSort(s, low, i - 1);
    quickSort(s, i + 1, high);

}
int main()
{
    int n;
    cin >> n;
    student students[n];

    for (int i = 0; i < n; i++)
    {
        cin >> students[i].id >> students[i].score;
    }

    //sort(students, students + n);
    quickSort(students, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << students[i].id << " " << students[i].score << endl;
    }

    return 0;
}
