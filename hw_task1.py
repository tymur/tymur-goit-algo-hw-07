# === Клас вузла двійкового дерева пошуку (BST) ===
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# === Функція вставки елементів у BST ===
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# === Функція пошуку найбільшого значення ===
def find_max(root):
    if root is None:
        return None  # дерево порожнє
    current = root
    while current.right is not None:
        current = current.right
    return current.key

# === Приклад використання ===
root = None
# Створюємо дерево:
for value in [50, 30, 70, 90, 20, 120, 40, 60, 80]:
    root = insert(root, value)

# Знаходимо найбільше значення
max_value = find_max(root)
print(f"Найбільше значення в дереві: {max_value}")
