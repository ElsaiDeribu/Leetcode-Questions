class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def check(banana_p_hour):

            hours = 0

            for pile in piles:
                hours += ceil(pile/banana_p_hour)

            return hours


        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2

            if check(m) <= h:
                r = m - 1
            else:
                l = m + 1

        
        return l

        