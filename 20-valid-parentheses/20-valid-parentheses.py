class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='{' or c=='(' or c=='[' :
                stack.append(c)
            else :
                if(len(stack)<1):
                    return False

                o = stack.pop()
                if c == '}' and o!='{':
                    return False
                if c == ')' and o!='(':
                    return False
                if c == ']' and o!='[':
                    return False

        return len(stack) ==0
