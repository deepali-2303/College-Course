low = [0, 0.1, 0.3]
medium = [0.5, 0.57, 0.6]
high = [0.8, 0.9, 1]

def AxB(a,b):
    axb = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            axb[i][j] = min(a[i], b[j])
    return axb

def max_min(a,b):
    aob = [[0] * 3 for _ in range(3)]
    for i in range (3):
        
        for j in range(3):
            temp = [0] * 3
            for k in range(3):
                temp[k] = min(a[i][k],b[k][j])
                # print(temp)
            aob[i][j] = max(temp)    
    return aob


def max_prod(a,b):
    aob = [[0] * 3 for _ in range(3)]
    for i in range (3):
        
        for j in range(3):
            temp = [0] * 3
            for k in range(3):
                temp[k] = (a[i][k]*b[k][j])
                # print(temp)
            aob[i][j] = max(temp)    
    return aob
    
        
r = AxB(low,medium)
s = AxB(medium,high)
ans = max_min(r,s)
prod = max_prod(r,s)

print("R  = ", r)
print("S = ", s)
print("Max_min = ", ans)
print("Max_prod = ",prod)