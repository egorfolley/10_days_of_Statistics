from math import e, factorial

if __name__ == '__main__':
    valA, valB = list(map(float, input().split()))

    costA = 160 + 40 * (valA + valA ** 2)
    costB = 128 + 40 * (valB + valB ** 2)
    print(round(costA, 3), round(costB, 3), sep = '\n')

