class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # disstance_left = (target - position)m / m/s
        pos_speed = sorted([(p, s) for p, s in zip(position, speed)])
        st = []

        for p, s in pos_speed:
            
            distance_left = target - p
            time = distance_left / s

            while st and st[-1] <= time:
                st.pop()

            st.append(time)

        return len(st)