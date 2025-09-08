class Solution:
    def countBits(self, n: int) -> List[int]:

        def cnt(b):
            return list(b).count("1")


        return [cnt(bin(i)[2:]) for i in range(n + 1)]