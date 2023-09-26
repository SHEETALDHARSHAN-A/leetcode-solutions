class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res = []
        for i in s.split():
            if i.isdigit():
                res.append(int(i))
        for i in range(1,len(res)):
            if(res[(i)-1]>=res[(i)] ):
                return False
        return True
