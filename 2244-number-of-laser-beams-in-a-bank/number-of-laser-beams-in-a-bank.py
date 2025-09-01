class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        ans = 0 
        prev = 0

        for i in range(len(bank)):
            total = 0

            for n in bank[i]:
                total += int(n)

            if prev and total:

                ans += total * prev
                prev = total

            elif total:
                prev = total


        return ans


        
        