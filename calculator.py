import re

def add_strings(s):
    sum_num = 0
    delimiter = s[2]

    sub_string = s.split('\n')
    numbers_sub_string = sub_string[1]

    delimiter = re.escape(delimiter)

    splitted_string = re.split(delimiter, numbers_sub_string)

    for i in splitted_string:
            sum_num += int(i)

    return sum_num
