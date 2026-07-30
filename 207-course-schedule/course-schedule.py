class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_count = defaultdict(int)
        pre_list = defaultdict(list)
        deq = deque([])
        order = []

        for crs, pre in prerequisites:
            pre_count[crs] += 1
            pre_list[pre].append(crs)

        
        for crs in range(numCourses):
            if pre_count[crs] == 0:
                deq.append(crs)


        while deq:

            pre = deq.popleft()
            order.append(pre)

            for crs in pre_list[pre]:
                pre_count[crs] -= 1
                if pre_count[crs] == 0:
                    deq.append(crs)



        return len(order) == numCourses




        

