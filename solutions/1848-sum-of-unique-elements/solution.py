class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        li=set(nums)
        temp=[]
        sums=0
        for i in nums:
            if (nums.count(i)>1):
                temp.append(i)
        for j in li:
            if j not in temp:
                sums=sums+j
        return sums            
