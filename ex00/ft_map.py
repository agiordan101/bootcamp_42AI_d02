def ft_map(function_to_apply, list_of_inputs):
    ret = []
    for i in list_of_inputs:
        ret.append(function_to_apply(i))
    return ret

def ft(input):
    return input + 1

print(ft_map(ft, [1, 2, 3]))
