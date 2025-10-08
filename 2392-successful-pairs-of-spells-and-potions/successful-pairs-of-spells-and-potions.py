class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()

        for idx, val in enumerate(spells):
            l = bisect.bisect_left(potions, success / val )
            spells[idx] = len(potions) - l

        return spells
        
        