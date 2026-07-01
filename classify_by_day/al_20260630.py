class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()

        answer = ""
        for i in range(len(s_split)-1, -1, -1):
            answer += s_split[i]+" "
        
        return answer.strip()
