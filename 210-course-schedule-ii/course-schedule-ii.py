class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_lst = defaultdict(list)
        pre_count = defaultdict(int)
        deq = deque([])
        order = []

        for crs, pre in prerequisites:
            adj_lst[pre].append(crs)
            pre_count[crs] += 1

        for crs in range(numCourses):
            if pre_count[crs] == 0:
                deq.append(crs)

        
        while deq:

            pre = deq.popleft()
            order.append(pre)

            for crs in adj_lst[pre]:
                pre_count[crs] -= 1
                if pre_count[crs] == 0:
                    deq.append(crs)



        return order if len(order) == numCourses else []
        