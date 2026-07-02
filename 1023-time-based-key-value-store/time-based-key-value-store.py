class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        l, r = 0, len(self.dic[key]) - 1

        while l <= r:
            m = (l + r) // 2

            if self.dic[key][m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1

        if l == 0 and self.dic[key][l][0] > timestamp:
            return ''


        return self.dic[key][l - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)