#execfile("./1. Setup/HelloWorld.py")

#execfile("./2. Datatypes/datatypes.py")


def mid(param):
    length = len(param)
    int_type = length%2
    if int_type == 0:
        return ''
    else:
        val = int(length/2)
        return param[val:val+1]

print(mid("abc"))