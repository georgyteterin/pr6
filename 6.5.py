#t=[1, 2, 3, 4, 5, 6, 7, 8, 2, 45, 16,7]
t=[1, 2, 3, 4, 5, 6, 7, 8, 9]
a='abc'

def Is_sorted(t):

    if (isinstance(t, str)):
        t_split = []
        t_split[:]=t
        print(t_split)
        return t_split == sorted(t)

    return (t == sorted(t))


print(Is_sorted(t))