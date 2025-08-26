class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        count = Counter(nums)
        ans = 0

        for key in count.keys():
            
            cand = k - key

            if count[cand] and count[key]:

                if cand == key:
                    temp = count[cand] // 2
                    ans += temp
                    count[cand] -= temp * 2

                elif count[cand] > count[key]:
                    ans +=  count[key]
                    count[cand] -= count[key]
                    count[key] = 0
                else:
                    ans += count[cand]
                    count[key] -= count[cand]
                    count[cand] = 0

        return ans

        