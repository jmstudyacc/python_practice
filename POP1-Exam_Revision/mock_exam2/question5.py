# 13198061

def trim_matrix(M):
    # non-fruitful function so it does not return anything new
    mini = 0
    for i in range(len(M)-1):
        a = len(M[i])
        b = len(M[i+1])
        if a < b:
            mini = a
        else:
            mini = b

    for j in range(len(M)):
        if len(M[j]) + 1 > mini:
            del M[j][mini:]
