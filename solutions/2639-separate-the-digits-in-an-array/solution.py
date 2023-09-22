class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        import sys
        sys.set_int_max_str_digits(10**5)
        su = [str(i) for i in nums]
        res=(int("".join(su)))
        res=str(res)
        res = [int(x) for x in str(res)]
        return res
        
