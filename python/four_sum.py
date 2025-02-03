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

class TwoPointer:
    def four_sum(self, nums, target):
        
        if not nums:
            return []
        nums.sort()
        ans = []
        unique = set()
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
                        if quad not in unique:
                            unique.add(quad)
                            ans.append(list(quad))

                        while left < right and nums[left] == nums[left +1]:
                            left +=1
                        while left < right and nums[right] == nums[right -1]:
                            right -=1
                        left +=1
                        right -= 1
                    elif add < target:
                        left +=1
                    elif add > target:
                        right -=1
        return ans
    
    
sol = TwoPointer()
# print(sol.four_sum([2,2,2,2,2], 8))
# print(sol.four_sum([1,0,-1,0,-2,2], 0))
print(sol.four_sum([-2,-1,-1,1,1,2,2], 0))
print(sol.four_sum([-1,0,1,2,-1,-4], -1))
                        
                        
                    
                