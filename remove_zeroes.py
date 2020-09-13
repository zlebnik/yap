# Удаляем нули in-place из-за требования на O(1) дополнительной памяти
# В этой реализации оригинальная сортировка элементов сохраняться не будет, но за счет этого упрощения - более понятный код;
# Сложность линейная - потому что по каждому элементу массива мы "пройдем" либо справа, либо слева
def remove_zeroes_linear(a):
    last_non_zero_index = len(a) - 1
    while last_non_zero_index > 0 and a[last_non_zero_index] == 0:
        last_non_zero_index -= 1
    # проверяем, что список пуст
    if last_non_zero_index <= 0:
        a.clear()
        return a

    i = 0
    while i < last_non_zero_index + 1:
        if a[i] == 0:
            a[i] = a[last_non_zero_index]
            a[last_non_zero_index] = 0
            while last_non_zero_index > i and a[last_non_zero_index] == 0:
                last_non_zero_index -= 1
        i += 1

    del a[last_non_zero_index + 1:]

    return a

# В этой реализации сортировка элементов сохранится, сложность уже скорее квадратичная:
# В худшем случае мы будем "пузырьком" продвигать каждый второй элемент массива, что будет означать порядка n^2 операций
def remove_zeroes_stable(a):
    last_non_zero_index = len(a) - 1
    while last_non_zero_index > 0 and a[last_non_zero_index] == 0:
        last_non_zero_index -= 1
    # проверяем, что список пуст
    if last_non_zero_index <= 0:
        a.clear()
        return a

    i = 0
    while i < last_non_zero_index + 1:
        if a[i] == 0:
            j = i
            while j < last_non_zero_index:
                b = a[j]
                a[j] = a[j + 1]
                a[j + 1] = b
                j += 1
            while last_non_zero_index > i and a[last_non_zero_index] == 0:
                last_non_zero_index -= 1
        else:
            # здесь приращение i только в случае несмены мест, потому что 2 нуля могут быть подряд
            i += 1

    del a[last_non_zero_index + 1:]

    return a

print(remove_zeroes_linear([])) # expected: []
print(remove_zeroes_stable([])) # expected: []
print(remove_zeroes_linear([0])) # expected: []
print(remove_zeroes_stable([0])) # expected: []
print(remove_zeroes_linear([1, 2, 3])) # expected: [1, 2, 3]
print(remove_zeroes_stable([1, 2, 3])) # expected: [1, 2, 3]
print(remove_zeroes_linear([0, 100, 0, 20, 0, 0, 99, 0, 1, 0])) # expected: [1, 100, 99, 20]
print(remove_zeroes_stable([0, 100, 0, 20, 0, 0, 99, 0, 1, 0])) # expected: [100, 20, 99, 1]