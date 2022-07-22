class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        toBeReversed = ""
        
        for i in s:
            if i == ")":
                top = stack.pop()
                while top != "(":
                    toBeReversed += top
                    top = stack.pop()
                
                for j in toBeReversed:
                    stack.append(j)
                    
                toBeReversed = ""
            else:
                stack.append(i)
            
        return ''.join(stack)
            
        