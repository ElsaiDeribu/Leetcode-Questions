class Solution:
    def isHappy(self, n: int) -> bool:

        look_up = set()

        while True:

            n = str(n)
            total = 0

            for s in n:
                total += int(s) ** 2

            if total == 1:
                return True

            if total in look_up:
                return False

            look_up.add(total)

            n = total

        return False

            




        