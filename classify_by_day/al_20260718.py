class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def product(node1, node2):
            return node1[0]*node2[0]+node1[1]*node2[1]

        node_list = [p1, p2, p3, p4]
        node_list.sort(key = lambda x : [x[0], x[1]])

        n1, n2, n4, n3 = node_list

        v1 = [n1[0]-n2[0], n1[1]-n2[1]]
        v2 = [n2[0]-n3[0], n2[1]-n3[1]]
        v3 = [n3[0]-n4[0], n3[1]-n4[1]]
        v4 = [n4[0]-n1[0], n4[1]-n1[1]]

        if product(v1, v2) == 0 and product(v2, v3) == 0 \
        and product(v3, v4) == 0 and product(v4, v1) == 0 and \
        (v1[0]**2+v1[1]**2)==(v2[0]**2+v2[1]**2) and v1[0]**2+v1[1]**2 != 0:
            return True
        else: 
            return False
