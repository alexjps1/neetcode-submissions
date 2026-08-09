class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
                continue
            if len(stack) == 0 or pairs[char] != stack.pop():
                return False
        if len(stack) == 0:
            return True 
        return False