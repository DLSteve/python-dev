

def reverse_string(inpt):
    rev_str = ''
    for i in range(len(inpt) - 1, -1, -1):
        rev_str += inpt[i]
    return rev_str


def word_count(inpt):
    c_list = inpt.split()
    return len(c_list)


def series(num, count=0):
    count += 1
    if num == 1:
        return count
    if num % 2 == 0:
        num = num / 2
        return series(num, count)
    else:
        num = num * 3 + 1
        return series(num, count)


def longest_series():
    number = 0
    count = 0
    for i in range(1, 100):
        c = series(i)
        if c > count:
            count = c
            number = i

    return 'Number: {} has {} iterations in the series.'.format(number, count)


def remove_duplicates(string):
    strng = list()
    for c in string:
        if c not in strng:
            strng.append(c)
    return ''.join(strng)


def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

if __name__ == '__main__':
    print(reverse_string('Hi how are you!!'))

    text = ('The method split() returns a list of all the words in the string, using str as the separator (splits on'
            ' all whitespace if left unspecified), optionally limiting the number of splits to num.')

    print(word_count(text))

    print(longest_series())

    print(remove_duplicates('geeksforgeeks'))

    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binary_search(testlist, 19))
