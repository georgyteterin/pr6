# не разобрался как поменять переменную t ведь в функции у нас меняется только локальная перемееная, а глобальная менятся не будет

global t
t=[[1, 2, 3, 4], 5, 6, 7, 8, [2, 45, 16,7]]

def middle(t):
    result=[]
    for j in range(1, (len(t)-1)):
        result.append(t[j])
    t=result
    print(t)

print(middle(t), t)