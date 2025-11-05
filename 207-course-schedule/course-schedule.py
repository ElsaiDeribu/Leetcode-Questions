class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        pre_count = defaultdict(int)
        deq = deque([])
        order = []


        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
            pre_count[crs] += 1

        for crs in range(numCourses):
            if pre_count[crs] == 0:
                deq.append(crs)


        while deq:

            pre = deq.popleft()
            order.append(pre)

            for crs in adj_list[pre]:
                pre_count[crs] -= 1
                if pre_count[crs] == 0:
                    deq.append(crs)

        return len(order) == numCourses
        