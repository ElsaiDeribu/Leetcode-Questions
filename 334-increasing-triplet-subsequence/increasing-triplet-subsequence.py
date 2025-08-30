class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        trip = [float("inf"), float("inf")]


        for n in nums:

            if n <= trip[0]:
                trip[0] = n

            elif n <= trip[1]:
                trip[1] = n

            else:
                return True


        return False
        