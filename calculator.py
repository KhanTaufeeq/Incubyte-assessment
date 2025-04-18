import re

def add_strings(s):
    if s == '':
        return 0
    delimiter = s[2]

    sub_string = s.split('\n')

    sub_num_string = sub_string[1]

    delimiter = re.escape(delimiter)
    splitted_string = re.split(delimiter,sub_num_string)

    result = add_multiple_number_string(splitted_string)

    return result


def add_multiple_number_string(s):
    sum_num = 0
    for i in s:
        sum_num += int(i)
    return sum_num
