class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()

        def check(s):

            l = 0
            r = len(potions) - 1

            while l <= r:

                m = (l + r) // 2

                if potions[m] *  s < success:
                    l = m + 1
                else:
                    r = m - 1

            return l


        for i in range(len(spells)):

            idx = check(spells[i])
            spells[i] = len(potions) - idx

        return spells





        