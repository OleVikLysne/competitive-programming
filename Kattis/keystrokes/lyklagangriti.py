import sys


class Node:
    def __init__(self, val=None, parent=None, child=None):
        self.val = val
        self.parent = parent
        self.child = child


def write(node: Node, char):
    new_node = Node(val=char, parent=node, child=node.child)
    node.child.parent = new_node
    node.child = new_node
    return new_node

def backspace(node: Node):
    parent = node.parent
    child = node.child
    parent.child = child
    child.parent = parent
    return parent


tail = Node()
head = Node(child=tail)
tail.parent = head
current = head
for char in sys.stdin.readline().rstrip():
    if char == "L":
        current = current.parent
    elif char == "R":
        current = current.child
    elif char == "B":
        current = backspace(current)
    else:
        current = write(current, char)


current = head.child
while current != tail:
    sys.stdout.write(current.val)
    current = current.child
