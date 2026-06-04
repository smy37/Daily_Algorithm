
Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = {}
        child_list = {}
        for p, c, b_left in descriptions:
            if p not in graph:
                graph[p] = [-1, -1]

            if b_left:
                graph[p][0] = c
            else:
                graph[p][1] = c
            child_list[c] = True

        parent = None
        for p in graph:
            if p not in child_list:
                parent = p
                break
        def dfs(s):
            cur = s.pop()
            left = None
            right = None

            if cur in graph:
                next_nodes = graph[cur]

                left_node = next_nodes[0]
                right_node = next_nodes[1]

                if left_node != -1 :
                    left = dfs(s+[left_node])

                if right_node != -1:
                    right = dfs(s+[right_node])
            
            return TreeNode(cur, left, right)

        answer = dfs([parent])

        return answer
