def ft_filter(function_to_apply, list_of_inputs):
    ret = []
    for i in list_of_inputs:
        if function_to_apply(i):
            ret.append(i)
    return ret

def ft(input):
    if input >= 0:
        return True
    else:
        return False

print(ft_filter(ft, [1, -2, 3, -10, 9]))
