from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) ==1: return 1
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a

        def normalize_line(x1, y1, x2, y2):
            A = y1-y2
            B = x2-x1
            C = x1*y2-x2*y1

            g = gcd(gcd(A, B), C)

            if g!= 0:
                A //= g
                B //= g
                C //= g

            if A <0 or (A == 0 and B <0) or (A == 0 and B == 0 and C <0):
                A *= -1
                B *= -1
                C *= -1

            return A, B, C


        memory = {}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                a, b, c = normalize_line(x1, y1, x2, y2)
                if (a, b, c) not in memory:
                    memory[(a,b,c)] = {}

                memory[(a, b, c)][(x1, y1)] = True
                memory[(a, b, c)][(x2, y2)] = True

        answer = 0
        for abc in memory:
            answer = max(answer, len(memory[abc]))

        return answer
        
