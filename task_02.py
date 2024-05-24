'''Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.'''

import turtle

def pifagor_tree(t, branch_len, order):
    if order == 0:
        return

    # Малюємо стовбур
    t.forward(branch_len)
    
    # Малюємо праву гілку
    t.right(45)
    pifagor_tree(t, branch_len * 0.7, order - 1)
    
    # Повертаємося до стовбура і малюємо ліву гілку
    t.left(90)
    pifagor_tree(t, branch_len * 0.7, order - 1)
    
    # Повертаємося до стовбура
    t.right(45)
    t.backward(branch_len)

def draw_pifagor_tree(order):
    window = turtle.Screen()
    window.bgcolor("white")  # Білий фон
    window.title("Дерево Піфагора")
    
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.left(90)  # Повертаємо черепашку для малювання знизу вгору
    t.penup()
    t.goto(0, -350)  # Початкова позиція для дерева
    t.pendown()
    t.color("black")  # Зміна кольору дерева на чорний

    pifagor_tree(t, 200, order)  # Початкова довжина гілки

    window.mainloop()

def main():
    # Максимальний і мінімальний рівень рекурсії
    MAX_ORDER = 10
    MIN_ORDER = 1

    while True:
        try:
            order = int(input(f"Введіть глибину рекурсії (від {MIN_ORDER} до {MAX_ORDER}): "))
            if MIN_ORDER <= order <= MAX_ORDER:
                break
            else:
                print(f"Будь ласка, введіть значення в діапазоні від {MIN_ORDER} до {MAX_ORDER}.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    draw_pifagor_tree(order)

if __name__ == "__main__":
    main()