class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        largest = 0
        baskets = defaultdict(int)
        while j < len(fruits):
            while j < len(fruits) and  len(baskets) < 2:
                baskets[fruits[j]] += 1 
                j += 1

            while j < len(fruits) and fruits[j] in baskets:
                baskets[fruits[j]] += 1
                j += 1
                
            largest = max(largest, j - i)
            
            if j < len(fruits):
                while i < j - 1 and len(baskets) == 2:
                    baskets[fruits[i]] -= 1
                    if baskets[fruits[i]] == 0:
                        del baskets[fruits[i]]
                    i += 1
                 
                # baskets[fruits[j]] += 1
                
        return largest