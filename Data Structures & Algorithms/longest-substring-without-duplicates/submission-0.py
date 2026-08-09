class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        p1 = 0
        p2 = 0
        longest = 0
        ch = set(s[0])

        while p2 < len(s) - 1: # may need to change condition
            if s[p2+1] in ch:
                # moving forward would create an invalid string
                ch.remove(s[p1])
                p1 += 1
            else:
                p2 += 1
                ch.add(s[p2])
            longest = max(longest, p2-p1+1)

        
        return longest


