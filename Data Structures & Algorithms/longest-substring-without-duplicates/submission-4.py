class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = p1 = p2 = 0
        ch = set()
        while p2 < len(s):
            if s[p2] in ch:
                ch.remove(s[p1])
                p1 += 1
            else:
                longest = max(longest, p2-p1+1)
                ch.add(s[p2])
                p2 += 1
        return longest