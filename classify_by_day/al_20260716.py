import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x_c = x_center
        self.y_c = y_center

    def randPoint(self) -> List[float]:
        dist = random.uniform(-self.r, self.r)
        angle = random.uniform(0, 2*math.pi)
        

        x = math.cos(angle)
        y = math.sin(angle)

        return [angle*dist, angle*dist]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
