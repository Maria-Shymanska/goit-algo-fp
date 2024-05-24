'''Алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі,
використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин
та обчислення найкоротших шляхів від початкової вершини до всіх інших.'''

import heapq

def dijkstra(graph, start_vertex):
    # Ініціалізація
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    heapq.heapify(priority_queue)
    visited = (set)
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        