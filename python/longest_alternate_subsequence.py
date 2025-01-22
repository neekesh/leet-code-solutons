'''
Longest alternate Subsequence
You are given a list X, which is a sequence composed exclusively of 0s and 1s. The task is to compute the length of the longest subsequence within this array that alternates between 0s and 1s.
A subsequence is a sequence that can be derived from the original array by deleting some or none of the elements, ensuring the order of the remaining elements is maintained. An alternating subsequence is one where no two adjacent elements are the same. In simpler terms, the elements of the subsequence alternate between 0 and 1.

Examples 1:
Input: X = [0, 1, 0, 1, 0]
output: 5

Examples 2:
Input: X = [0]
output: 1
Constraints:

1 >= X <= 10^5.
The elements in the array X are guaranteed to be either 0 or 1.'''

class Solution:
    def longest_alternate_subsequence(self, X):
        n = len(X)
        if n == 0:
            return 0  # No elements in the sequence
        if n == 1:
            return 1  # A single element is itself an alternating subsequence
        

        max_len = 0  # At least one element is part of the subsequence
        int_len = 1
        for i in range(1, n):
            if X[i] != X[i - 1]:  # A change is detected
                int_len += 1
            else:
                int_len = 1
            max_len = max(max_len, int_len)

        return max_len
 
    

sol = Solution()
# print(sol.longest_alternate_subsequence([0]))
# print(sol.longest_alternate_subsequence([0, 1, 0, 1, 0]))
# print(sol.longest_alternate_subsequence([0,0, 1, 0, 1, 0]))
# print(sol.longest_alternate_subsequence([1, 2, 2, 3, 4, 4, 5])) 
# print(sol.longest_alternate_subsequence([1, 1, 0, 1, 0, 0, 1]))  
print(sol.longest_alternate_subsequence([1, 1, 0, 1, 0, 0, 1,0,1,0,1,0,1]))  
