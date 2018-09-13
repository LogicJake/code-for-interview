#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string.h>

using namespace std;
int stoi(string s)
{
    stringstream ss(s);
    int value;
    ss >> value;
    return value;
}
class my_time
{
  public:
    int year;
    int month;
    int day;
    int hour;
    int minute;
    my_time(string s)
    {
        year = stoi(s.substr(0, 4));
        month = stoi(s.substr(4, 2));
        day = stoi(s.substr(6, 2));
        hour = stoi(s.substr(8, 2));
        minute = stoi(s.substr(10, 2));
    }
    friend ostream &operator<<(ostream &out, const my_time &obj);

    bool operator!=(const my_time &right)
    {
        if (year != right.year || month != right.month || day != right.day || hour != right.hour || minute != right.minute)
        {
            return true;
        }
        return false;
    }

    my_time operator++()
    {
        minute++;
        if (minute >= 60)
        {
            hour += minute / 60;
            minute %= 60;
        }
        if (hour >= 23)
        {
            day += hour / 23;
            hour %= 23;
        }
        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
        {
            if (day >= 31)
            {
                month += day / 31;
                day %= 31;
            }
        }
        else if (month == 4 || month == 6 || month == 9 || month == 11)
        {
            if (day >= 30)
            {
                month += day / 30;
                day %= 30;
            }
        }
        else if (month == 2)
        {
            if (day >= 28)
            {
                month += day / 28;
                day %= 28;
            }
        }
        if (month >= 12)
        {
            year += month / 12;
            month %= 12;
        }
        return *this;
    }

    my_time operator++(int)
    {
        my_time tmp = *this;
        minute++;
        if (minute >= 60)
        {
            hour += minute / 60;
            minute %= 60;
        }
        if (hour >= 24)
        {
            day += hour / 24;
            hour %= 24;
        }
        if (day >= 31)
        {
            month += day / 31;
            day %= 31;
        }
        if (month >= 12)
        {
            year += month / 12;
            month %= 12;
        }
        return tmp;
    }
};

class crontab
{
  public:
    string minute;
    string hour;
    string dayOfMonth;
    string month;
    string dayOfWeek;
    string command;
    void serData(string s)
    {
        const char *delime = " ";
        char *p = (char *)s.c_str();
        char *res;
        res = strtok(p, delime);
        minute = res;
        res = strtok(NULL, delime);
        hour = res;
        res = strtok(NULL, delime);
        dayOfMonth = res;
        res = strtok(NULL, delime);
        month = res;
        res = strtok(NULL, delime);
        dayOfWeek = res;
        res = strtok(NULL, delime);
        command = res;
    }

    bool check(my_time time)
    {
        if (minute == "*" || stoi(minute) == time.minute)
        {
            if (hour == "*" || stoi(hour) == time.hour)
            {

                if (dayOfMonth == "*" || stoi(dayOfMonth) == time.day)
                {

                    if (month == "*" || stoi(month) == time.month)
                    {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
ostream &operator<<(ostream &out, const my_time &obj)
{
    out << obj.year << setw(2) << setfill('0') << obj.month << setw(2) << setfill('0') << obj.day << setw(2) << setfill('0') << obj.hour << setw(2) << setfill('0') << obj.minute;
    return out;
}

int main()
{
    int n;
    string s, t;
    cin >> n >> s >> t;
    my_time startTime(s);
    my_time endTime(t);
    cin.ignore();
    crontab crontabs[n];

    for (int i = 0; i < n; i++)
    {
        string s;
        getline(cin, s);
        crontabs[i].serData(s);
    }

    my_time timepass = startTime;

    while (timepass != endTime)
    {
        for (int i = 0; i < n; i++)
        {
            if (crontabs[i].check(timepass))
            {
                cout << timepass << " " << crontabs[i].command << endl;
                break;
            }
        }
        timepass++;
    }
}