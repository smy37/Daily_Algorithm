class Solution:
    def rotateRight(self, head, k: int):
        num_list = []
        cur = head
        
        while cur:
            num_list.append(cur.val)
            cur = cur.next
        if len(num_list):
            k = k%len(num_list)
        else: return None
        cur_node = None
        for i in range(len(num_list)-k-1, -1, -1):
            cur_node = ListNode(num_list[i], cur_node)

        for i in range(len(num_list)-1, len(num_list)-k-1, -1):
            cur_node = ListNode(num_list[i], cur_node)

        return cur_node
        
