class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.visited = 1

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.recursive(self.root, value)

    def recursive(self, new_node, value):
        if value < new_node.value:
            if new_node.left is None:
                new_node.left = Node(value)
            else:
                self.recursive(new_node.left, value)
        elif value > new_node.value:
            if new_node.right is None:
                new_node.right = Node(value)
            else:
                self.recursive(new_node.right, value)

    def fromArray(self, array):
        self.root = None
        for value in array:
            self.insert(value)

    def search(self, value):
        curr_node = self.root
        self.visited = 1
        while curr_node is not None:
            if curr_node.value == value:
                return True
            elif curr_node.value > value:
                self.visited += 1
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
                self.visited += 1
        self.visited -= 1
        return False

    def min(self):
        curr_node = self.root
        self.visited = 1
        while curr_node is not None and curr_node.left is not None:
            curr_node = curr_node.left
            self.visited += 1
        return curr_node.value if curr_node else None

    def max(self):
        curr_node = self.root
        self.visited = 1
        while curr_node is not None and curr_node.right is not None:
            curr_node = curr_node.right
            self.visited += 1
        return curr_node.value if curr_node else None

    def visitedNodes(self):
        if self.root:
            return self.visited
        else:
            return 0
