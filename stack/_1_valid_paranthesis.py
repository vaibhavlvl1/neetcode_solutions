#######################StackImplementation###############################################

class Stack:
    def __init__(self):
        self.data = []
        self.count = 0

    def push(self,data):
        self.data.append(data)
        self.count +=1
    def isEmpty(self):
        return self.count==0
    def pop(self):
        if self.count==0:
            return "Already Empty"
        else:
            x = self.data.pop()
            self.count -=1
            return x
    def top(self):
        if self.count==0:
            return "Already Empty"
        return self.data[self.count-1]
    def size(self):
        return self.count

    def printStack(self):
        print(self.data)

# Testing Stack

# c=Stack()
# c.push(1)
# c.push(2)
# c.push(3)
# c.push(4)
# print("Whether is empty ? ",c.isEmpty())
# print("At Top is ",c.top())
# print("The size is ",c.size())
# c.printStack()
# print("poping begins")
# print(c.pop())
# print(c.pop())
# print(c.pop())
# print(c.pop())
# print(c.pop())
# print(c.pop())
# print("The size is ",c.size())
# print("At Top is ",c.top())


################################################################################################

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


"""

# solution
def isValid(self, c: str) -> bool:
    s = Stack()
    open = "{[("
    for ele in c:
        if ele in open:
            s.push(ele)
        elif s.top() == "[" and ele == "]":
            s.pop()
        elif s.top() == "{" and ele == "}":
            s.pop()
        elif s.top() == "(" and ele == ")":
            s.pop()
        else:
            s.push(ele)
    if s.isEmpty():
        return True
    else:
        return False




###### other solution

def isValid(self, s: str) -> bool:
    stack = []
    closeToopen = {")": "(", "}": "{", "]": "["}

    for c in s:
        if c in closeToopen:
            if stack and stack[-1] == closeToopen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

