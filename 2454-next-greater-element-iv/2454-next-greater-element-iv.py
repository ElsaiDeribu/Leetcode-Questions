class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:

        nextSecondGreatest = defaultdict(int)
        st = []
        secondSt = []
        temp = []

        for i in range(len(nums)):

            while secondSt and secondSt[-1][0] < nums[i]:
                number = secondSt.pop()
                nextSecondGreatest[number] = nums[i]

            while st and st[-1][0] < nums[i]:
                number = st.pop()
                temp.append(number)

            secondSt.extend(temp[::-1])
            temp = []
            st.append((nums[i],i))


        for i in range(len(nums)):
            if (nums[i], i) in nextSecondGreatest:
                nums[i] = nextSecondGreatest[(nums[i], i)]
            else:
                nums[i] = -1


        return nums




      