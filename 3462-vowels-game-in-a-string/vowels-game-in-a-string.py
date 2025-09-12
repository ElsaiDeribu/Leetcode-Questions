class Solution:
    def doesAliceWin(self, s: str) -> bool:


        vowels = ["a","e", "i", "o", "u"]

        for l in s:
            if l in vowels:
                return True

        return False

        

        