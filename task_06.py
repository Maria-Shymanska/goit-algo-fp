items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортування елементів за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, values in sorted_items:
        cost = values['cost']
        calories = values['calories']
        
        if total_cost + cost <= budget:
            chosen_items.append(item)
            total_cost += cost
            total_calories += calories
    
    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]
    
    # Ініціалізація таблиці для зберігання максимальних калорій для кожного значення бюджету
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнення таблиці dp
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлення оптимального набору елементів
    w = budget
    chosen_items = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            w -= costs[i - 1]
    
    total_calories = dp[n][budget]
    total_cost = budget - w
    
    return chosen_items, total_calories, total_cost

# Приклад використання
budget = 100

print("Greedy Algorithm:")
greedy_chosen_items, greedy_total_calories, greedy_total_cost = greedy_algorithm(items, budget)
print(f"Chosen items: {greedy_chosen_items}")
print(f"Total calories: {greedy_total_calories}")
print(f"Total cost: {greedy_total_cost}")

print("\nDynamic Programming:")
dp_chosen_items, dp_total_calories, dp_total_cost = dynamic_programming(items, budget)
print(f"Chosen items: {dp_chosen_items}")
print(f"Total calories: {dp_total_calories}")
print(f"Total cost: {dp_total_cost}")
