class StockSpanner:

    def __init__(self):
        self.st = []
        

    def next(self, price: int) -> int:

        count = 1

        while self.st and self.st[-1][0] <= price:

            _, c = self.st.pop()
            count += c

        self.st.append((price, count))

        return count

        



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)