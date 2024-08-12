class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        aux=[]
        if len(nums1)>=len(nums2):
            num=list(set(nums1))
            num1=list(set(nums2))
            for i in range(len(num1)):
                if num1[i] in num:
                    aux.append(num1[i])
        else:
            num=list(set(nums1))
            num1=list(set(nums2))
            for i in range(len(num)):
                if num[i] in num1:
                    aux.append(num[i])            
        return aux            

