#!/usr/bin/env python3

data = {'first_50': 1230, 'from_51_to_100': 1530, 'above_100': 1786}


def calculate_cost(usage, prices):
    '''Tính tiền điện (integer)
    với giá tiền cho bởi đề bài, số điện tiêu thụ `usage`
    '''
    # Viết code tính toán vào đây
    # for i in idata['usages']:
    if int(usage) < 50:
        result = int(usage) * prices['first_50']
    elif int(usage) >50 and int(usage) < 100:
        result = (50 * prices['first_50']) + (int(usage) - 50) * prices['from_51_to_100']
    else :
        result = (50 * prices['first_50']) +(
            (50 * prices['from_51_to_100']) +(int(usage) - 100) *prices['above_100'])
    return result

def solve(input_data):

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

    # Bài này làm mẫu, gọi function học viên định nghĩa với input để
    # tính kết quả.
    # Các bài còn lại học viên tự định nghĩa function và gọi function để
    # tính toán kết quả `result`
    result = [(i[0].title(), calculate_cost(i[1], input_data['prices']))
              for i in input_data['usages']]

    return result


def main():
    '''
    Cho tiền điện sinh hoạt được tính theo công thức:

    - 50 số đầu: 1230 VND/số.
    - 50 số tiếp: 1530 VND/số.
    - Các số tiếp theo: 1786 VND/số.
    '''
    idata = {'usages': [('nam', '1'), ('pikalong', '29'),
                        ('phan quan', '1235'), ('maria', '69'),
                        ('trump', '100')],
             'prices': data}
    print(solve(idata))


if __name__ == "__main__":
    main()
