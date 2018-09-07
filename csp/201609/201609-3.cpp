#include <iostream>
#include <vector>
using namespace std;

class role
{
  public:
    int health;
    int attack;
    role(int h, int a)
    {
        health = h;
        attack = a;
    }
};

//当前是哪个英雄在行动
int current_hero = 0;
vector<role> role0;
vector<role> role1;

void switchHero()
{
    current_hero = (current_hero + 1) % 2;
}

void summon(vector<role> &currentRole, int pos, int attack, int health)
{
    //随从个数，减去首位的英雄
    int entourageNum = currentRole.size() - 1;
    //最右边直接插入
    if (pos > entourageNum)
    {
        currentRole.push_back(role(health, attack));
    }
    else
    {
        currentRole.insert(currentRole.begin() + pos, role(health, attack));
    }
}

void attack(vector<role> &attacker, vector<role> &defender, int attackerPos, int defenderPos)
{
    int hx, ax, hy, ay;
    hx = attacker[attackerPos].health;
    ax = attacker[attackerPos].attack;

    hy = defender[defenderPos].health;
    ay = defender[defenderPos].attack;

    hx -= ay;
    hy -= ax;

    if (hx <= 0)
        attacker.erase(attacker.begin() + attackerPos);
    else
        attacker[attackerPos].health = hx;

    if (hy <= 0 && defenderPos != 0)
        defender.erase(defender.begin() + defenderPos);
    else
        defender[defenderPos].health = hy;
}

void print()
{
    if (role0[0].health != 0 && role1[0].health != 0)
        cout << 0 << endl;
    else if (role0[0].health <= 0)
    {
        cout << -1 << endl;
    }
    else if (role1[0].health <= 0)
    {
        cout << 1 << endl;
    }

    cout << role0[0].health << endl;
    cout << role0.size() - 1 << " ";
    for (int i = 1; i < role0.size(); i++)
    {
        cout << role0[i].health << " ";
    }
    cout << endl;

    cout << role1[0].health << endl;
    cout << role1.size() - 1 << " ";
    for (int i = 1; i < role0.size(); i++)
    {
        cout << role1[i].health << " ";
    }
}

int main()
{
    role hero0(30, 0), hero1(30, 0);

    //0位是英雄，1~7是随从
    role0.push_back(hero0);
    role1.push_back(hero1);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string orderType;
        cin >> orderType;

        if (orderType == "summon")
        {
            int pos, attack, health;
            cin >> pos >> attack >> health;
            if (current_hero == 0)
                summon(role0, pos, attack, health);
            else
                summon(role1, pos, attack, health);
        }
        else if (orderType == "end")
        {
            switchHero();
        }
        else if (orderType == "attack")
        {
            int attackerPos, defenderPos;
            cin >> attackerPos >> defenderPos;
            if (current_hero == 0)
                attack(role0, role1, attackerPos, defenderPos);
            else
                attack(role1, role0, attackerPos, defenderPos);
        }
    }

    print();
}