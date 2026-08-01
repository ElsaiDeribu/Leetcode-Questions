class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # ans = []
        # path = []

        # def dfs(start):
        #     if len(path) == k:
        #         ans.append(path[:])
        #         return

        #     for idx in range(start, n + 1):
        #         path.append(idx)
        #         dfs(idx + 1)
        #         path.pop()

        # dfs(1)

        # return ans
        
        ans = []
        path = []

        def dfs(idx):
            
            if len(path) == k:
                ans.append(path[:])
                return
           
            if idx > n: return

            # take
            path.append(idx)
            dfs(idx + 1)
            path.pop()

            # not take
            dfs(idx + 1)

        dfs(1)

        return ans