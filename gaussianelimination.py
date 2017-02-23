def gaussy(A, b, n):
    l = [0 for x in range(n)]
    s = [0.0 for x in range(n)]
    for i in range(n):
        l[i] = i
        smax = 0.0
        for j in range(n):
            if abs(A[i][j]) > smax:
                smax = abs(A[i][j])
        s[i] = smax

    for i in range(n - 1):
        rmax = 0.0
        for j in range(i, n):
            ratio = abs(A[l[j]][i]) / s[l[j]]
            if ratio > rmax:
                rmax = ratio
                rindex = j
        temp = l[i]
        l[i] = l[rindex]
        l[rindex] = temp
        for j in range(i + 1, n):
            multiplier = A[l[j]][i] / A[l[i]][i]
            for k in range(i, n):
                A[l[j]][k] = A[l[j]][k] - multiplier * A[l[i]][k]
            b[l[j]] = b[l[j]] - multiplier * b[l[i]]

    x = [0.0 for y in range(n)]
    x[n - 1] = b[l[n - 1]] / A[l[n - 1]][n - 1]
    for j in range(n - 2, -1, -1):
        summ = 0.0
        for k in range(j + 1, n):
            summ = summ + A[l[j]][k] * x[k]
        x[j] = (b[l[j]] - summ) / A[l[j]][j]

    print ("The solution vector is [",)
    for i in range(n):
        if i != (n - 1):
            print(x[i], ",",)
        else:
            print(x[i], "].")

matrix0 = [[3.0, -13.0, 9.0, 3.0], [-6.0, 4.0, 1.0, -18.0], [6.0, -2.0, 2.0, 4.0], [12.0, -8.0, 6.0, 10.0]]
vector0 = [-19.0, -34.0, 16.0, 26.0]

matrix1 = [[3.0, 2.0, -5.0], [2.0, -3.0, 1.0], [1.0, 4.0, -1.0]]
vector1 = [0.0, 0.0, 4.0]

gaussy(matrix0, vector0, 4)
gaussy(matrix1, vector1, 3)
