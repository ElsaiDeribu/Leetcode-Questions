class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def recur(total, res):
            if total == target:
                ans.append(res.copy())

            if total > target:
                return

            for num in candidates:
                recur(total + num, res + [num])

        recur(0, [])

        res = set()

        for item in ans:
            res.add(tuple(sorted(Counter(item).items())))

        ans = []

        for tp in res:
            temp = []
            for val, freq in tp:
                temp += ([val] * freq)

            ans.append(temp)

        return ans



