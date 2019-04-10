#!/usr/bin/env python3


def solve():
    '''Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    '''
    li1 = [(a,b,c) for a in range(11) for b in range(11) for c in range(11)]
    li2 = [(a,b,c) for (a,b,c) in li1 if a + b + c == 24]
    result = [(a,b,c) for (a,b,c) in li2 if a**2 + b**2 == c**2]

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
