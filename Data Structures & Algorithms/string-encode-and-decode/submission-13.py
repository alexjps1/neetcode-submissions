class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ":"
        delimiter = ";"
        for s in strs:
            if delimiter in s:
                delimiter = f"{delimiter};"
        ans = f"{delimiter}:{delimiter.join(strs)}"
        print(ans)
        return ans 

    def decode(self, s: str) -> List[str]:
        if s[0] == ":":
            return []
        i = 0
        while s[i] == ";":
            i += 1
        delimiter = "".join([";"] * i)
        return s[i+1:].split(delimiter) 
        

