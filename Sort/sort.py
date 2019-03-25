import random


def generator(n):
    arr = []
    for x in range(n):
        y = random.randint(1, n)
        arr.append(y)
    return arr


def bubble_sort(arr):
    n = len(arr)
    is_sorted = True
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break


def heapify(arr, size, index):
    largest = index
    left = index*2 + 1
    right = index*2 + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, size, largest)


def heap_sort(arr):

    for i in range(len(arr)//2, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def merge(arr, temp1, temp2):

    i = j = k = 0
    while i < len(temp1) and j < len(temp2):
        if temp1[i] <= temp2[j]:
            arr[k] = temp1[i]
            i += 1
        else:
            arr[k] = temp2[j]
            j += 1
        k += 1
    while i < len(temp1):
        arr[k] = temp1[i]
        i += 1
        k += 1
    while j < len(temp2):
        arr[k] = temp2[j]
        j += 1
        k += 1


def merge_sort(arr):

    if len(arr) > 1:
        m = len(arr)//2
        temp1 = arr[:m]
        temp2 = arr[m:]
        merge_sort(temp1)
        merge_sort(temp2)
        merge(arr, temp1, temp2)


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]


def partition(arr, l, r):

    rand = random.randint(l, r)
    arr[rand], arr[r] = arr[r], arr[rand]
    pivot = arr[r]
    i = (l-1)
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1


def quick_sort(arr):
    quick_sort_imp(arr, 0, len(arr) -1)


def quick_sort_imp(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quick_sort_imp(arr, l, p-1)
        quick_sort_imp(arr, p+1, r)
