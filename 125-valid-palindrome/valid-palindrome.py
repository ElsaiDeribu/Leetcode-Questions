class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            if not s[l].isalnum():
                l += 1

            elif not s[r].isalnum():
                r -= 1

            elif s[r].lower() != s[l].lower():

                return False

            else:
                l += 1
                r -= 1



        return True
        