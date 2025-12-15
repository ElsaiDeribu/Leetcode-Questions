class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        letter_comb = {"2":"abc", "3": "def", "4": "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = []

        def dfs(comb, idx):
            if len(comb) == len(digits):
                ans.append(''.join(comb))
                return

            for letter in letter_comb[digits[idx]]:
                dfs(comb + [letter], idx + 1)


        dfs([], 0)

        return ans
            
        