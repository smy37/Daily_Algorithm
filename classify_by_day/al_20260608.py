# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def update_graph(graph):
            def delete_node(parent, cur):
                while cur.left:
                    parent = cur
                    cur = cur.left

                val = cur.val

                if parent:
                    parent.left = cur.right
                else:
                    graph.right = cur.right

                return val

            if not graph.left and not graph.right:
                return None

            elif not graph.left:
                return graph.right

            elif not graph.right:
                return graph.left

            else:
                val = delete_node(None, graph.right)
                graph.val = val
                return graph

        cur = root
        parent = None

        while cur:
            if cur.val == key:
                sub_graph = update_graph(cur)

                if parent is None:
                    return sub_graph

                if parent.left == cur:
                    parent.left = sub_graph

                elif parent.right == cur:
                    parent.right = sub_graph

                return root

            parent = cur

            if cur.val > key:
                cur = cur.left

            elif cur.val < key:
                cur = cur.right

        return root
