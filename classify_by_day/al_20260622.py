class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        p = [i for i in range(n)]

        def find(i, parent):
            if i == parent[i]:
                return i
            parent[i] = find(parent[i], parent)
            return parent[i]

        def union(i, j, parent):
            parent_i = find(i, parent)
            parent_j = find(j, parent)

            if parent_i != parent_j:
                parent[parent_i] = parent_j
                return True
            return False

        edges_with_idx = [(u, v, w, i) for i, (u,v,w) in enumerate(edges)]
        edges_with_idx.sort(key = lambda x : x[2])
        mst_cost = 0

        for u, v, w, _ in edges_with_idx:
            if union(u, v, p):
                mst_cost += w


        mst_list = []
        def dfs(cur_edge_idx, cur_edge_list, cur_weight_sum, parent):
            if len(cur_edge_list) == n-1:
                mst_list.append(set(cur_edge_list.keys()))
                return

            snapshot = parent[:]
            for i in range(cur_edge_idx, len(edges_with_idx)):
                u, v, w, idx = edges_with_idx[i]
                if i not in cur_edge_list and cur_weight_sum + w <= mst_cost and union(u, v, parent):
                    cur_edge_list[idx] = True
                    dfs(i, cur_edge_list, cur_weight_sum+w, parent)
                    del cur_edge_list[idx]
                    parent[:] = snapshot

        dfs(0, {}, 0, [i for i in range(n)])

        common = set.intersection(*mst_list)
        uncommon = set.union(*mst_list)-common

        return [list(common), list(uncommon)]
