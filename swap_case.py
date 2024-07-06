def swap_case(s):
    s_list = list(s)
    change_s = []
    for i in s_list:
        if i.isalpha() and i.isupper():
            change_s.append(i.lower())
        elif i.isalpha and i.islower():
            change_s.append(i.upper())
        else:
            change_s.append(i)
    return "".join(change_s)
