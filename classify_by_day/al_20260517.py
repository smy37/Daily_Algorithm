class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = {}

        for s, e in edges:
            in_degree[e] = s

        answer = [i for i in range(n) if i not in in_degree]

        return answer