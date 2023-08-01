def disjoint_intervals(inp):
    aux = []
    for a in range(0,len(inp)):
        for j in range(0,len(inp)):
            print(a)
        #'''case1: A esta contido em B'''
            if  inp[a][0]>=inp[j][0] and inp[a][1]<=inp[j][1]:
                inp[a][0]=inp[j][0]
                inp[a][1]=inp[j][1]
        #case2: ha intececcao mas nem A esta contido em B e nem vice-versa.
            elif inp[a][0]<=inp[j][0] and inp[a][1]<=inp[j][1] and inp[a][1]>=inp[j][0]:
                inp[j][0]=inp[a][0]
                inp[a][1]=inp[j][1]
            elif inp[a][0]>=inp[j][0] and inp[a][1]>=inp[j][1] and inp[j][1]>=inp[a][0]:
                inp[a][0]=inp[j][0]
                inp[j][1]=inp[a][1]
    #limpa os elementos duplicados
    for i in range(0, len(inp)):
        if inp[i] not in aux:
            aux.append(inp[i])
    aux.sort()
    return aux

a = disjoint_intervals([[2, 5], [1, 3], [7, 10], [10, 15], [-3.5, -1.5], [20, 22], [12, 20]])
print(a)

