#!/usr/bin/env python3


def solve(N):
    '''Create a list which contains N lists,
    each list contains N numbers from 0->N-1.

    E.g with N = 10:

    matrix = [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      ...
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    Then returns a string looks like below

      0********0
      *1******1*
      **2****2**
      ***3**3***
      ****44****
      ****55****
      ***6**6***
      **7****7**
      *8******8*
      9********9
    '''

    matrix = [list(range(10)) for x in range(10)]
    for idx_row, val_row in enumerate(matrix):
        for idx, _ in enumerate(val_row):
            if idx == idx_row or idx == N - idx_row - 1:
                val_row[idx] = str(idx_row)
            else:
                val_row[idx] = '*'
    result = '\n'.join(''.join(i) for i in matrix)
    return result

    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
