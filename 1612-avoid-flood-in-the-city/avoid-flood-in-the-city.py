class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = defaultdict(deque)


        for idx, val in enumerate(rains):
            if val != 0:
                dic[val].append(idx)

        
        heap = []
        full = set()

        for idx, val in enumerate(rains):
            if val != 0:
                if val in full:
                    return []

                full.add(val)
                dic[val].popleft()

                if dic[val]:
                    heapq.heappush(heap, (dic[val][0], val))

                rains[idx] = -1

            else:

                if heap:
                    i, v = heapq.heappop(heap)
                    rains[idx] = v
                    full.remove(v)

                else:
                    rains[idx] = 1

        return rains
