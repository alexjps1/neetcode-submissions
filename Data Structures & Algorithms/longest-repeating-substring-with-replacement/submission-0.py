class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        n = len(s)
        l = 0
        r = 0
        longest = 0
        freq = defaultdict(int)
        while r < n:
            freq[s[r]] += 1
            r += 1
            maxchar = max(list(freq.items()), key=lambda x: x[1])[0]
            while freq[maxchar] + k < r-l:
                freq[s[l]] -= 1
                l += 1
                maxchar = max(list(freq.items()), key=lambda x: x[1])[0]
            longest = max(longest, r-l)
        return longest
            

