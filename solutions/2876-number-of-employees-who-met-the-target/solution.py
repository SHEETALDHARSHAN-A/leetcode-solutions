class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
      ar=[i for i in hours if(i>=target)]  
      return len(ar)
