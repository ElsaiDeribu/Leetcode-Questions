class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        r_b = []
        ans = 0

        for row in bank:
            total = sum(int(s) for s in row)
            r_b.append(total) if total else None

        for i in range(1,len(r_b)):
            ans += r_b[i - 1] * r_b[i]


        return ans


        
        