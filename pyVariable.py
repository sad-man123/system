def good_dict(dict1):
    line = ""
    num_1 = 0
    array = []
    word = ""
    str_dict1 = str(dict1)
    str_dict1 = str_dict1.replace(", ", ",\n")
    str_dict1 = str_dict1.replace("{", "{\n")
    str_dict1 = str_dict1.replace("}", "\n}\n")
    str_dict1 = str_dict1.replace("    }", "}")
    str_dict1 = str_dict1.replace("[", "[\n")
    str_dict1 = str_dict1.replace("]", "\n]\n")
    str_dict1 = str_dict1.replace("    ]", "]")
    for i in str_dict1:
        if i == "\n":
            array.append(word)
            word = ""
        else:
            word += i
    boolean = True
    for ii in array:
        if "{" in ii or "[" in ii:
            num_1 += 1
        elif "}" in ii or "]" in ii:
            num_1 -= 1
        if boolean:
            line += f"{ii}\n"
            boolean = False
        else:
            if "{" in ii or "[" in ii:
                num_1 -= 1
            line += f"{'    ' * num_1}{ii}\n"
            if "{" in ii or "[" in ii:
                num_1 += 1
    line = line.replace("\n    \n", "\n")
    line = line.replace("'", '"')
    line = line.replace("\n    ,", ",")
    return line


def words(line, clear=None):
    if clear is None:
        simbols = " ,./?!#@%^&*()+-=[]{}"
    else:
        simbols = clear
    array = []
    word = ""
    for i in simbols:
        line = line.replace(i, "")
    line += clear[0]
    for i in line:
        if i == " ":
            array.append(word)
            word = ""
        else:
            word += i
    return array


def min_int(array):
    num_1 = array[0]
    for i in array:
        if num_1 > i:
            num_1 = i
    return num_1


def amx_int(array):
    num_1 = array[0]
    for i in array:
        if num_1 < i:
            num_1 = i
    return num_1


def min_str(array):
    num_1 = 0
    num_2 = 0
    for ii in array[0]:
        num_1 += 1
    word = array[0]
    for i in array:
        for ii in i:
            num_2 += 1
        if num_1 > num_2:
            num_1 = num_2
            word = i
        num_2 = 0
    return word


def max_str(array):
    num_1 = 0
    num_2 = 0
    for ii in array[0]:
        num_1 += 1
    word = array[0]
    for i in array:
        for ii in i:
            num_2 += 1
        if num_1 < num_2:
            num_1 = num_2
            word = i
        num_2 = 0
    return word