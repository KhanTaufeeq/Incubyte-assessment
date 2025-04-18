import re

def add_strings(s):

    splitted_string = re.split(r'[,\n]', s)
    sum_num = 0
    for i in splitted_string:
        if i != '':
            sum_num += int(i)

    return sum_num
