class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        st = deque()
        ans = []
        l = 0

        for r in range(len(nums)):

            while st and st[-1] < nums[r]:
                st.pop()
            st.append(nums[r])

            while r - l + 1 > k:
                if nums[l] == st[0]:
                    st.popleft()
                l += 1

            if r - l + 1 == k:
                ans.append(st[0])


        return ans