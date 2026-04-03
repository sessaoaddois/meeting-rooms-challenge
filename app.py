def checaConflito(array: list[list]) -> int:
    salas= 0
    if (len(array) == 0): 
        return 0
    elif (len(array[0]) == 0):
        return 0
    for i in range(0,len(array)):
        if(array[i][1] > array[-1][0]):
            salas+=1
    return salas
    
input = sorted([[0,10],[10,20]])
salas = checaConflito(input)
print(salas)