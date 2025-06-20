"""
Stacks: Last-In-First-Out (LIFO) data structure
Key Operations: Push, Pop, Peek, Applications
"""

# --------------------------
# 1. Stack Implementation
# --------------------------
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)  # O(1)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # O(1)
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # O(1)
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0  # O(1)
    
    def size(self):
        return len(self.items)  # O(1)
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.items)  # Output: [10, 20, 30]
print("Pop:", stack.pop())  # Output: 30
print("Peek:", stack.peek())  # Output: 20
print("Size after pop:", stack.size())  # Output: 2
print("Is stack empty?", stack.is_empty())  # Output: False

# --------------------------
# 2. Built-in Alternatives
# --------------------------
# Python lists can act as stacks (but lack explicit APIs)
stack_list = []
stack_list.append(10)  # Push
stack_list.pop()  # Pop (raises IndexError if empty)

# collections.deque is optimized for stack operations
from collections import deque
deque_stack = deque()
deque_stack.append(40)  # Push
deque_stack.pop()  # Pop (raises IndexError if empty)

# --------------------------
# 3. Applications
# --------------------------
# A. Parentheses Matching (O(n))
def is_balanced(expr):
    stack = Stack()
    pairs = { ')':'(', '}':'{', ']':'[' }
    for char in expr:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

print(is_balanced("({[]})"))  # True
print(is_balanced("({[)]})"))  # False

# B. Undo/Redo Mechanism
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def write(self, char):
        self.text += char
        self.undo_stack.push(('add', len(char)))
        self.redo_stack = Stack() # Clear redo on new action

    def undo(self):
        if not self.undo_stack.is_empty():
            action, pos = self.undo_stack.pop()
            if action == "add":
                removed = self.text[-pos:]
                self.text = self.text[:-pos]
                self.redo_stack.push(('remove', removed))
            return self.text
        return "Nothing to undo"

    def redo(self):
        if not self.redo_stack.is_empty():
            action, data = self.redo_stack.pop()
            if action == "remove":
                self.text += data
                self.undo_stack.push(('add', len(data)))
            return self.text
        return "Nothing to redo"

editor = TextEditor()
editor.write("hello")
editor.write("world")
print("Text: ", editor.text)
print("Undo: ", editor.undo())  # "hello"
print("Redo: ", editor.redo())  # "hello world"

# --------------------------
# 4. Advanced Use Cases
# --------------------------
# A. Postfix Evaluation (O(n))
def eval_postfix(expr):
    stack = Stack()
    for token in expr.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == '+': stack.push(a+b)
            elif token == '-': stack.push(a-b)
            elif token == '*': stack.push(a*b)
            elif token == '/': stack.push(a/b)
    return stack.pop()

print(eval_postfix("3 4 + 5 *")) # 35

# B. Browser History (Simplified)
class Browser:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = None

    def visit(self, url):
        if self.current:
            self.back_stack.push(current)
        self.current(url)
        self.forward_stack = Stack()

    def go_back():
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current)
            self.current = self.back_stack.pop()
            return self.current
        return "Can't go back"

# --------------------------
# 5. Exercises
# --------------------------
# 1. Reverse a string using a stack
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

print(reverse_string("Hello, This is a reversed string"))

# 2. Check for redundant parentheses
def has_redundant_parentheses(expr):
    stack = Stack()
    for char in expr:
        if char == ")":
            top = stack.pop()
            if top == "(":
                return True
            while top != "(":
                top = stack.pop()
        else:
            stack.push(char)
    return False

print(has_redundant_parentheses("(())"))






