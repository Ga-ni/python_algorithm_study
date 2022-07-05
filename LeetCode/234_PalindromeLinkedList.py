from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        input = []

        node = head
        while node.next:
            input.append(node.val)
            node = node.next

        input.append(node.val)

        for i in range(int(len(input) / 2)):
            if input[i] != input[len(input) - 1 - i]:
                return False

        return True


'''
Runtime: 1088 ms, faster than 57.16% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.7 MB, less than 38.26% of Python3 online submissions for Palindrome Linked List.
'''

