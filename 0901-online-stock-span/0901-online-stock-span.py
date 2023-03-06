class StockSpanner:

    def __init__(self):
        
        self.stock = []
        

    def next(self, price: int) -> int:
        
        score = 1
        
        while self.stock and self.stock[-1][0] <= price:
            temp =  self.stock.pop()
            score += temp[1]
            
        self.stock.append((price, score))
        
        
        return score
            
        
        
        
        
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)