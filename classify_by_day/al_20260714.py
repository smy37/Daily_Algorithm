class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s1 = (ax2 - ax1) * (ay2 - ay1)
        s2 = (bx2 - bx1) * (by2 - by1)
        s = s1+s2
        if not (ax2 <= bx1 or ax1 >= bx2 or ay1 >= by2 or ay2 <=by1):
            s3 = (min(ax2, bx2) -max(ax1, bx1))* (min(ay2, by2)-max(ay1, by1))
            s -= s3

        return s
