class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path.split("/"))
        stack = []

        for temp in path.split("/"):
            if len(temp) > 0:
                if temp == ".":
                    continue
                elif temp == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(temp)
        
        answer= "/".join(stack)
        answer = "/" + answer

        return answer
