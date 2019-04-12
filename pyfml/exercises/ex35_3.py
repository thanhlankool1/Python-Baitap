#!/usr/bin/env python3


def solve(N):
    '''Creates a list which contains N first even integers. ``[2, 4 ...]``
    Must: use list comprehension
    Tips: list comprehension always create new list
    '''
    result = [x for x in range(2 * (N + 1)) if x % 2 == 0 and x != 0]
    return result


def main():
    print(solve(6))


if __name__ == "__main__":
    main()
