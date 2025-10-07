class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack):
            return -1


        l = 0

        for r in range(len(haystack)):

            if r - l + 1 > len(needle):
                l += 1

            if r - l + 1 == len(needle):
                if haystack[l:r + 1] == needle:
                    return l

        return -1


        