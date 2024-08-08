# medium
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a given string into a zigzag pattern on a given number of rows.

        Args:
        s (str): The input string to be converted.
        numRows (int): The number of rows in the zigzag pattern.

        Returns:
        str: The string read line by line from the zigzag pattern.
        """
        # Edge case: if numRows is 1 or greater than or equal to the length of the string,
        # return the original string as no zigzag pattern is needed.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a list to store strings for each row
        rows = ['' for _ in range(numRows)]
        
        # Variables to track the current row and the direction of movement
        current_row = 0
        going_down = False
        
        # Iterate over each character in the string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char
            
            # Determine if we need to change direction
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            # Update the current row based on the direction
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to form the final result
        return ''.join(rows)

# Test cases
def test_zigzag_conversion():
    solution = Solution()
    
    # Test case 1: Basic example
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    expected1 = "PAHNAPLSIIGYIR"
    assert solution.convert(s1, numRows1) == expected1, f"Test case 1 failed: expected {expected1}"
    
    # Test case 2: Single row
    s2 = "PAYPALISHIRING"
    numRows2 = 1
    expected2 = "PAYPALISHIRING"
    assert solution.convert(s2, numRows2) == expected2, f"Test case 2 failed: expected {expected2}"
    
    # Test case 3: Number of rows greater than string length
    s3 = "AB"
    numRows3 = 3
    expected3 = "AB"
    assert solution.convert(s3, numRows3) == expected3, f"Test case 3 failed: expected {expected3}"
    
    # Test case 4: Two rows
    s4 = "PAYPALISHIRING"
    numRows4 = 2
    expected4 = "PYAIHRNAPLSIIG"
    assert solution.convert(s4, numRows4) == expected4, f"Test case 4 failed: expected {expected4}"
    
    # Test case 5: Four rows
    s5 = "PAYPALISHIRING"
    numRows5 = 4
    expected5 = "PINALSIGYAHRPI"
    assert solution.convert(s5, numRows5) == expected5, f"Test case 5 failed: expected {expected5}"
    
    print("All test cases passed!")

# Run tests
test_zigzag_conversion()