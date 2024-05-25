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
    visited = set()
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад використання
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(distances)
      