#!/usr/bin/env python3


def solve(text):
    '''Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]

    NOTE: không dùng `re` library
    '''
    result = []
    for i in text:
        if i.isdigit():
            result.append(int(i))
    return result


def main():
    ss = 'Bé lên 3 bé đi lớp 4'
    print(solve(ss))
    assert solve(ss) == [3, 4]


if __name__ == "__main__":
    main()
