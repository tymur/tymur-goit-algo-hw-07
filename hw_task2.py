# === Клас вузла AVL-дерева ===
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # початкова висота вузла

# === Функції для вставки з балансуванням ===
def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right

    # Виконуємо ротацію
    x.right = y
    y.left = T2

    # Оновлюємо висоти
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    # Виконуємо ротацію
    y.left = x
    x.right = T2

    # Оновлюємо висоти
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def insert(node, key):
    # Стандартна вставка
    if not node:
        return AVLNode(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # Оновлюємо висоту вузла
    node.height = 1 + max(get_height(node.left), get_height(node.right))

    # Балансування вузла (чотири способи, як показано в конспекті)
    balance = get_balance(node)

    # Ліво-Ліво
    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    # Право-Право
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    # Ліво-Право
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # Право-Ліво
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

# === Функція пошуку найменшого значення ===
def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current.key

# === Приклад використання ===
root = None
for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

# Знаходимо найменше значення
min_value = find_min(root)
print(f"Найменше значення в AVL-дереві: {min_value}")
