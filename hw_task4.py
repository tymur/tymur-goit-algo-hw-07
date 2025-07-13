import networkx as nx
import matplotlib.pyplot as plt

# === Клас коментаря ===
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []  # список відповідей
        self.is_deleted = False  # прапорець видалення

    def add_reply(self, reply_comment):
        """Додає відповідь до коментаря."""
        self.replies.append(reply_comment)

    def remove_reply(self):
        """Позначає коментар як видалений."""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        """Рекурсивно виводить коментарі та відповіді."""
        indent = "    " * level
        print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

    def build_graph(self, graph, parent=None):
        """Будує граф для візуалізації коментарів."""
        label = f"{self.author}: {self.text}"
        graph.add_node(label)
        if parent:
            graph.add_edge(parent, label)
        for reply in self.replies:
            reply.build_graph(graph, label)

def visualize_comments(root_comment):
# Візуалізує дерево коментарів. не є частиною завдання, просто мені особисто так наочніше.
    graph = nx.DiGraph()
    root_comment.build_graph(graph)

    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=8)
    plt.title("Ієрархія коментарів")
    plt.show()

# === Приклад використання ===
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видаляємо перший коментар-відповідь
reply1.remove_reply()

# Вивід у консолі
root_comment.display()

# Візуалізація дерева коментарів
visualize_comments(root_comment)
