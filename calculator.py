import re

def add_strings(s):
    if s == '':
        return 0
    
    if s[0] == '/' and s[1] == '/':
        delimiter = s[2]
        sub_string = s.split('\n')
        sub_num_string = sub_string[1]
        delimiter = re.escape(delimiter)
        splitted_string = re.split(delimiter,sub_num_string)
        splitted_string = [n for n in splitted_string if n != '']
    
    else:
        splitted_string = re.split(r'[,\n]',s)

        is_negative(splitted_string)

    result = add_multiple_number_string(splitted_string)

    return result


def add_multiple_number_string(s):
    sum_num = 0
    for i in s:
        if int(i) > 1000:
            continue
        else:
            sum_num += int(i)
    return sum_num

def is_negative(s):
    negatives = [n for n in s if int(n) < 0]
    if negatives:
        raise ValueError (f"Negative numbers not allowed: {', '.join(negatives)}")
