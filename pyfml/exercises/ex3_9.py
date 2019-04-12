#!/usr/bin/env python3

'''
a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]
'''


def solve():
    '''Trả về list chứa các list là các bộ số thỏa mãn đề bài

    Ví dụ:
        [[9, 1, 1], ..., [1, 9, 1]]

    Lưu ý: kết quả từng list con trả về với a giảm dần, b và c tăng dần
    '''

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    s = []
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for a in data[::-1]:
        for b in data:
            for c in data:
                if a + b / c == 10:
                    s.append([a, b, c])
    result = s
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
