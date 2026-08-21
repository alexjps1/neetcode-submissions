class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # build count of s1 (the pattern string)
        az = "abcdefghijklmnopqrstuvwxyz"
        ct1 = {letter: 0 for letter in az}
        for letter in s1:
            ct1[letter] += 1

        # build first s2 window (string in which to find perm)
        ct2 = {letter: 0 for letter in az}
        r = 0
        while r < len(s1):
            ct2[s2[r]] += 1
            r += 1

        # Check the very first window
        if ct1 == ct2:
            return True

        l = 0
        # use <= because r is inclusive and therefore we also want to run when = len(s2)
        while r < len(s2):
            ct2[s2[r]] += 1
            ct2[s2[l]] -= 1
            if ct1 == ct2:
                return True
            r += 1
            l += 1
        return False

            
