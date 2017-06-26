

def bubblesort(array):
    for i in range(len(array)):
        for k in range(len(array) - 1, i, -1):
            if array[k] < array[k - 1]:
                array[k], array[k - 1] = array[k - 1], array[k]


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1


if __name__ == "__main__":
    ar = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    bubblesort(ar)
    print(ar)

    ar = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    insertion_sort(ar)
    print(ar)
    
    ar = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    merge_sort(ar)
    print(ar)
