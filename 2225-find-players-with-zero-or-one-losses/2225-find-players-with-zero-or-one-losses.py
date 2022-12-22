class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        wins = defaultdict(int)
        gamesPlayed = defaultdict(int)
        ans0 = []
        ans1 = []
        for match in matches:
            wins[match[0]] += 1
            gamesPlayed[match[0]] += 1
            gamesPlayed[match[1]] += 1
            
        for player in gamesPlayed:
            if gamesPlayed[player] == wins[player]:
                ans0.append(player)
            elif gamesPlayed[player] == wins[player] + 1:
                ans1.append(player)
        
        
        
        return [sorted(ans0), sorted(ans1)]