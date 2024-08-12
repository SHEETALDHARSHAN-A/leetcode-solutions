class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumofall=sum(range(0,len(nums)+1))
        sumofel=sum(nums)
        return sumofall-sumofel   
