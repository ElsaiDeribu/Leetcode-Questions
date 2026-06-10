class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        freq_groups = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            freq_groups[freq].append(num)

        
        ans = []

        for i in range(len(freq_groups) - 1, -1, -1):

            for num in freq_groups[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans



        