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
        ans =  float('inf')
        n = len(nums) -1
        for i in range(n):
            left = i+1
            right = n
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                current = sum -target
                if abs(target - sum) < abs(target - ans):
                    ans = sum
                if current == 0:
                    return target
                elif sum < target:
                    left +=1
                elif sum  > target :
                    right -=1

                
        return ans

sol = TwoPointer()
print(sol.three_sun_closest([0,0,0], 1))
print(sol.three_sun_closest( [-1,2,1,-4], 1))
# print(sol.three_sun_closest([0,0,0], 1))
