#include <iomanip>
#include <iostream>
#include <math.h>

using namespace std;
int main()
{
    double x0, y0, z0, x1, y1, z1;
    cin >> x0 >> y0 >> z0 >> x1 >> y1 >> z1;

    double r, v;
    r = sqrt(pow(x0 - x1, 2) + pow(y0 - y1, 2) + pow(z0 - z1, 2));
    v = 4.0 / 3 * acos(-1) * pow(r, 3);

    cout << setiosflags(ios::fixed) << setprecision(3) << r << " " << v;
}