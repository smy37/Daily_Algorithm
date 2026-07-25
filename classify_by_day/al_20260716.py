import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x_c = x_center
        self.y_c = y_center

    def randPoint(self) -> List[float]:
        dist = self.r*math.sqrt(random.uniform(0, 1))
        angle = random.uniform(0, 2*math.pi)
        

        x = math.cos(angle)*dist
        y = math.sin(angle)*dist

        return [x+self.x_c, y+self.y_c]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
