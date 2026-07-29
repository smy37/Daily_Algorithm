class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if (x1 <= xCenter <= x2 and y1-radius <= yCenter <= y2 + radius):
            return True

        if (y1 <= yCenter <= y2 and x1-radius <= xCenter <= x2+radius):
            return True
        
        d1 = (xCenter-x1)**2 + (yCenter-y1)**2
        d2 = (xCenter-x1)**2 + (yCenter-y2)**2
        d3 = (xCenter-x2)**2 + (yCenter-y1)**2
        d4 = (xCenter-x2)**2 + (yCenter-y2)**2
        
        if min(d1, d2, d3, d4) <= radius**2:
            return True
        
        return False
