class Solution:
    def isHappy(self, n: int) -> bool:

        look_up = defaultdict(int)

        while look_up[n] <= 1:

            n = str(n)
            total = 0

            for s in n:
                total += int(s) ** 2

            if total == 1:
                return True

            look_up[total] += 1

            n = total

        return False

            




        