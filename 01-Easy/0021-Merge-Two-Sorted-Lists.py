# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Description: Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        
        # Traverse both linked lists until one of them is empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # Move the tail to the next node after appending
            tail = tail.next
        
        # Append the remaining nodes of l1 or l2
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next


# Unit Test: Input: l1 = [1,2,4], l2 = [1,3,4], Output: [1,1,2,3,4,4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list3 = Solution.mergeTwoLists(list1, list2)
assert list3.val == 1
assert list3.next.val == 1
assert list3.next.next.val == 2
assert list3.next.next.next.val == 3
assert list3.next.next.next.next.val == 4
assert list3.next.next.next.next.next.val == 4
print("All unit tests are passed")
