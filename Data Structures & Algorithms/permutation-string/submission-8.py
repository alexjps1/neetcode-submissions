class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # fix window of size len(s1)
        # permutation = same freq dict

        # create freq of s1:
        az = "abcdefghijklmnopqrstuvwxyz"
        freq2 = {letter: 0 for letter in az}
        for i in range(len(s1)):
            freq2[s1[i]] += 1
        
        # create first window
        freq = {letter: 0 for letter in az}
        for r in range(len(s2)):
            freq[s2[r]] += 1
            # remove character before window
            if r - len(s1) >= 0:
                freq[s2[r - len(s1)]] -= 1
            if freq == freq2:
                return True
        return False
        

