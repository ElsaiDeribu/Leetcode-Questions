class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
            
        total = numBottles
        emptyBottles = numBottles

        while numBottles >= numExchange:

            numBottles -= numExchange
            numExchange += 1
            numBottles += 1
            total += 1


        return total

