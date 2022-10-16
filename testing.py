def buggy(arg, l=[]):
    l.append(arg)
    print(l)


buggy(9)
buggy(0)


def arg_test(var1, var2, *args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


arg_test(1, 2, (1, 2, 3), {1, 2, 3}, {'aa': 'aa'}, a='a', b='b')

args = (1, 2, 3, 4)
print(type([*args][0]))


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


print_data(list(range(100)), start=90, end=99)

