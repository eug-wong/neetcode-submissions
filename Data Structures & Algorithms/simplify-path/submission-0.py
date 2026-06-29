class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = "/"
        for c in path:
            if c == "/" and new_path[-1] == "/":
                continue
            else:
                new_path = new_path + c
        
        new_path = new_path.split("/")
        new_path = [x for x in new_path if x != ""]
        stack = []
        for f in new_path:
            if f == "..":
                if stack:
                    stack.pop()
            elif f == ".":
                continue
            else:
                stack.append(f)
        
        res = ""
        for f in stack:
            res = res + f + "/"

        if res and res[-1] == "/":
            res = res[: -1]

        if not res or res[0] != "/":
            res = "/" + res
    
        return res
