class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rad = deque()
        dr = deque()
        n = len(senate)

        for i, v in enumerate(senate):
            if v == "R":
                rad.append((v,i))
            else:
                dr.append((v,i))


        while rad and dr:

            r, ri = rad.popleft()
            d, di = dr.popleft()

            if ri < di:
                rad.append((r, n + ri))
            else:
                dr.append((d, n + di))

        if rad:
            return "Radiant"

        return "Dire"


