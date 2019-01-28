import random


def hsort(arr):
    length = len(arr)
    init_heap(arr)
    print(arr)
    tmp = arr[0]
    arr[0] = arr[length - 1]
    arr[length - 1] = tmp
    sorted = 1
    while sorted < length:
        ajust_heap(arr, 0, length - sorted)
        tmp = arr[0]
        arr[0] = arr[length - 1 - sorted]
        arr[length - 1 - sorted] = tmp
        sorted += 1


def init_heap(arr):
    length = len(arr)
    for i in range(int(length / 2), -1, -1):
        ajust_heap(arr, i, length)


def ajust_heap(arr, root, end):
    if end > 2 * root + 1:
        bigger = 2 * root + 1
        if end > 2 * root + 2 and arr[2 * root + 2] > arr[2 * root + 1]:
            bigger = 2 * root + 2
        if arr[root] < arr[bigger]:
            tmp = arr[root]
            arr[root] = arr[bigger]
            arr[bigger] = tmp
            ajust_heap(arr, bigger, end)


if __name__ == '__main__':
    arr = []
    [arr.append(random.randint(-100, 100)) for i in range(random.randint(10, 30))]
    print(arr)
    hsort(arr)
    print(arr)
    print(sorted(arr))
