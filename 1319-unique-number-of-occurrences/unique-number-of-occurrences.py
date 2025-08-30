class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count = Counter(arr)
        occ = set()


        for _ , val in count.items():
            if val in occ:
                return False
            else:
                occ.add(val)


        return True

        