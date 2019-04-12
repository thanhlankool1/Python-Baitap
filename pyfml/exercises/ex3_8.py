#!/usr/bin/env python3


def solve(input_data):
    '''Kiểm tra input_data có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 1 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    '''

    s = list(input_data.lower().strip().replace(' ', ''))
    if s == s[::-1] and len(s) > 2:
        return True
    else:
        return False
    return


def main():
    print(solve('Able was I ere I saw Elba'))


if __name__ == "__main__":
    main()
