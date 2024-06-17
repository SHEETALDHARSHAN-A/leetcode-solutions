class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = [0] * 128
        left = 0
        right = 0
        res = 0

        while right < len(s):
            r = s[right]
            char_set[ord(r)] += 1
            while char_set[ord(r)] > 1:
                l = s[left]
                char_set[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res
