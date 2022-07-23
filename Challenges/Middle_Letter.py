def mid(param):
    length = len(param)
    int_type = length%2
    if int_type == 0:
        return ''
    else:
        val = int(length/2)
        return param[val:val+1]