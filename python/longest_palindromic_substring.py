'''
    Leet code Link: https://leetcode.com/problems/longest-palindromic-substring/
    Given a string s, return the longest palindromic substring in s.

    Example 1:

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
    Example 2:

    Input: s = "cbbd"
    Output: "bb"
    

    Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
'''


# Method 1: brute Force approach (Two pointer method)
# Time Complexity : O(n^3)
# Space Complexity: O(m)
class TwoPointerApproach:

    def longest_pallindrome(self, s: str) -> str:
        def check( i, j):
            left = i
            right = j-1
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left +=1
                    right -=1
            return True
        n = len(s)
        for length in range(len(s),0, -1):
            for start in range(len(s)-length+1):
               if check(start, start+length):
                    return s[start: start+length]
            
        return "" 


'''
    Method 2: Dynamic Programming
    
'''

class DynamicProgramming:
    def longest_pallindrome(self, s):
        n= len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0,0]
        for i in range(n):
            dp[i][i] = True
            if i < n-1:
                if s[i] == s[i+1]:
                    ans= [i,i+1]
                    dp[i][i+1] = True
        for diff in range(2, n):
            for i in range(0, n-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i,j]
        return s[ans[0]: ans[1]+1]
# dynamicProgramming = DynamicProgramming()
# print(dynamicProgramming.longest_pallindrome("babad"))

'''
Method 3: Expand from centers

'''
class ExpandFromCenters:
    def longest_pallindrome(self, s: str):
        n = len(s)
        def expand(i, j):
            left = i
            right = j
            while  right < n and left >= 0 and s[left]== s[right]:
                    left -=1
                    right +=1
            return right - left -1
        ans = [0, 0]
        for i in range(n):
            max_len = ans[1]-ans[0]
            odd_length = expand(i, i)
            if odd_length  > max_len +1:
                dist = odd_length //2
                ans =[i-dist, i+ dist]
            even_length = expand(i, i+1)
            if even_length  > max_len+1:
                
                dist = (even_length // 2) - 1
                ans =[i-dist, i+ dist+1]
            
        return s[ans[0]: ans[1]+1]  
    
pd = ExpandFromCenters()
print(pd.longest_pallindrome("ababa"))
                
