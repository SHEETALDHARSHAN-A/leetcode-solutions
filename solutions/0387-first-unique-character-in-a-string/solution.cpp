class Solution {
public:
    int firstUniqChar(string s) {
       int charArr[26] = {0};
        int stringlen = (s.length());
        int i, index;

        for (i = 0; i < stringlen; ++i) {
            charArr[s[i] - 'a']++;
        }

        for (i = 0; i < stringlen; ++i) {
            if (charArr[s[i] - 'a'] == 1) {
                return i;
            }
        }

        return -1;
    }
};
