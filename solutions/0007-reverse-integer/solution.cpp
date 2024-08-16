class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        int sign = x < 0 ? -1 : 1;
        x = abs(x);

        while (x != 0) {
            int rem = x % 10;
            if (rev > (INT_MAX - rem) / 10) {
                return 0;
            }
            rev = rev * 10 + rem;
            x /= 10;
        }

        return rev * sign;
    }
};
