class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/") 
        ptr = 0
        while ptr < len(parts) and len(parts) > 0:
            if parts[ptr] == "..":
                if ptr > 0:
                    ptr -= 1
                    del parts[ptr]
                del parts[ptr]
                continue
            if parts[ptr] == "." or len(parts[ptr]) == 0:
                del parts[ptr]
                continue
            ptr += 1

        return "/" + "/".join(parts)

