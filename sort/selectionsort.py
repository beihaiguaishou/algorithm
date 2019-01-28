import random


def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


if __name__ == '__main__':
    arr = []
    [arr.append(random.randint(-100, 100)) for i in range(random.randint(20, 50))]
    print(arr)
    selection_sort(arr)
    print(arr)
    print(sorted(arr))
