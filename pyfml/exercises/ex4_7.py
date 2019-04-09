#!/usr/bin/env python3


def solve(year):
    '''Trả về tuple-2 chứa year và tên gọi can chi tương ứng. Các từ trong tên
    đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

      ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

      ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
       'tuất', 'hợi']

    Năm 2017 là năm "Đinh Dậu".
    '''
    ThienCan = ['canh','tân' ,'nhâm' , 'quý','giáp','ất', 'bính','đinh','mậu','kỷ']
    DiaChi = ['tý','sửu','dần', 'mão', 'thìn', 'tỵ' ,'ngọ' ,'mùi','thân','dậu','tuất','hợi']
    result = []
    y = ((2019 - year) % 12)
    print(y)
    year = str(year)
    s = year[len(year)-1]
    print(s)
    
    if y != 0:
        return result.append([int(year), ThienCan[int(s)],'',DiaChi[(11 - int(y))]])        
    else:
        return result.append([int(year), ThienCan[int(s)],DiaChi[11]])
    return result



def main():
    print("Năm {0} là năm {1}".format(*solve(1696)))


if __name__ == "__main__":
    main()
