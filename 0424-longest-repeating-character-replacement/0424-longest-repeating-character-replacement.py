class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",                                     "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        
        longest = 0
        
        for i in letters:
            l = r = 0
            cash = k
            length = 0

            while r < len(s):

                if s[r] != i:
                    cash -= 1

                while cash < 0 :
                    if s[l] != i:
                        cash += 1

                    l += 1
                length = max(length, r - l + 1)  

                r += 1
            
            longest = max(length, longest)
            
        
        return longest