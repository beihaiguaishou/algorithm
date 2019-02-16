import random

cnt = 0


def shell_sort(arr):
    length = len(arr)
    step_size = int(length / 2)
    while step_size > 0:
        shell_step(arr, step_size)
        step_size = int(step_size / 2)


# 本质为一次插入排序
def shell_step(arr, step_size):
    global cnt
    for i in range(step_size):
        for j in range(i, len(arr), step_size):
            k = j
            while k - step_size >= 0 and arr[k] < arr[k - step_size]:
                tmp = arr[k]
                arr[k] = arr[k - step_size]
                arr[k - step_size] = tmp
                k -= step_size
                cnt += 1


if __name__ == '__main__':
    arr = []
    [arr.append(random.randint(-100, 100)) for i in range(random.randint(10000, 10000))]
    print(arr)
    shell_sort(arr)
    print(arr)
    print(sorted(arr))
    print(len(arr))
    print(cnt)
