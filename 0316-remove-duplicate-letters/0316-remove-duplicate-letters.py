class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        count = Counter(s)
        stackElements = set()
        stack = []
        
        
        for i in range(len(s)):
            
            
            while stack and (stack[-1] > s[i] and count[stack[-1]] > 0) and s[i] not in stackElements:
                temp = stack.pop()
                stackElements.remove(temp) if temp in stackElements else None 


            if s[i] not in stackElements:
                stack.append(s[i])
                count[s[i]] -= 1
                stackElements.add(s[i])
                
            else:
                count[s[i]] -= 1
                
        
                
        return ''.join(stack)
        
