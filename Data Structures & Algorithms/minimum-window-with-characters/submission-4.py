class Solution:
    def valid(self, wf, tf) -> bool:
        if len(wf) < len(tf):
            return False
        for letter in tf:
            if wf[letter] < tf[letter]:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        shortest = None
        shortestLength = math.inf
        
        lower = "abcdefghijklmnopqrstuvwxyz" 
        self.az = lower + lower.upper()

        tf = {letter: 0 for letter in self.az}
        for letter in t:
            tf[letter] += 1
        

        wf = {letter: 0 for letter in self.az}
        l = 0
        satisfied = 0
        required = sum([1 for i in self.az if tf[i] > 0])
        for r in range(len(s)):
            wf[s[r]] += 1
            if wf[s[r]] == tf[s[r]]:
                satisfied += 1
            while satisfied == required:
                if r - l + 1 < shortestLength:
                    shortestLength = r - l + 1
                    shortest = s[l:r+1]
                wf[s[l]] -= 1
                if wf[s[l]] < tf[s[l]]:
                    satisfied -= 1
                l += 1
        
        return shortest if shortest else ""