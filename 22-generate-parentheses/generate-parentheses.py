class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        comb = []
        ans = []

        def dfs(left, right):
            if len(comb) / 2 == n:
                ans.append(''.join(comb))
                return


            if left > right:
                if left < n:
                    comb.append("(")
                    dfs(left + 1, right)
                    comb.pop()

                comb.append(")")                    
                dfs(left, right + 1)
                comb.pop()

            else:
                comb.append("(")
                dfs(left + 1, right)
                comb.pop()

        dfs(0,0)    
        
        return ans

