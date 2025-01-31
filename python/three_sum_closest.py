'''
Threesum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104


'''
class TwoPointer:
    def three_sun_closest(self, nums, target):
        nums.sort()
        
        ans, n = nums[0] + nums[1] + nums[2], len(nums)
        min_diff = float('inf')
        
        # with sorting if the first three are greater than the target
        # then we don;t need to find out the other remaining elements and vice-versa for the 
        # last three
        if sum(nums[:3]) >= target:
            return sum(nums[:3])
        elif sum(nums[-3:]) <= target:
            return sum(nums[-3:])
        
        for i in range(n):
            left = i+1 
            right = n-1
            
            if i and nums[i] == nums[i - 1]:
                continue
            # Directly going to the last element and checking for the last option
            add = nums[i] + nums[right] + nums[right-1]
            if add < target:
                if target -add < ans:
                    min_diff = target - add
                    ans = add
                continue
                    
            
            while left < right:
                add = nums[i] + nums[left] + nums[right]
                min_diff = add -target
                if abs(target - add) < abs(target - ans):
                    ans = add
                if min_diff == 0:
                    return target
                elif add < target:
                    if add -target < min_diff:
                        min_diff = add-target
                        ans = add
                    left +=1
                elif add  > target :
                    if add -target < min_diff:
                        min_diff = add-target
                        ans = add
                    right -=1

                
        return ans

sol = TwoPointer()
# print(sol.three_sun_closest([0,0,0], 1))
# print(sol.three_sun_closest( [-1,2,1,-4], 1))
print(sol.three_sun_closest( [-4,2,2,3,3,3], 0))
# print(sol.three_sun_closest([0,0,0], 1))
