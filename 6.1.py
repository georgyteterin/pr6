t=[[1, 2, 3, 4], [2, 45, 16,7]]

def nested_sum(t):
    sum_t=0
    for j in range(len(t)):
        sum_t+=sum(t[j])
    return (sum_t)

print(nested_sum(t))
