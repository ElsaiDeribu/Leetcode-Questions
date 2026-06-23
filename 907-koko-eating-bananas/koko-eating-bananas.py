class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        left, right = 1, max(piles)


        def calc_time(rate):
            time_taken = 0
            # time(hr) = pile(b)/rate(b/hr)
            for pile in piles:
                time_taken += math.ceil(pile/rate)

            return time_taken


        while left <= right:
            mid = (left + right) // 2

            if calc_time(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1



        return left

        