s=list(input("insert please ", ))
sort_s=sorted(s)
def same(s):
  for i in range(len(sort_s)-1):
    if sort_s[i]==sort_s[i+1]:
      cond= True
      break
    else:
      cond=False
  return cond
same(s)