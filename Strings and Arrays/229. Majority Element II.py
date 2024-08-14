# medium

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
"""

import math
from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        floor = math.floor(len(nums) / 3)

        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        return [key for key, value in hashmap.items() if value > floor]


"""
NOTE:
Sure! Here’s a concise note to help you remember how to retrieve keys from a dictionary based on their values:

---

## Retrieving Keys from a Dictionary Based on Values

### 1. **Retrieve the First Key with a Specific Value**

To find the first key that matches a specific value in a dictionary:

```python
# Example dictionary
my_dict = {3: 3, 4: 2, 5: 1, 2: 1}

# Value to find
target_value = 1

# Find the first key with the target value
key_with_value = next((key for key, value in my_dict.items() if value == target_value), None)

print(key_with_value)  # Output: 5 (or 2, depending on the order)
```

### 2. **Retrieve All Keys with a Specific Value**

To find all keys that have a specified value:

```python
# Example dictionary
my_dict = {3: 3, 4: 2, 5: 1, 2: 1}

# Value to find
target_value = 1

# Find all keys with the target value
keys_with_value = [key for key, value in my_dict.items() if value == target_value]

print(keys_with_value)  # Output: [5, 2]
```

### **Key Concepts**

- **Iteration**: Use `my_dict.items()` to iterate over key-value pairs.
- **Condition**: Check if `value == target_value`.
- **Output**: 
  - Use `next()` for the first matching key.
  - Use a list comprehension for all matching keys.

---

Feel free to refer to this note whenever you need a reminder!
"""