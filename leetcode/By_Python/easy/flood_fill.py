# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-10 15:27:50
# @Last Modified time: 2018-11-10 15:51:40


class Solution:
    four_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def fill_color(self, sr, sc):
        self.image[sr][sc] = self.newColor
        for direction in self.four_direction:
            new_x = sr + direction[0]
            new_y = sc + direction[1]
            if new_x > -1 and new_x < len(self.image) and new_y > -1 and new_y < len(self.image[0]):
                if self.image[new_x][new_y] == self.oldColor:
                    self.fill_color(new_x, new_y)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        self.image = image
        self.newColor = newColor
        self.oldColor = oldColor
        self.fill_color(sr, sc)
        return self.image

if __name__ == '__main__':
    solution = Solution()
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    image = solution.floodFill(image, sr, sc, newColor)
    print(image)
