'''
Four sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class BasicTwoPointer:
    def four_sum(self, nums, target):
        
        if not nums:
            return []
        nums.sort()
        ans = []

        n = len(nums)
        if n <= 4:
            if sum(nums) == target:
                return [nums]
            return []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                left =j+1
                right = n-1
               
                while left < right:
                    add = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if add == target:
                        quad = (nums[i], nums[j], nums[left], nums[right])
                        ans.append(list(quad))

                        while left < right and nums[left] == nums[left +1]:
                            left +=1
                        while left < right and nums[right] == nums[right -1]:
                            right -=1
                        left +=1
                        right -= 1
                    elif add < target:
                        left +=1
                    elif add > target :
                        right -=1
        return ans
    
class RecursiveTwoPointer:
    def four_sum(self, nums, target):
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        if n <= 4:
            if sum(nums) == target:
                return [nums]
            return []
        
        def k_sum(nums, target, k):
            ans = []
            if not nums:
                return []
            
            avg_value = target //k
            if avg_value < nums[0] or nums[-1] < avg_value:
                return ans
            if k == 2:
            
                return two_sum(nums, target)
            for i in range(len(nums)):
                
                if i == 0 or nums[i]!= nums[i-1]:

                    for subset in k_sum(nums[i+1:], target -nums[i], k-1):
                        ans.append([nums[i]]+ subset)
            return ans
        
        def two_sum(nums, target):
            ans = []
            left, right = 0 , len(nums)-1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target or (left > 0 and nums[left -1] == nums[left]):
                    left +=1
                elif curr_sum > target or (right < len(nums) -1 and nums[right +1] == nums[right]):
                    right -=1
                else:
                    ans.append([nums[left], nums[right]])
                    left +=1 
                    right -=1
            return ans
        return k_sum(nums, target , 4)
    
from typing import List

class HashSet:
    def four_sum(self, nums, target):
        def k_sum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            # There are k remaining values to add to the sum. The
            # average of these values is at least target // k.
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in k_sum(nums[i + 1 :], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            # purpose of set is to find the complement of the target
            s = set()

            for i in range(len(nums)):
                # by checking the first value of last added index of the list
                # we prevent from duplication since the nums is ssorted 
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])

            return res

        nums.sort()
        return k_sum(nums, target, 4)
                
            
                     
            

    
sol = HashSet()
# print(sol.four_sum([2,2,2,2,2], 8))
print(sol.four_sum([1,0,-1,0,-2,2], 0))
print(sol.four_sum([-2,-1,-1,1,1,2,2], 0))
print(sol.four_sum([-1,0,1,2,-1,-4], -1))
                        
                        
                    
                