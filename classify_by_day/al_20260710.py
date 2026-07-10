class Solution:
    def countAndSay(self, n: int) -> str:
        cur = "1"
        for _ in range(n-1):
            new = ""
            
            temp = cur[0]
            cnt = 0
            for j in range(len(cur)):
                
                if cur[j] == temp:
                    cnt += 1
                else:
                    new += f"{cnt}{temp}"
                    cnt = 1
                    temp = cur[j]
            new += f"{cnt}{temp}"
            
            cur = new
        return cur
