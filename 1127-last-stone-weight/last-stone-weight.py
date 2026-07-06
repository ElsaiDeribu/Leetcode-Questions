class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        # TC: O(nlogn)
        # SC: O(n)
        for idx, val in enumerate(stones):
            stones[idx] = -val


        heapify(stones)

        while len(stones) > 1:
            large = -heappop(stones)
            small = -heappop(stones)

            if large != small:
                heappush(stones, -(large - small))

        if len(stones) == 1:
            return -stones[0]

        return 0



        