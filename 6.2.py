t=[[1, 2, 3, 4], [2, 45, 16,7]]

def cumsum(t):
    result=[]
    for j in range(len(t)):
        result.append(sum(t[j]))
    return (result)

print(cumsum(t))