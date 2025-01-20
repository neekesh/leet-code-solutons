'''
    Valid Parentheses
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.


    Example 1:
    Input: s = "()"
    Output: valid

    Example 2:
    Input: s = "()[]{}"
    Output: valid

    Example 3:
    Input: s = "(]"
    Output: invalid


    Example 4:
    Input: s = "([)]"
    Output: invalid

    Example 5:
    Input: s = "{[]}"
    Output: valid
    Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'
'''


class StackSolution:
    def is_valid(self, s):
        stack = []
        mapping = {')': '(', '}':"{", "]":"["}
                    
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)  
        return True if not stack else False
        
        
sol = StackSolution()

print(sol.is_valid("{[]}"))
print(sol.is_valid("([)]"))
print(sol.is_valid("()[]{}"))
print(sol.is_valid("([{]}"))

class ReplaceString:
    def is_valid(self, s):
        while "{}" in s or "()" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return not s
    
     
sol = ReplaceString()

print(sol.is_valid("{[]}"))
print(sol.is_valid("([)]"))
print(sol.is_valid("()[]{}"))
print(sol.is_valid("([{]}"))
