#!/usr/bin/env python3
'''
Gợi ý: có thể dùng enumerate()
https://docs.python.org/3/library/functions.html#enumerate
'''


data = ["I", "Love", "You", "Chiu", "Chiu"]


def solve(input_data):
    '''Trả về 1 `list` các `list` theo định dạng sau:

        result = [[1, "I"], [2, "Love"], [3, "You"], [4, "Chiu"], [5, "Chiu"]]

    :rtype: list
    '''
    # result = None
    s = []
    for index, value in enumerate(input_data, 1):
        s.append([index, value])

    result = s
    return result


def main():
    # xử lí in ra theo yêu cầu đề bài bên dưới
    result = solve(data)
    print(result)
    pass


if __name__ == "__main__":
    main()
