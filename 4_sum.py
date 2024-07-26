from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to use the two-pointer technique
        quadruplets = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicate elements
                
                left, right = j + 1, len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # Skip duplicate elements
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # Skip duplicate elements
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1  # Move left pointer to the right
                    else:
                        right -= 1  # Move right pointer to the left

        return quadruplets
