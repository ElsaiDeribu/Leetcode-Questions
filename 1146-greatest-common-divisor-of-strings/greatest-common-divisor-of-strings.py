class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        largest = str1
        smallest = str2

        if len(str1) < len(str2):
            largest = str2
            smallest = str1

        for i in range(len(smallest) - 1, -1, -1):
            
            if len(smallest) % (i + 1) or len(largest) % (i + 1):
                continue

            res1 = int(len(smallest) / (i + 1))
            res2 = int(len(largest) / (i + 1))

            temp = smallest[:i + 1]
          
            if (temp * res1) == smallest and (temp * res2) == largest:
                return temp

        return ''
        