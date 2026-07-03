class Solution:
    def numDecodings(self, s: str) -> int:
        # import string
        # alpha_list = list(string.ascii_uppercase)
        # num_to_alpha = {}
        # for i in range(len(alpha_list)):
        #     num_to_alpha[str(i+1)] = alpha_list[i]
        # visit = [0 for _ in range(len(s))]
        # global answer
        # answer = 0
        # def dfs(cur_idx):
        #     global answer
        #     if cur_idx >= len(s):
        #         answer += 1
        #         return  
        #     if visit[cur_idx] == 1:
        #         return
        #     else:
        #         visit[cur_idx] = 1
            
        #     if s[cur_idx] == "0": return   
                 
        #     dfs(cur_idx+1)
            
        #     if cur_idx+2 <= len(s) and s[cur_idx:cur_idx+2] in num_to_alpha:
            
        #         dfs(cur_idx+2)
        
        # dfs(0)
        
        # return answer

        memory = [0 for _ in range(len(s)+1)]
        memory[0] = 1
        for i in range(len(s)):
            
            if i+1 <= len(s) and s[i] != "0":
                memory[i+1] += memory[i]
            
            if i+2 <= len(s) and s[i] != "0" and int(s[i:i+2]) <=26:
                memory[i+2] += memory[i]
            

        return memory[-1]
            

