class Solution:
    def countDigits(self, num: int) -> int:
        rem=0
        c=0
        a=num
        while(num):
            rem=num%10
            if(a%rem==0):
                c=c+1
            num=num//10
        return c          
