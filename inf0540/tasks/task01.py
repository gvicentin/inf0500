#!/usr/bin/env python3


def task01(val1, val2):
    sum = val1 + val2
    print(f"O resultado da soma é {sum}")
    print(f"O cubo de valor 1 é {val1 ** 3}")
    print(f"O cubo de valor 2 é {val2 ** 3}")


if __name__ == "__main__":
    val1 = int(input("Valor 1: "))
    val2 = int(input("Valor 2: "))
    task01(val1, val2)
