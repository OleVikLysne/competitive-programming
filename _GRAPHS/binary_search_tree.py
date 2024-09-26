
"""
    BST implementation (not exhaustively tested, only used to solve https://open.kattis.com/problems/golf)

    Binary Search Tree with smaller values on the left. Supports queries to find how many values
    are strictly larger than x. To find larger or equal, you can probably do so by adding the node.count-1
    in the query function (not tested).

    The tree is NOT self-balancing, and can therefore turn degenerate and cause O(n) adding/removing/querying.

    Use a dummy root intialized with some large value BST(float("inf"))
"""

class BST:
    def __init__(self, val, parent=None):
        self.val = val
        self.size = 0
        self.count = 0
        self.parent = parent
        self.left = None
        self.right = None

    def left_size(self):
        return self.left.size if self.left is not None else 0

    def right_size(self):
        return self.right.size if self.right is not None else 0

    def replace_with(self, other):
        if other is not None:
            other.parent = self.parent
        if self.parent.left == self:
            self.parent.left = other
        else:
            self.parent.right = other

    def is_leaf(self):
        return self.left is None and self.right is None

    def remove(self):
        # reduce size of self and its parents
        node = self
        while node is not None:
            node.size -= 1
            node = node.parent

        self.count -= 1
        if self.count > 0:
            return

        if self.is_leaf():
            self.replace_with(None)
            return

        if self.left is None:
            self.replace_with(self.right)
            return
        if self.right is None:
            self.replace_with(self.left)
            return

        # we have to merge the two subtrees
        # choose the subtree of the largest size as the new root
        if self.left.size > self.right.size:
            self.replace_with(self.left)
            # find rightmost node in left subtree
            subtree = self.left
            subtree.size += self.right.size
            while subtree.right is not None:
                subtree = subtree.right
                subtree.size += self.right.size
            subtree.right = self.right
            self.right.parent = subtree
        else:
            self.replace_with(self.right)
            # find leftmost node in right subtree
            subtree = self.right
            subtree.size += self.left.size
            while subtree.left is not None:
                subtree = subtree.left
                subtree.size += self.left.size
            subtree.left = self.left
            self.left.parent = subtree

    def next_tree(self, val):
        if val == self.val:
            return self
        if val < self.val:
            if self.left is None:
                self.left = BST(val, self)
            return self.left
        else:
            if self.right is None:
                self.right = BST(val, self)
            return self.right

    def add(self, val):
        self.size += 1
        if (next := self.next_tree(val)) == self:
            self.count += 1
            return self
        return next.add(val)

    def query(self, val):
        if (next := self.next_tree(val)) == self:
            return self.left_size()
        if self.val < next.val:
            return next.query(val) + self.size - self.right_size()
        return next.query(val)

    def find(self, val):
        if (next := self.next_tree(val)) == self:
            return self
        return next.find(val)


tree = BST(float("inf"))
