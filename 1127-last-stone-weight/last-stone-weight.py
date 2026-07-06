class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for idx, val in enumerate(stones):
            stones[idx] = -val


        heapify(stones)

        while len(stones) > 1:
            large = -heappop(stones)
            small = -heappop(stones)

            if large != small:

                ans = max(large, small) - min(large, small)

                heappush(stones, -ans)

        if len(stones) == 1:
            return -stones[0]

        return 0



        