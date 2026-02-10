class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:

        st = []

        for num in nums:
            if not st:
                st.append(num)

            else:
                curr = num
                
                while st and st[-1] == curr:
                    temp = st.pop()
                    temp += curr
                    curr = temp

                st.append(curr)

        return st

            
        