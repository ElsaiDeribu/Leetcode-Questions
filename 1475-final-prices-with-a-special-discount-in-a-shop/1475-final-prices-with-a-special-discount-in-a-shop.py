class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        ans = prices.copy()
        st = []
        
        for i in range(len(prices)):
            
            while st and st[-1][1] >= prices[i]:
                ans[st[-1][0]] = st[-1][1] - prices[i]
                st.pop()
                
            st.append((i, prices[i]))
            
            
        return ans
            