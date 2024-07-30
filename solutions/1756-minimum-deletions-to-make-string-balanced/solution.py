class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = 0
        minDel = 0
        for char in s:
            if char == 'a':
                minDel = min(minDel + 1, bCount)
            else:
                bCount += 1   
        return minDel  
