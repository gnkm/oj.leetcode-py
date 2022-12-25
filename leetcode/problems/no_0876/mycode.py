"""876. Middle of the Linked List

URL: https://leetcode.com/problems/middle-of-the-linked-list/

## Description

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

difficulty: Easy

## Memo

@TODO: Study linked list.
I can't understand how to use ListNode.
"""

from typing import Any, Dict, List, Optional, Union


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        # I add this
        return f"ListNode({self.val = })"


# my code.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # def middleNode(self, head):
        pass


class SolutionModelAnswer:
    """
    https://leetcode.com/problems/middle-of-the-linked-list/solutions/154715/middle-of-the-linked-list/
    """
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        # When execute `python leetcode/problems/no_0876/mycode.py`, following error occur.
        # AttributeError: 'list' object has no attribute 'next'
        while arr[-1].next:
            # when `head` is 1, arr[-1].next = [2,3,4,5]
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]


if __name__ == "__main__":
    import pkg_resources
    if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
        import icecream
        _debug = icecream.ic
    else:
        _debug = print

    global debug
    debug = _debug

    list_node = ListNode(3)
    debug(list_node)
    debug(list_node.next)

    # solution = SolutionModelAnswer()
    # debug(solution.middleNode(3))
