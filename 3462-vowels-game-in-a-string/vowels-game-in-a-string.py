class Solution:
    def doesAliceWin(self, s: str) -> bool:


        vowels = ["a","e", "i", "o", "u"]

        c = 0

        for l in s:
            if l in vowels:
                c += 1

        return True if c else False

        

        