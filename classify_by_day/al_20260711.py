"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
import math

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        val_list = []
        dq = deque()

        if root is not None:
            dq.append(root)
        
        while dq:
            cur = dq.popleft()
            val_list.append(cur)

            if cur.left is not None:
                dq.append(cur.left)
            if cur.right is not None:
                dq.append(cur.right)
        
        height = int(math.log2((len(val_list)+1)))
        idx = -1
        
        for i in range(height):
            for j in range(2**i):
                idx += 1
                
                if j < 2**i-1:
                    
                    val_list[idx].next = val_list[idx+1]
        
        return val_list[0] if len(val_list) > 0 else None
            
