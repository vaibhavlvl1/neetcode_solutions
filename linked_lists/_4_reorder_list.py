from DSA import ll_input,printll,reverse1

"""
143. Reorder List
Medium
8K
277
Companies

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]



Constraints:

    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000


"""

head = ll_input()

def reorder(head):

    curr = head
    curr2 = head.next
    head2 = curr2
    while curr.next.next is not None:
        curr.next = curr.next.next
        curr = curr.next


    return head
he1= reorder(head)
printll(he1)

