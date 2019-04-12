#!/usr/bin/env python3

from functools import reduce


def solve(numbers):
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
    result = []
    sum = reduce(lambda x1, x2: x1 + x2, numbers)
    product = reduce(lambda x1, x2: x1 * x2, numbers)
    result.append((sum, product))
    return tuple(result[0])


def main():
    # Cho list numbers chứa các số chẵn từ -10 đến 10, trừ số 0.
    numbers = range(-10, 11, 2)  # step=2
    numbers = list(numbers)
    numbers.remove(0)

    result = solve(numbers)
    print(result)
    assert result == (0, -14745600)


if __name__ == "__main__":
    main()
