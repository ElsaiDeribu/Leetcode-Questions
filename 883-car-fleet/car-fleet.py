class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        res = sorted(list(zip(position, speed)))
        st = []

        for pos, s in res:

            time = (target - pos) / s
            while st and st[-1] <= time:
                st.pop()
                
            st.append(time)

        return len(st)