class Solution:
    def commonprefix(self, s1, s2):
        minlen = min(len(s1), len(s2))
        res = ""
        for i in range(minlen):
            if s1[i] == s2[i]:
                res += s1[i]
            else:
                return res
        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for s in strs[1:]:
            # update lcp based on s
            lcp = self.commonprefix(lcp, s)

        return lcp