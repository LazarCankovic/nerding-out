class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # creating close : open pairs because when we see the closing bracket
        # there should be a open one on top of the stack
        pairs = { "]" : "[", ")" : "(", "}": "{"}

        for c in s:
            # if it's a closing bracket
            if c in pairs:
                # if the stack is not empty and the last element is the opening one
                # previously added
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False