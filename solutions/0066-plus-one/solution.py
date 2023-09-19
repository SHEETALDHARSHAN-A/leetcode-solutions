class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      a=0
      for i in digits:
         a=i+a*10
      a=a+1
      res = list(map(int, str(a)))
      return list(res) 


        
