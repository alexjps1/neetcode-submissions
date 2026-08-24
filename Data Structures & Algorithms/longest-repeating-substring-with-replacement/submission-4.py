class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use r incl
        # valid window: window size - majority char ct <= k
        longest = 0
        l = 0
        n = len(s)
        freq = defaultdict(int)
        maxf = 0
        for r in range(n):
            freq[s[r]] += 1
            if freq[s[r]] > maxf:
                maxf = freq[s[r]]
            while r-l+1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
        

