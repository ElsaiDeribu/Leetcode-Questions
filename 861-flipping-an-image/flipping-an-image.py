class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:


        for r in range(len(image)):
            image[r] = image[r][::-1]
            for c in range(len(image[0])):
                if image[r][c] == 1:
                   image[r][c] = 0
                else:
                    image[r][c] = 1


        return image
        