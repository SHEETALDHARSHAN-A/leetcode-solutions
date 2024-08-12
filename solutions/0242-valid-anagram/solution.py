class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not(len(s) == len(t)):
            return False
        l=list(s)
        l.sort()
        l2=list(t)
        l2.sort()
        for i in range(len(t)):
            if(l[i]==l2[i]):
                continue
            else:
                return False
        return True            
