class Solution {
public:
    void merge(int A[], int m, int B[], int n)
    {
        int total = m + n;
        int i = m - 1;
        int j = n - 1;
        int cur = total - 1;

        while (i >= 0 && j >= 0) {
            if (A[i] >= B[j]) {
                A[cur] = A[i];
                i -= 1;
            } else {
                A[cur] = B[j];
                j -= 1;
            }
            cur -= 1;
        }

        while (j >= 0) {
            A[cur] = B[j];
            j -= 1;
            cur -= 1;
        }
    }
};