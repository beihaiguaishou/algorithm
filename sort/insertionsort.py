import random


def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i - 1
        while j >= 0 and arr[j] > arr[i]:
            j -= 1
        tmp = arr[i]
        shift(arr, j + 1, i)
        arr[j + 1] = tmp


def shift(arr, start, end):
    for i in range(end - 1, start - 1, -1):
        arr[i + 1] = arr[i]


if __name__ == '__main__':
    arr = []
    [arr.append(random.randint(-100, 100)) for i in range(random.randint(20, 50))]
    print(arr)
    insertion_sort(arr)
    print(arr)
    print(sorted(arr))
