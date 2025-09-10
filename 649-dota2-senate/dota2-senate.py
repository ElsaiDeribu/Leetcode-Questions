class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rad, dr = deque(), deque()
        n = len(senate)

        for i, v in enumerate(senate):
            if v == "R":
                rad.append(i)
            else:
                dr.append(i)


        while rad and dr:

            ri, di = rad.popleft(), dr.popleft()

            if ri < di:
                rad.append(n + ri)
            else:
                dr.append(n + di)

        
        return "Radiant" if rad else "Dire"


