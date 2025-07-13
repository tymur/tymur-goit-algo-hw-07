# === Реалізація AVL-дерева з балансуванням (з завдання 2) ===
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def insert(node, key):
    if not node:
        return AVLNode(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    # Балансування
    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

# === Функція для обходу та підрахунку суми ===
# Цей функціонал не є вимогою у завданні, але я вирішив також реалізувати обхід і візуалізацію посортованого списку значень
def in_order_traversal(node, result=None):
    """Обхід дерева in-order та збір усіх значень у список.""" 
    if result is None:
        result = []
    if node:
        in_order_traversal(node.left, result)
        result.append(node.key)
        in_order_traversal(node.right, result)
    return result

def sum_tree(node):
    """Підрахунок суми всіх значень у дереві."""
    if node is None:
        return 0
    return sum_tree(node.left) + node.key + sum_tree(node.right)

# === Створюємо дерево та додаємо значення ===
root = None
values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
for value in values:
    root = insert(root, value)

# === Перевірка вузлів та їх суми ===
all_nodes = in_order_traversal(root)
total_sum = sum_tree(root)

print(f"Всі вузли дерева (in-order): {all_nodes}")
print(f"Сума значень всіх вузлів: {total_sum}")
