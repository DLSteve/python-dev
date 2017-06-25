

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


if __name__ == "__main__":
    ar = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    bubblesort(ar)
    print(ar)

    ar = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    insertion_sort(ar)
    print(ar)
