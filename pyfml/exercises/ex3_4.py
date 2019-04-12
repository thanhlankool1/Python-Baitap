#!/usr/bin/env python3

'''
Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.

Ví dụ::

  input_data = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input_data = 'maria.data.mp9'
  output = 'maria.data'
'''


def solve(input_data):
    '''Trả về tên file sau khi loại bỏ phần mở rộng

    :param input_data: tên file bất kì
    :rtype: str
    '''
    lenght = len(input_data)
    s = input_data[:lenght - (lenght - input_data.rfind('.'))]
    result = input_data = s
    return result


def main():
    data = 'maria.data.mp9'
    print(solve(data))


if __name__ == "__main__":
    main()
