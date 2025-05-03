class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result="";
        int i =0;
        int w1_len=word1.length();
        int w2_len=word2.length();

        while(i<w1_len || i<w2_len)
        {
            if (i<w1_len)
            {
                result+=word1[i];
            }
            if(i<w2_len)
            {
                result+=word2[i];
            } 
            i++;
        }
        return result;
    }
};
