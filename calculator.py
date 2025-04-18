import re

def add_strings(s):
    if s == '':
        return 0
    splitted_string = re.split(r'[\n,]',s)

    result = add_multiple_number_string(splitted_string)

    return result


def add_multiple_number_string(s):
    sum_num = 0
    for i in s:
        sum_num += int(i)
    return sum_num
