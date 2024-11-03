import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

# Приклад використання:
unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_list = heapsort(unsorted_list)
print("Відсортований список:", sorted_list)
