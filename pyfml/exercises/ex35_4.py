#!/usr/bin/env python3


def solve(N):
    '''Creates a string which contains N random ASCII letters.

    To create 1 letter, use::

      import random
      import string
      random.choice(string.ascii_letters)

    Must: use list comprehension
    Tips: list comprehension always create new list
    '''
    import random
    import string
    result = [random.choice(string.ascii_letters) for x in range(N)]
    return result


def main():
    print(solve(16))


if __name__ == "__main__":
    main()
