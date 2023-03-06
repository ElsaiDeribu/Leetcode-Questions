class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        count = Counter(s)
        stackElements = set()
        stack = []
        
        
        for i in range(len(s)):
            
            if s[i] not in stackElements:
                while stack and (stack[-1] > s[i] and count[stack[-1]] > 0):
                    temp = stack.pop()
                    stackElements.remove(temp)

             
                stack.append(s[i])
                count[s[i]] -= 1
                stackElements.add(s[i])

            else:
                count[s[i]] -= 1
                
        
                
        return ''.join(stack)
        
