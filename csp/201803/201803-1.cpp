#include <iostream>
using namespace std;
int main()
{
    int num;
    int score = 0;
    int lastScore = 1;
    do{
        cin >> num;
        
        switch (num)
        {
            case 1:
                score += 1;
                lastScore = 1;
                break;
            case 2:
                if (lastScore == 1) {
                    lastScore = 2;
                    score += 2;
                }
                else
                {
                    lastScore += 2;
                    score += lastScore;
                }
            default:
                break;
        }
    } while (num != 0);
    cout << score;
}
