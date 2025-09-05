class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        st = []

        for i in range(len(temperatures)):

            while st and st[-1][1] < temperatures[i]:
                idx, t = st.pop()
                temperatures[idx] = i - idx


            st.append((i, temperatures[i]))


        for i, t in st:
            temperatures[i] = 0

        return temperatures