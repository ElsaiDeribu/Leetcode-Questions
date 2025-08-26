class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st = []

        for num in asteroids:
            while st and st[-1] > 0 and num < 0:
                if st[-1] < -num:   
                    st.pop()
                    continue
                elif st[-1] == -num: 
                    st.pop()
                break
            else:
                st.append(num)

        return st      

            
                    

