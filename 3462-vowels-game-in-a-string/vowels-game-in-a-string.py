class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowels = {"a", "e", "i", "o", "u"}
        return any(c in vowels for c in s)
