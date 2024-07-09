import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_cases(self):
        self.assertTrue(self.solution.isValid("()"), "Should be valid")
        self.assertTrue(self.solution.isValid("()[]{}"), "Should be valid")
        self.assertTrue(self.solution.isValid("{[]}"), "Should be valid")

    def test_invalid_cases(self):
        self.assertFalse(self.solution.isValid("(]"), "Should be invalid")
        self.assertFalse(self.solution.isValid("([)]"), "Should be invalid")
        self.assertFalse(self.solution.isValid("((()"), "Should be invalid")

if __name__ == '__main__':
    unittest.main()