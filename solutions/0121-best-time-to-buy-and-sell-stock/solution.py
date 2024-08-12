class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_p=prices[0]
        pro=0
        for p in prices[1:]:
            if b_p>p:
                b_p=p
            pro=max(pro,p-b_p)    
        return pro    
