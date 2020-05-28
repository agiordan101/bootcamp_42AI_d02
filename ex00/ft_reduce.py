def ft_reduce(function_to_apply, list_of_inputs):
    ret = list_of_inputs[0]
    for i in list_of_inputs[1:]:
        ret = function_to_apply(ret, i)
    return ret

def ft(x, y):
    return x + y

print(ft_reduce(ft, [1, -2, 3, -10, 9]))
