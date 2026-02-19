class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l, r = 0, len(letters)

        while l < r:

            m = (l + r) // 2

            if letters[m] <= target:
                l = m + 1

            else:
                r = m

        if l < len(letters):
            return letters[l]

        return letters[0]
        