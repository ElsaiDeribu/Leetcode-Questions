class Solution:
    def scoreOfParentheses(self, s: str) -> int:
               
        stack = []
        curr = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(curr)
                curr = 0
                
            else:
                curr = stack.pop() + max(curr * 2, 1)
                
                
        return curr