import math

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        memory = set()

        for x_c, y_c, r in circles:
            for x in range(x_c-r, x_c+r+1):
                dx = x - x_c
                dy = math.isqrt(r**2-dx**2)
                for y in range(y_c-dy, y_c+dy+1):
                    memory.add((x, y))

        return len(memory)
