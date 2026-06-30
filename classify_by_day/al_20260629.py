# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = True
        answer = []
        if not root:
            return answer
        cur = [root]
        
        while cur:
            temp_answer = []
            next_list = []
            
            if flag:
                for i in range(len(cur)):
                    temp_answer.append(cur[i].val)
                    if cur[i].left:
                        next_list.append(cur[i].left)
                    if cur[i].right:
                        next_list.append(cur[i].right)
                    
            else:
                for i in range(len(cur)-1, -1, -1):
                    temp_answer.append(cur[i].val)
                    if cur[i].right:
                        next_list.append(cur[i].right)
                    if cur[i].left:
                        next_list.append(cur[i].left)
            if temp_answer:
                answer.append(temp_answer)
            cur = next_list[::-1] if not flag else next_list
            
            flag = False if flag else True

        return answer
            
