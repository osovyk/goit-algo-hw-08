import heapq

def merge_k_lists(lists):
    heap = []
    result = []

    # Ініціалізуємо мін-купу першими елементами з кожного списку
    for i in range(len(lists)):
        if lists[i]:  # Перевіряємо, що список не порожній
            heapq.heappush(heap, (lists[i][0], i, 0))

    # Поки в купі є елементи
    while heap:
        # Витягуємо найменший елемент
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)

        # Якщо в поточному списку є ще елементи, додаємо наступний елемент до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_element, list_idx, element_idx + 1))

    return result

# Приклад використання:
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
