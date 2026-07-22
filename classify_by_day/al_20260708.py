from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        n_list = [i for i in range(1, n + 1)]

        def dfs(num_list):
            if len(num_list) == 0:
                return [None]
            temp_list = []
            for k in range(len(num_list)):

                left_list = num_list[:k]
                right_list = num_list[k + 1:]

                left_list = dfs(left_list)
                right_list = dfs(right_list)

                for i in range(len(left_list)):
                    for j in range(len(right_list)):
                        node = TreeNode(num_list[k], left_list[i], right_list[j])
                        temp_list.append(node)

            return temp_list

        answer = dfs(n_list)
        return answer

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateTrees(3))