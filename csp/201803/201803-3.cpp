#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

class UrlRule
{
  public:
    string name;
    string rule;
    vector<string> div;
    void division();
};

void UrlRule::division()
{
    const char *d = "/";
    char *p;
    char *s;
    s = new char[rule.length() + 1];
    strcpy(s, rule.c_str());

    p = strtok(s, d);
    while (p)
    {
        div.push_back(p);
        p = strtok(NULL, d);
    }
}

bool regexInt(string s)
{
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != '0' && s[i] != '1' && s[i] != '2' && s[i] != '3' && s[i] != '4' && s[i] != '5' && s[i] != '6' && s[i] != '7' && s[i] != '8' && s[i] != '9')
            return false;
    }
    return true;
}

void split(vector<string> &res, string url)
{
    const char *d = "/";
    char *p;
    char *s;
    s = new char[url.length() + 1];
    strcpy(s, url.c_str());

    p = strtok(s, d);
    while (p)
    {
        res.push_back(p);
        p = strtok(NULL, d);
    }
}

int main()
{
    int n, m;
    cin >> n >> m;

    UrlRule urlRules[n];
    for (int i = 0; i < n; i++)
    {
        cin >> urlRules[i].rule >> urlRules[i].name;
        urlRules[i].division();
    }

    string urls[m];
    for (int i = 0; i < m; i++)
    {
        cin >> urls[i];
    }

    for (int i = 0; i < m; i++)
    {
        vector<string> urlDiv;
        split(urlDiv, urls[i]);

        bool flag1 = false;
        for (int j = 0; j < sizeof(urlRules) / sizeof(urlRules[0]); j++)
        {
            vector<string> ruleDiv = urlRules[j].div;
            bool flag = true;
            bool isPath = false;
            vector<string> parameters;
            int k;
            for (k = 0; k < ruleDiv.size(); k++)
            {
                if (k >= urlDiv.size())
                {
                    flag = false;
                    break;
                }

                if (ruleDiv[k] == "<int>")
                {
                    if (regexInt(urlDiv[k]))
                    {
                        string parameter = urlDiv[k];
                        if(parameter[0] == '0')
                            parameter = parameter.substr(1);
                        parameters.push_back(parameter);
                    }
                    else
                    {
                        flag = false;
                        break;
                    }
                }
                else if (ruleDiv[k] == "<str>")
                {
                    parameters.push_back(urlDiv[k]);
                }
                else if (ruleDiv[k] == "<path>")
                {
                    string parameter = "";
                    isPath = true;
                    int m = k;
                    for (; m < urlDiv.size() - 1; m++)
                    {
                        parameter += urlDiv[m] + "/";
                    }
                    parameter += urlDiv[m];
                    parameters.push_back(parameter);
                    break;
                }
                else
                {
                    if (urlDiv[k] != ruleDiv[k])
                    {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag && (k == urlDiv.size() || isPath))
            {
                flag1 = true;
                cout << urlRules[j].name << " ";

                for (int k = 0; k < parameters.size(); k++)
                {
                    cout << parameters[k] << " ";
                }
                cout << endl;
            }
        }
        if (!flag1)
        {
            cout << "404" << endl;
        }
    }
}