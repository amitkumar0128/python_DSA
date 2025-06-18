"""
Linked Lists: Sequential elements connected via pointers
Key Concepts: Node Structure, Traversal, Dummy Nodes
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --------------------------
# 1. Singly Linked List (SLL)
# --------------------------
class SLL:
    def __init__(self):
        self.head = None

    # Append (O(n))
    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)
    
    # Traversal (O(n))
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

# Example usage of SLL
sll = SLL()
sll.append(1)
sll.append(2)
sll.append(3)
print("SLL Print Forward")
sll.print_list()  # Output: 1 -> 2 -> 3 -> None

# --------------------------
# 2. Doubly Linked List (DLL)
# --------------------------
class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Append (O(1) with tail pointer)
    def append(self, val):
        new_node = DLLNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node   
    
    # Traversal (Forward)
    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print("None")

    # Traversal (Backward)
    def print_backward(self):
        curr = self.tail
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.prev
        print("None")

# Example Usage 
dll = DLL()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
print("DLL Print Forward")
dll.print_forward()
print("DLL Print Backward")
dll.print_backward()

# --------------------------
# 3. Pointer Manipulation
# --------------------------
# Reverse SLL (Iterative, O(n))
def reverse_sll(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Example
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_sll(head)
print("Reversed List: ")
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next # Output: 3 -> 2 -> 1 -> None
print("None")

# --------------------------
# 4. Dummy Nodes Technique
# --------------------------
# Merge Two Sorted SLLs (O(n+m))
def merge_sorted_list(l1, l2):
    dummmy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1 < l2:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

# --------------------------
# 5. Fast-Slow Pointers
# --------------------------
# Find Middle Node (O(n))
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Detect Cycle (O(n))
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# --------------------------
# 6. Exercises
# --------------------------
# 1. Remove Nth Node From End (One-pass, O(n))
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n+1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

# 2.Palindrome Check for SLL (O(n) time, O(1) space)
def is_palindrome_linked_list(head):
    if not head or not head.next:
        return True  # Empty or single-node list is palindrome
    
    # 1. Find middle (slow stops at mid-left for even, mid for odd)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 2. Reverse second half
    second_half = reverse_sll(slow)
    
    # 3. Compare first half and reversed second half
    p1, p2 = head, second_half
    while p2:  # Only need to compare until second half ends
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    
    return True
