class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        ans = 0 
        prev = 0

        for i in range(len(bank)):
            total = sum(int(s) for s in bank[i])

            if prev and total:

                ans += total * prev
                prev = total

            elif total:
                prev = total


        return ans


        
        