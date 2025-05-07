class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int>s_hash;
        std::unordered_map<char,int>t_hash;
        if(s.length() != t.length())
        {
            return false;
        }
        for (char c:s){
            s_hash[c]++;
        }
        for (char c:t){
            t_hash[c]++;
        }       
        for (int i = 0;i<s.length();i++)
        {
            if(!(s_hash[s[i]] == t_hash[s[i]]))
            {
                return false;;
            }
        }
        return true;
    }
};
