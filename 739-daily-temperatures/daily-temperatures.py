class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        st = []
        ans = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):

            while st and temperatures[st[-1]] < temp:
                i = st.pop()
                ans[i] = idx - i

            st.append(idx)

        return ans


        

