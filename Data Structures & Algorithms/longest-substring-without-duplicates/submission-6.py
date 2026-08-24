class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        n = len(s)
        l = 0
        mp = {}
        for r in range(0, n):
            if s[r] in mp:
                # don't allow jumping backwards
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest

        