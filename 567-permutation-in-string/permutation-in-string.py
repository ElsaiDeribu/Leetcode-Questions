class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        window, wanted = defaultdict(int), Counter(s1)
        matches = 0
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            window[c] += 1

            if c in wanted:
                if window[c] == wanted[c]:
                    matches += 1
                elif window[c] == wanted[c] + 1:
                    matches -= 1

            while r - l + 1 > len(s1):

                c = s2[l]
                if c in wanted:
                    if window[c] == wanted[c]:
                        matches -= 1
                    elif window[c] == wanted[c] + 1:
                        matches += 1

                window[c] -= 1
                l += 1


            if matches == len(wanted):
                return True


        return False
