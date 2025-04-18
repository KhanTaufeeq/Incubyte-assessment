def add_strings(s):
    if s == '':
        return 0
    sum_num = 0
    splitted_string = s.split(',')

    for i in splitted_string:
        sum_num += int(i)

    return sum_num
