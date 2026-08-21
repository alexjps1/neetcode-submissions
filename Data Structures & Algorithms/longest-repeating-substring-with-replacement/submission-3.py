class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        freq = defaultdict(int)
        maxf = 0
        longest = 0
        while r < n:
            freq[s[r]] += 1
            # most frequent character
            # (only changes if r becomes most freq, as only r was added)
            # may become stale during shrink, but that doesn't change final answer
            maxf = max(maxf, freq[s[r]])
            r += 1
            while maxf + k < r-l:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r-l)
        return longest
            

