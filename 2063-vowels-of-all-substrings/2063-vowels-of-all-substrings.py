class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        
        ans = 0
        
        
        for i in range(len(word)):
            
            if word[i] in vowels:
                
                
                
                r = len(word) - i
                l = i + 1
                
                ans += (l * r)
                
                
        return ans