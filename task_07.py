import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def simulate_dice_rolls(num_rolls):
    results = [0] * 11  # Масив для збереження кількості випадків для сум від 2 до 12

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        results[roll_sum - 2] += 1  # Зберігаємо результат (зміщення на 2 для індексування від 0)

    return results

# Функція для обчислення ймовірностей
def calculate_probabilities(results, num_rolls):
    probabilities = [count / num_rolls for count in results]
    return probabilities

# Функція для побудови графіка
def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    theoretical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probabilities, alpha=0.6, label='Simulated Probabilities')
    plt.plot(sums, theoretical_probabilities, 'ro-', label='Theoretical Probabilities')
    
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probability of Sums from Rolling Two Dice')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()

# Головна функція
def main():
    num_rolls = 1000000  # Кількість кидків
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    
    # Вивід результатів
    print("Sum\tSimulated Probability\tTheoretical Probability")
    theoretical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    for i in range(11):
        print(f"{i + 2}\t{probabilities[i]:.4f}\t\t{theoretical_probabilities[i]:.4f}")
    
    plot_probabilities(probabilities)

# Запуск програми
if __name__ == "__main__":
    main()
