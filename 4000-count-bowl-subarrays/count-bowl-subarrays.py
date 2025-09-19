class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:

        st = []
        ans = 0

        for i, num in enumerate(nums):
            print()

            while st and st[-1][0] < num:
                val, idx = st.pop()
                if i - idx > 1:
                    ans += 1
                    
            if st:
                val, idx = st[-1]
                if i - idx > 1:
                    ans += 1

            st.append((num, i))

        return ans 



        