#include <iostream>
#include <set>
using namespace std;
class ball
{
  private:
    bool direction;
    int speed;
    int length;

  public:
    int pos;

    void setData(int pos, int direction, int speed, int length)
    {
        this->pos = pos;
        this->direction = direction;
        this->speed = speed;
        this->length = length;
    }
    void move()
    {
        if (direction)
            pos += speed;
        else
            pos -= speed;

        if (pos == 0 || pos == length)
        {
            changeDirection();
        }
    }
    void changeDirection()
    {
        if(direction)
            direction = false;
        else
            direction = true;
    }
    friend ostream &operator<<(ostream &os, ball &object);
};
ostream &operator<<(ostream &os, ball &object)
{
    os << object.pos << " " << object.direction;
    return os;
}
int main()
{
    int n, l, t;
    cin >> n >> l >> t;
    ball balls[n];
    for (int i = 0; i < n; i++)
    {
        int pos;
        cin >> pos;
        balls[i].setData(pos, true, 1, l);
    }

    for (int time = 1; time <= t; time++)
    {
        for (int i = 0; i < n; i++)
        {
            balls[i].move();
        }
        set<int> find;
        for (int i = 0; i < n; i++)
        {
            if (find.find(i) == find.end())
            {
                for (int j = 0; j < n; j++)
                {
                    if (balls[i].pos == balls[j].pos)
                    {
                        balls[i].changeDirection();
                        balls[j].changeDirection();
                        find.insert(i);
                        find.insert(j);
                        break;
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << balls[i].pos << " ";
    }
}
