class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        ans = 0
        l = 0
        

        for r in range(len(s)):

            if s[r] in vowels:
                count += 1

            if r - l + 1 < k:
                continue


            ans = max(ans, count)

            if s[l] in vowels:
                count -= 1

            l += 1

        return ans

            

        