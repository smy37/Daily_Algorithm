from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        answer = nums[0]

        while left <= right:
            mid = (left+right)//2
            answer = min(answer, nums[mid])

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid-1

        return answer


if __name__ == "__main__":
    nums = [2,2,2,0,1]
    sol = Solution()
    print(sol.findMin(nums))