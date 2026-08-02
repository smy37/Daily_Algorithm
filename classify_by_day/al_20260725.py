class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ## 1.
        # return str(int(num1)*int(num2))

        ## 2.
        # num_dict = {}
        # for i in range(0, 10):
        #     num_dict[str(i)] = i

        # arr = [0, 0]

        # for i in range(len(num1)):
        #     arr[0] = arr[0] + num_dict[num1[i]]*(10**(len(num1)-i-1))

        # for i in range(len(num2)):
        #     arr[1] = arr[1] + num_dict[num2[i]]*(10**(len(num2)-i-1))
        
        # return str(arr[0]*arr[1])

        ## 3. 
        # num_dict = {}
        # for i in range(0, 10):
        #     num_dict[str(i)] = i
        
        # answer = [0 for _ in range(len(num1)*len(num2))]
        # for i in range(len(num1)):
        #     for j in range(len(num2)):
        #         answer[i*len(num1)+j] = num_dict[num1[i]]*num_dict[num2[j]]*(10**(len(num1)-1-i))*(10**(len(num2)-1-j))
        
        # return str(sum(answer))

        ## 4. 
        answer = [0]*(len(num1)+len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                value = int(num1[i])*int(num2[j])

                low = i+j+1
                high = i+j
                total = answer[low] + value
                answer[low] = total%10
                answer[high] += total//10
                
        answer =  "".join([str(i) for i in answer]).lstrip("0")

        return answer if answer else "0"
