class Solution:
    def reverseWords(self, s: str) -> str:
        a = split(' ', s)
        
        print(a)
        
        for i in range(len(a)):
            a[i] = split('', a[i])
            a[i].reverse()
            a[i] = ''.join(a[i])
        
        return " ".join(a)
            
        
            
                