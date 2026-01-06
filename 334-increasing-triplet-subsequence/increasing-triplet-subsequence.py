class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        i = j = k = float("inf")

        for n in nums:
            if n <= i:
                i = n

            elif n <= j:
                j = n

            else:
                k = n

        if i == float("inf") or j == float("inf") or k == float("inf"):
            return False

        return True

        