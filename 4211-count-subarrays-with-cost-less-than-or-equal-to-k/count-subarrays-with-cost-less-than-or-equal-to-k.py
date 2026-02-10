class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        min_q = deque() # increasing
        max_q = deque() # decreasing
        ans = 0
        l = 0

        for r in range(len(nums)):

            # add to min
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()

            min_q.append(nums[r])

            # add to max
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()

            max_q.append(nums[r])


            while (max_q[0] - min_q[0]) * (r - l + 1) > k:

                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                
                l += 1        

            ans += r - l + 1
            
        return ans
        