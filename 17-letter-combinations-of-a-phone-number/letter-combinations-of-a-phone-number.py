class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}


        ans = []
        comb = []

        def dfs(idx):

            if idx == len(digits):
                ans.append(''.join(comb.copy())) if comb else None
                return

            
            for l in map[digits[idx]]:
                comb.append(l)
                dfs(idx + 1)
                comb.pop()


        dfs(0)

        return ans