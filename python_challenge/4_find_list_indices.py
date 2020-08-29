def find_list_indices(list, value):
    indices = list()
    for i in range(len(list)):
        if list[i] == value:
            indices.append([i])