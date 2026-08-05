from collections import deque
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        answer = set()
        stack = []

        def dfs(s, visit):
            if len(s) == len(nums):
                answer.add(tuple(s))
                return

            for i in range(len(nums)):
                if i not in visit:
                    visit[i] = True
                    dfs(s+[nums[i]], visit)
                    del visit[i]
        dfs(stack, {})
        return list(answer)
            

