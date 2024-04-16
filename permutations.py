def permutations(array):
    if len(array) == 0:
        return [[]]

    if len(array) == 1:
        return [array]

    lst_tmp = []

    for i in range(len(array)):
        m = array[i]
        rem_arr = array[:i] + array[i + 1:]
        for cmb in permutations(rem_arr):
            lst_tmp.append([m] + cmb)
    return lst_tmp

print(permutations(['a', 'b', 'c']))

