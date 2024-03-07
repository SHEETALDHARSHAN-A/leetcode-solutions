class Solution:
    def minTimeToType(self, word: str) -> int:    
        total,pointer=0,0
        for i in word:
            nxtChar=ord(i)-ord('a')
            path1=abs(pointer-nxtChar)
            path2=26-path1
            total+=min(path1,path2)
            pointer=nxtChar
        return total+len(word)    
