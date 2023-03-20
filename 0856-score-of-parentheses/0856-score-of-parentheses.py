class Solution:
    def scoreOfParentheses(self, s: str) -> int:
               
        s = s.replace(")(", ")+(" )
        s = s.replace("()", "1")
        s = s.replace(")", ")*2")
        
        return eval(s) 