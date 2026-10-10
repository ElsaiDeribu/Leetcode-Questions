class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        ans = []
        shortest = min(strs, key=lambda x: len(x))

        for i in range(len(shortest)):
            for j in range(len(strs)):
                if strs[j][i] != shortest[i]:
                    return ''.join(ans)

            ans.append(shortest[i])


        return ''.join(ans)



        