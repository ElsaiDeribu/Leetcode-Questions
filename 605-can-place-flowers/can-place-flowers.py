class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed.append(0)
        flowerbed.insert(0, 0)

        for i in range(1, len(flowerbed) - 1):

            prev = i - 1
            curr = i
            next = i + 1

            if flowerbed[prev] ==  flowerbed[curr] ==  flowerbed[next] == 0:
                flowerbed[i] = 1
                n -= 1

        return True if n <= 0 else False        
        