#!/usr/bin/env python3


def create_tuple_N(iterable, N):
    # Sửa tên, set giá trị return
    result = []
    for i in range(len(iterable)//N):
        result.append(tuple(iterable[(N*i):((i+1)*N)]))
    return result



def solve(iterable, N):
    ''' Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    '''
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

    # sửa thành tên function phù hợp
    result = create_tuple_N(iterable, N)

    return result


def main():
    li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
    print(solve(li, 2))


if __name__ == "__main__":
    main()
