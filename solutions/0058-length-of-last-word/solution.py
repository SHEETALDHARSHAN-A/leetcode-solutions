class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=list(map(len,s.split()))
        return res[len(res)-1]

