class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        def check_edge(a, b, graph):
            if b not in graph[a]:
                return False
            return True

        graph = {i: {} for i in range(1, n + 1)}

        for a, b in edges:
            graph[a][b] = True
            graph[b][a] = True

        odd_list = []

        for n in graph:
            if len(graph[n]) % 2 != 0:
                odd_list.append(n)

        print(odd_list)
        if len(odd_list) in [1, 3] or len(odd_list) > 5:
            return False

        elif len(odd_list) == 2:
            if not check_edge(odd_list[0], odd_list[1], graph):
                return True
            else:
                for i in range(1, n + 1):
                    if odd_list[0] != i and i not in graph[odd_list[0]]:
                        if i not in graph[odd_list[1]]:
                            return True
                return False
        elif len(odd_list) == 4:
            if not check_edge(odd_list[0], odd_list[1], graph) and not check_edge(odd_list[2], odd_list[3], graph):
                return True
            if not check_edge(odd_list[0], odd_list[2], graph) and not check_edge(odd_list[1], odd_list[3], graph):
                return True
            if not check_edge(odd_list[0], odd_list[3], graph) and not check_edge(odd_list[1], odd_list[2], graph):
                return True
            return False
        else:
            return True