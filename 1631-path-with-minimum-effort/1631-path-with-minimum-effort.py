class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        queue={(0,0):0}
        seen={(0,0):0}
        ans=inf
        while queue:
            newqueue={}
            for (i,j),h in queue.items():
                if i==(m-1) and j==(n-1):
                    ans=min(ans,h)
                for x,y in (i-1,j),(i,j-1),(i,j+1),(i+1,j):
                    if 0<=x<m and 0<=y<n:
                        hi=max(h,abs(heights[i][j]-heights[x][y]))

                        if hi<seen.get((x,y),inf):
                            seen[(x,y)]=hi
                            newqueue[(x,y)]=hi
            queue=newqueue
        return ans   