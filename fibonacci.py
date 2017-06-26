

def fibc(num):
    if num <= 0:
        return 0
    cur, nxt = 1, 1
    for i in range(num - 1):
        cur, nxt = nxt, cur + nxt
    return cur


def fibr(num):
    if num <= 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return fibr(num - 1) + fibr(num - 2)


if __name__ == '__main__':
    print(fibc(16))
    print(fibr(16))
