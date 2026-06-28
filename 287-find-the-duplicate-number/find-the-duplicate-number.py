class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # 0 → nums[0] → nums[nums[0]] → ...
        # slow = 0
        # fast = 0

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        curr = 0
        while curr != slow:
            curr = nums[curr]
            slow = nums[slow]

        return curr