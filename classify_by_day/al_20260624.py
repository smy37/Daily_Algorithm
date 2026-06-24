class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memory = {}
        for n in nums:
            if n not in memory:
                memory[n] = 1
            else:
                if memory[n] == 2:
                    del memory[n]
                else:
                    memory[n] += 1

        answer = list(memory.keys())[0]

        return answer