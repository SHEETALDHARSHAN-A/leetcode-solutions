class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        maxi=0
        for i in (prices):
            if i < mini:
                mini=i
            elif i-mini > maxi:
                maxi=i-mini

        return maxi

