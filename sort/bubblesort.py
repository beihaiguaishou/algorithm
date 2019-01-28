import random


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i):
            if j + 1 < length and arr[j + 1] < arr[j]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp


if __name__ == '__main__':
    arr = []
    [arr.append(random.randint(-100, 100)) for i in range(random.randint(20, 50))]
    print(arr)
    bubble_sort(arr)
    print(arr)
    print(sorted(arr))
