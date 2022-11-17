class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        prefixes = [0] * (n + 1)
        
        
        for i in range(len(bookings)):
            prefixes[bookings[i][0] - 1] += bookings[i][2]
            prefixes[bookings[i][1]] -= bookings[i][2]
        
        for i in range(1, len(prefixes)):
            prefixes[i] = prefixes[i - 1] + prefixes[i]
        
        return prefixes[:-1]