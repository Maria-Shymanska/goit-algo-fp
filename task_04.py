

import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла
        
def add_edges(graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)   # Використання id та збереження значення вузла
            if node.left:
               graph.add_edge(node.id, node.left.id)
               l = x - 1 / 2 ** layer
               pos[node.left.id] = (l, y - 1)
               l = add_edges(graph, node.left, pos, x=l, y= y - 1, layer=layer + 1)
            if node.right:
               graph.add_edge(node.id, node.right.id)
               r = x + 1 / 2 ** layer
               pos[node.right.id] = (r, y - 1)
               r = add_edges(graph, node.right, pos, x= r, y= y - 1, layer=layer + 1)
        return graph