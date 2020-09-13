# Сложность по времени (n, m - длины массивов): O(m) создание множества, далее O(n) на итерирование, каждая проверка - O(1), итого - O(n + m)
# Сложность по памяти: O(n + m)
def list_difference(a, b):
    b_set = set(b)
    return [x for x in a if x not in b]

print(list_difference([1], [])) # [1] expected
print(list_difference([1], [1])) # [] expected
print(list_difference([1], [1, 2])) # [] expected
print(list_difference([1, 2, 3], [1])) # [2, 3] expected
print(list_difference(range(100), range(10))) # [10, ..., 99] expected