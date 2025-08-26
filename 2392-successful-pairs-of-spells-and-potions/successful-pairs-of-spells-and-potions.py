class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()

      

        for i in range(len(spells)):

            idx = bisect_left(potions, success/spells[i])
            spells[i] = len(potions) - idx

        return spells





        