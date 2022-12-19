class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        strs = sorted(strs)
        for i in range(len(strs[0])):
            common = True
            for j in range(1, len(strs)):
                if i < len(strs[j]) and strs[j][i] != strs[0][i]:
                    common = False
            if common:
                ans += strs[0][i]
            else:
                break
        return ans
                    
            
            