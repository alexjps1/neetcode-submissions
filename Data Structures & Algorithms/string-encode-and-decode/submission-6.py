class Solution:

    def encode(self, strs: List[str]) -> str:
        return "/empty/" if len(strs) == 0 else "/separator/".join(strs)

    def decode(self, s: str) -> List[str]:
        return [] if s == "/empty/" else s.split("/separator/")