class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def find(x, parent):
            if x == parent[x]:
                return x
            parent_x = find(parent[x], parent)
            parent[x] = parent_x
            return parent[x]

        def union(a, b, parent):
            parent_a = find(a, parent)
            parent_b = find(b, parent)

            if parent_a <= parent_b:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b


        success_list = [False for _ in range(len(requests))]
        parent_dict = {i : i for i in range(n)}
        group_num_to_member = {i: set() for i in range(n)}

        ban_dict = {}
        for x, y in restrictions:
            ban_dict[(min(x, y), max(x, y))] = True


        for i in range(len(requests)):
            x, y = requests[i]
            parent_x = find(x, parent_dict)
            parent_y = find(y, parent_dict)

            flag = True

            for m in list(group_num_to_member[parent_x]) + [x]:
                for n in list(group_num_to_member[parent_y]) + [y]:
                    if (min(m, n), max(m,n)) in ban_dict:
                        flag = False
                        break

            if (min(x, y), max(x, y)) in ban_dict:
                flag = False

            if flag:
                union(x, y, parent_dict)
                p_x = find(x, parent_dict)
                group_num_to_member[p_x] |= group_num_to_member[parent_x]
                group_num_to_member[p_x] |= group_num_to_member[parent_y]
                group_num_to_member[p_x].add(x)
                group_num_to_member[p_x].add(y)
                success_list[i] = True

        return success_listclass Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def find(x, parent):
            if x == parent[x]:
                return x
            parent_x = find(parent[x], parent)
            parent[x] = parent_x
            return parent[x]

        def union(a, b, parent):
            parent_a = find(a, parent)
            parent_b = find(b, parent)

            if parent_a <= parent_b:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b


        success_list = [False for _ in range(len(requests))]
        parent_dict = {i : i for i in range(n)}
        group_num_to_member = {i: set() for i in range(n)}

        ban_dict = {}
        for x, y in restrictions:
            ban_dict[(min(x, y), max(x, y))] = True


        for i in range(len(requests)):
            x, y = requests[i]
            parent_x = find(x, parent_dict)
            parent_y = find(y, parent_dict)

            flag = True

            for m in list(group_num_to_member[parent_x]) + [x]:
                for n in list(group_num_to_member[parent_y]) + [y]:
                    if (min(m, n), max(m,n)) in ban_dict:
                        flag = False
                        break

            if (min(x, y), max(x, y)) in ban_dict:
                flag = False

            if flag:
                union(x, y, parent_dict)
                p_x = find(x, parent_dict)
                group_num_to_member[p_x] |= group_num_to_member[parent_x]
                group_num_to_member[p_x] |= group_num_to_member[parent_y]
                group_num_to_member[p_x].add(x)
                group_num_to_member[p_x].add(y)
                success_list[i] = True

        return success_list