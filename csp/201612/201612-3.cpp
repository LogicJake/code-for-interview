#include <iostream>
#include <map>
#include <sstream>
#include <stdio.h>
#include <string.h>
using namespace std;

class privilege
{
  public:
    string category;
    string level;
};

void getPrivilege(string s, string &category, int &level)
{
    if (s.find(':') == string::npos)
    {
        category = s;
        level = -1; //代表无等级限制
    }
    else
    {
        const char *div = ":";
        char *p = (char *)s.c_str();
        char *r;
        category = strtok(p, div);
        r = strtok(NULL, div);
        stringstream ss(r);
        ss >> level;
    }
}

// -1 ：无权限 -2：有权限 正整数代表最高等级
int check(map<string, map<string, int>> user, string name, string query)
{
    if (user.find(name) == user.end())
    {
        return -1;
    }
    map<string, int> pr = user[name];

    string category;
    int query_level;
    getPrivilege(query, category, query_level);

    if (pr.find(category) == pr.end())
    {
        return -1;
    }

    int real_level = pr.find(category)->second;
    //能查询到该权限且该权限无等级限制，直接返回true
    if (real_level == -1)
    {
        return -2;
    }

    //能查询到该权限且该权限有等级限制
    if (real_level != -1)
    {
        if (query_level == -1)
        {
            return real_level;
        }
        else
        {
            if (real_level < query_level)
            {
                return -1;
            }
            else
            {
                return -2;
            }
        }
    }
}

int main()
{
    int p, r, u, q;

    map<string, int> privileges;
    map<string, map<string, int>> role;
    map<string, map<string, int>> user;

    cin >> p;
    for (int i = 0; i < p; i++)
    {
        string input;
        cin >> input;
        string category;
        int level;
        getPrivilege(input, category, level);
        privileges.insert(make_pair(category, level));
        // privileges.insert(pair<string, int>(category, level));
    }

    cin >> r;
    for (int i = 0; i < r; i++)
    {
        string name;
        cin >> name;
        int num;
        cin >> num;

        map<string, int> role_privileges;
        for (int j = 0; j < num; j++)
        {
            string input;
            cin >> input;
            string category;
            int level;
            getPrivilege(input, category, level);
            role_privileges[category] = level;
        }

        role[name] = role_privileges;
    }

    cin >> u;
    for (int i = 0; i < u; i++)
    {
        string name;
        cin >> name;
        int num;
        cin >> num;

        map<string, int> user_privileges = user[name];
        for (int j = 0; j < num; j++)
        {
            string role_name;
            cin >> role_name;

            //一定存在role
            map<string, int> pr = role[role_name];
            map<string, int>::iterator it = pr.begin();

            while (it != pr.end())
            {
                string category = it->first;
                int level = it->second;

                //如果之前没有这个权限或者权限等级比现在低，则加入现在的权限
                if (user_privileges.find(category) == user_privileges.end() || (user_privileges.find(category)->second < level))
                {
                    user_privileges[category] = level;
                }
                it++;
            }
        }

        //更新权限
        user[name] = user_privileges;
    }

    cin >> q;
    int res[q];

    for (int i = 0; i < q; i++)
    {
        string name, query;
        cin >> name >> query;
        res[i] = check(user, name, query);
    }

    for (int i = 0; i < q; i++)
    {
        if (res[i] == -1)
        {
            cout << "false" << endl;
        }
        else if (res[i] == -2)
        {
            cout << "true" << endl;
        }
        else
        {
            cout << res[i] << endl;
        }
    }
}