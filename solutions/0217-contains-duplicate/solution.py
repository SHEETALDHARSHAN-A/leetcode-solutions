class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sl=set(nums)
        if(len(nums)!=len(sl)):
            return True
        return False
