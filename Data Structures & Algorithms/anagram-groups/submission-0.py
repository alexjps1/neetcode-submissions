from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(s: str) -> str:
            code = [0] * 26 
            for i in s:
                code[ord(i) -  ord('a')] += 1
            return "a".join([str(i) for i in code])
        
        d: Dict[str, List[str]] = defaultdict(list)
        for s in strs:
            encoded = encode(s)
            d[encoded].append(s)
        
        return list(d.values())
        

