class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
             str2=(str(x)[::-1])
             str2=str2[:-1]
             str2='-'+str2
             x2=int(str2)  
        elif(x%10==0):
            x=x//10
            x2=(int(str(x)[::-1]))
        else:
             x2=(int(str(x)[::-1]))                   
        if((x2<(2**31)-1) and x2>(-2**31)):
            return x2
        else:
            return 0    
          
     
                 
