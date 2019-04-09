#!/usr/bin/env python3


def solve(words):
    '''Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    '''
    Li = []
    Tong = 0
    for word in words:
        word = word.lower()
        for char in word:
            gt = ord(char) - 96
            Tong += gt
        Li.append(Tong)
        Tong = 0
        result = Li
    return result

def main():
    words = ['numpy', 'django', 'saltstack', 'discipline',
             'Python', 'FAMILUG', 'pymi',]

    print(solve(words))


if __name__ == "__main__":
    main()
