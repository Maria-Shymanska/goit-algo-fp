'''Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку необхідно:

1.Написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
2.Розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
3.Написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.'''

# Спочатку реалізуємо базовий однозв'язний список з вузлами.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Функція реверсування однозв'язного списку

def reverse_linked_list(llist):
    prev = None
    current = llist.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    llist.head = prev
    
    
# Алгоритм сортування: сортування вставками

def sorted_insert(sorted_head, new_node):
    if not sorted_head or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        sorted_head = new_node
    else:
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_head

def insertion_sort_linked_list(llist):
    sorted_head = None
    current = llist.head
    while current:
        next_node = current.next
        # Important to detach the current node from the rest of the list
        current.next = None
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    llist.head = sorted_head


# Функція об'єднання двох відсортованих однозв'язних списків

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list



# Створення однозв'язних списків
llist1 = LinkedList()
llist2 = LinkedList()

for i in [3, 1, 5]:
    llist1.append(i)

for i in [4, 2, 6]:
    llist2.append(i)

# Друк початкових списків
print("Початковий список 1:")
llist1.print_list()

print("Початковий список 2:")
llist2.print_list()

# Реверсування списку 1
reverse_linked_list(llist1)
print("Реверсований список 1:")
llist1.print_list()

# Сортування списку 1
insertion_sort_linked_list(llist1)
print("Відсортований список 1:")
llist1.print_list()

# Об'єднання списків
merged_list = merge_sorted_lists(llist1, llist2)
print("Об'єднаний відсортований список:")
merged_list.print_list()






