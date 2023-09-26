class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a=n
        b=int()
        for i in range(n):
            a-=1
            b+=1
            if "0" in str(a) or "0" in str(b):
                continue
            else:
                return[a,b]    

