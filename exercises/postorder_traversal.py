class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)

# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Зворотний обхід:")
postorder_traversal(root)
