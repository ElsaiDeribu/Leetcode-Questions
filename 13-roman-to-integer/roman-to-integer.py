class Solution:
    def romanToInt(self, s: str) -> int:
        
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


        ans = []

        for item in s:
            ans.append(dic[item])


        for i in range(len(s) - 2, -1, -1):
            if ans[i] < ans[i + 1]:
                ans[i + 1] -= ans[i]
                ans[i] = 0

        return sum(ans)
            

            
