class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
            
        total = numBottles

        while numBottles >= numExchange:

            # exchange bottles
            numBottles -= numExchange
            numBottles += 1

            # drink the exchanged bottle
            total += 1
            
            numExchange += 1



        return total

