import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, highlight_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if highlight_nodes is not None:
        colors = [highlight_nodes.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    else:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(node, visit_order, highlight_nodes, colors, depth=0):
    if node is None:
        return
    visit_order.append(node.id)
    color = colors[len(visit_order) - 1]
    highlight_nodes[node.id] = color
    draw_tree(root, highlight_nodes)
    dfs(node.left, visit_order, highlight_nodes, colors, depth + 1)
    dfs(node.right, visit_order, highlight_nodes, colors, depth + 1)

def bfs(node, visit_order, highlight_nodes, colors):
    from collections import deque
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current is not None:
            visit_order.append(current.id)
            color = colors[len(visit_order) - 1]
            highlight_nodes[current.id] = color
            draw_tree(root, highlight_nodes)
            queue.append(current.left)
            queue.append(current.right)

def generate_colors(n):
    base_color = mcolors.hex2color("#1296F0")  # Starting color
    colors = [mcolors.rgb2hex((base_color[0] * (1 - i / n), base_color[1] * (1 - i / n), base_color[2] * (1 - i / n))) for i in range(n)]
    return colors

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходів
visit_order = []
highlight_nodes = {}
colors = generate_colors(6)  # Кількість вузлів у дереві

# Візуалізація обходу в глибину (DFS)
print("DFS:")
dfs(root, visit_order, highlight_nodes, colors)

# Візуалізація обходу в ширину (BFS)
visit_order = []
highlight_nodes = {}
print("BFS:")
bfs(root, visit_order, highlight_nodes, colors)
