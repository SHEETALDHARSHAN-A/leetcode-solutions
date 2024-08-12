class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=list(set(nums))
        l.sort()
        nums[0:len(l)+1]=l
        return len(l)
