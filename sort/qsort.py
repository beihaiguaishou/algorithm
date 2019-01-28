import random


# 可优化去掉forward状态位， 在while中向前向后交换一次，i >= j时停止
def qsort(arr, start, end):
    if start < 0 or end < 0 or end <= start:
        return
    divide = start
    i = start
    j = end
    forward = False
    while i != j:
        if forward:
            if arr[i] > arr[divide]:
                tmp = arr[i]
                arr[i] = arr[divide]
                arr[divide] = tmp
                divide = i
                forward = False
            else:
                i += 1
        else:
            if arr[j] < arr[divide]:
                tmp = arr[j]
                arr[j] = arr[divide]
                arr[divide] = tmp
                divide = j
                forward = True
            else:
                j -= 1
    qsort(arr, start, divide - 1)
    qsort(arr, divide + 1, end)


if __name__ == '__main__':
    arr = []
    [arr.append(random.randint(-100, 100)) for i in range(random.randint(20, 50))]
    print(arr)
    qsort(arr, 0, len(arr) - 1)
    print(arr)
    print(sorted(arr))
