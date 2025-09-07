n = 5
for i in range(1, n+1):
    if i == 0 or i == n-1:
        print("*"*i)
    else:
        print("*"+" "*(i-2)+"*")