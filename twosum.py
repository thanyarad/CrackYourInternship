from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        
        return [] 


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  
print(solution.twoSum([3, 2, 4], 6))       
print(solution.twoSum([3, 3], 6))  
