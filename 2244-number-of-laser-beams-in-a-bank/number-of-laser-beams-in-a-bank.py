class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        ans, prev = 0, 0

        for row in bank:
            total = row.count('1')

            if total:
                ans += total * prev
                prev = total



        return ans


        
        