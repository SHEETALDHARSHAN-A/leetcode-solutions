class Solution {
public:
    int strStr(string haystack, string needle) {
        int h_len = haystack.length();
        int n_len = needle.length();
        if(h_len < n_len)
        {
            return -1;
        }
        for(int i=0;i <= h_len - n_len;i++)
        //loop until last pair length of needle
        {
            if(haystack.substr(i,n_len)==needle)
            //check each substr of haystack len of needle and str needle 
            { 
                return i;
            }
        }
        return -1;
    }
};
