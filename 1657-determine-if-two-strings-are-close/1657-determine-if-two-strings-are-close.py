class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        
        count1 = Counter(word1)
        count2 = Counter(word2)

        freq1 = sorted([val for _, val in count1.items()])
        freq2 = sorted([val for _, val in count2.items()])
        
        letters1 = sorted([key for key, _ in count1.items()])
        letters2 = sorted([key for key, _ in count2.items()])
        
#         print(letters1)
#         print(letters2)
        
#         print(freq1)
#         print(freq2)
            
        return freq1 == freq2 and letters1 == letters2
    
