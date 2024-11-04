import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх і додаємо до загальних витрат
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання:
cable_lengths = [4, 3, 2, 6, 7, 1]
print("Мінімальні витрати:", min_connection_cost(cable_lengths))
