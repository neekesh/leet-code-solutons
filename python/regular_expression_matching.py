'''
Regular Expression Matching:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''
class Recursive:
    def isMatch(self, text: str, pattern: str) -> bool:

        # Base case: If the pattern is empty, the text must also be empty to match.
        if not pattern:
            return not text

        # Check if the first character of the text matches the first character of the pattern
        # This includes matching '.' (wildcard that matches any character).
        first_match = bool(text) and pattern[0] in {text[0], "."}

        # Handle '*' in the pattern
        if len(pattern) >= 2 and pattern[1] == "*":
            # Two possibilities:
            # 1. Ignore the '*' and the preceding element (move past both in the pattern).
            # 2. If the first characters match, treat '*' as consuming one occurrence of the element,
            #    and continue matching the rest of the text with the same pattern.
            return (
                self.isMatch(text, pattern[2:])  # Ignore '*' and its preceding element.
                or (first_match and self.isMatch(text[1:], pattern))  # Consume one match and recurse.
            )
        else:
            # If there's no '*', simply check the first characters and recurse on the rest of the text and pattern.
            return first_match and self.isMatch(text[1:], pattern[1:])

            
# solution = Recursive()
# print(solution.isMatch("aa", "a*"))            
# print(solution.isMatch("aa", "a"))            
# # print(solution.isMatch("aa", ".*"))            
# print(solution.isMatch("aab", "c*a*b"))            
# print(solution.isMatch("mississippi", "mis*is*ip*."))            
# print(solution.isMatch("a", "a"))     



        
       


class DynamicProgramming:
    def isMatch(self, s, pattern):
        memo = {}  # Memoization dictionary
        
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):  # If the pattern is exhausted
                    ans = i == len(s)  # Match if the string is also exhausted
                else:
                    first_match = i < len(s) and pattern[j] in (s[i], ".")
                    if j + 1 < len(pattern) and pattern[j + 1] == "*":
                        # Match zero occurrences (dp(i, j+2)) or one/more occurrences (dp(i+1, j))
                        ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
                    else:
                        # Match one character and move to the next
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans  # Cache the result
            return memo[i, j]
        
        return dp(0, 0)  # Start matching from the beginning

solution = DynamicProgramming()
# print(solution.isMatch("aa", "a*"))            
print(solution.isMatch("aa", "a"))            
# print(solution.isMatch("aa", ".*"))            
print(solution.isMatch("aab", "c*a*b"))            
print(solution.isMatch("mississippi", "mis*is*ip*."))            
print(solution.isMatch("a", "a"))    