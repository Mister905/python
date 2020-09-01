def digital_root(n):
    if (n >=10):
        root = 0
        n_string = str(n)
        n_string_char_list = list(n_string)
        n_int_list = list()
        for i in range(len(n_string_char_list)):
            n_int_list.append(int(n_string_char_list[i]))
        for i in range(len(n_int_list)):
            root += n_int_list[i]
        if (root < 10):
            return root
        else:
            return digital_root(root)
    else:
        return n

if __name__ == '__main__':

    print(digital_root(16))

    print(digital_root(942))

    print(digital_root(132189))

    print(digital_root(493193))