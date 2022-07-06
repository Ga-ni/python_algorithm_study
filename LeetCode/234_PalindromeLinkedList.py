# palindrome : 회문, 거꾸로 읽어도 제대로 읽는 것과 동인한 문장이나 낱말, 숫자, 문자열

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # my solution
    """
    Runtime: 1088 ms, faster than 57.16% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 46.7 MB, less than 38.26% of Python3 online submissions for Palindrome Linked List.
    """
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



    # best solution analysis
    """
    Runtime: 706 ms, faster than 98.91% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 31 MB, less than 98.54% of Python3 online submissions for Palindrome Linked List.
    """
    def isPalindrome_best_solution(self, head: Optional[ListNode]) -> bool:
        rev = None  # 첫 노드는 뒤집으면 마지막 노드니까 None으로 시작!
        fast = slow = head

        # fast는 2개씩, slow는 1개씩 이동하다가 fast의 next가 없으면 중간을 찾은 것!
        # fast 여부부터 확인하는 이유는 짝수개일 경우, 마지막 fast는 None이기 때문에 NoneType의 next에 접근할 수 없다는 에러 발생
        while fast and fast.next:
            fast = fast.next.next
            slow, rev, rev.next = slow.next, slow, rev

        # 요소가 홀수개인 경우 slow(비교할 뒤의 절반)을 하나 다음으로 이동
        if fast:
            slow = slow.next

        # 방향을 바꾼 앞쪽 절반 rev와 뒤쪽 절반 slow를 하나씩 값 비교.
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev


    """
    이 문제는 Linked List의 중간 지점을 찾으면서 앞의 node들은 반대 방향으로 바라보도록 next를 바꿔준다.
    중간을 찾으면, 방향을 바꿔둔 앞의 절반(rev)과 뒤의 절반(slow)을 비교하면서 결과를 도출하여 시간을 단축할 수 있다.
    1. 중간 지점을 찾는 방법은 slow와 fast라는 변수를 두면서 slow는 한 칸씩, fast는 두 칸씩 이동하도록 만든다.
    2. 앞의 node들이 바라보는 방향을 바꾸는 것은 next를 앞의 node로 지정해 주면 된다.
    """

