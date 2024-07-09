import unittest

class TestSum(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum([1, 2, 3]), 6, "should be 6")
    
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "should be 5")

    def test_sum_empty(self):
        self.assertEqual(sum([]), 0, "should be 0")

if __name__ == "__main__":
    unittest.main()