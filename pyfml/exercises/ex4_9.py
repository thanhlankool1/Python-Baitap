#!/usr/bin/env python3
from functools import reduce


def solve(numbers):
    '''Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`
    '''
    assert isinstance(numbers, list)
    result = reduce(lambda x, y: x if x > y else y, numbers)
    return result


def main():
    print(solve([-1, 5, 9, 6, 2, 1]))


if __name__ == "__main__":
    main()
