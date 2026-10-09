class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        st = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while st and st[-1][1] < temperatures[i]:
                idx, val = st.pop()
                days = i - idx
                ans[idx] = days

            st.append((i, temperatures[i]))


        return ans


        

