class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        res = sorted(list(zip(position, speed)))
        
        for idx, (pos, s) in enumerate(res):
            res[idx] = (target - pos) / s

        st = []
        for time in res:
            while st and st[-1] <= time:
                st.pop()
            st.append(time)

        return len(st)