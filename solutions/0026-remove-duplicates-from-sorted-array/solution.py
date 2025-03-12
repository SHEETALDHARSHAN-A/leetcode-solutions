class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        curr_unique=1
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[curr_unique]=nums[i]
                curr_unique+=1
            else:
                continue
        return curr_unique               

