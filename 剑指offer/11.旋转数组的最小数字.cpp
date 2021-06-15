#include <vector>
using namespace std;

class Solution {
public:
    int minArray(vector<int>& numbers)
    {
        int low = 0;
        int high = numbers.size() - 1;

        while (low < high) {
            int mid = low + (high - low) / 2;

            if (numbers[mid] < numbers[high]) {
                high = mid;
            } else if (numbers[mid] > numbers[high]) {
                low = mid + 1;
            } else {
                high -= 1;
            }
        }
        return numbers[high];
    }
};