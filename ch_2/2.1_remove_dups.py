"""
Q. Write code to remove duplicates from an unsorted linked list.
"""
import unittest
from linked_list import LinkedList

def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()
    
    while current:
        if current.val not in seen:
            seen.add(current.val)
            previous = current
        else:
            previous.next = current.next
        
        current = current.next

class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        # Test case 1: Empty linked list
        ll = LinkedList()
        remove_dups(ll)
        self.assertIsNone(ll.head)

        # Test case 2: Linked list with no duplicates
        ll = LinkedList([1, 2, 3, 4, 5])
        remove_dups(ll)
        self.assertEqual(ll.to_list(), [1, 2, 3, 4, 5])

        # Test case 3: Linked list with duplicates
        ll = LinkedList([1, 2, 3, 2, 4, 5, 1, 6])
        remove_dups(ll)
        self.assertEqual(ll.to_list(), [1, 2, 3, 4, 5, 6])

        # Test case 4: Linked list with all duplicates
        ll = LinkedList([1, 1, 1, 1, 1])
        remove_dups(ll)
        self.assertEqual(ll.to_list(), [1])

        # Test case 5: Linked list with a single node
        ll = LinkedList([1])
        remove_dups(ll)
        self.assertEqual(ll.to_list(), [1])

    def test_remove_dups_with_none(self):
        # Test case 6: Linked list with None values
        ll = LinkedList([1, None, 2, None, 3])
        remove_dups(ll)
        self.assertEqual(ll.to_list(), [1, None, 2, 3])

if __name__ == '__main__':
    unittest.main()