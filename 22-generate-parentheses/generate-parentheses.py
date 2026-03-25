class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        comb = []
        ans = []

        def dfs(opn, close):
            
            if opn == close == n:
                ans.append(''.join(comb))
                return

            if opn < n:
                comb.append("(")
                dfs(opn + 1, close)
                comb.pop()

            if opn > close:
                comb.append(")")                    
                dfs(opn, close + 1)
                comb.pop()


        dfs(0,0)    

        return ans

