class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        n = len(image[0])
        for row in image:
            for c in range((n + 1)// 2):
                row[c], row[n - 1 - c] = 1 - row[n - 1 - c],  1 - row[c]


        return image
        