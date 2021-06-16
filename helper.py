a = int(input('number of equations: '))

linearEquations = []

for i in range(a):
    equation = []
    for j in range(a+1):
        var = chr(123-a+j)
        if(j < a):
            b = int(input('Enter coefficient of '+var+': '))
        else:
            b = int(input('Enter value: '))
        equation.append(b)
    linearEquations.append(equation)
# print(linearEquations)
# ------------------------------------------------------------------------------------------------------------------


numberOfEq = len(linearEquations)  # CHECKING NUMBERS OF EQUATION
numberOfCoef = len(linearEquations[0])
firstLoop = 0
while(firstLoop < numberOfEq-1):
    # IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
    if(linearEquations[firstLoop][firstLoop] > 1 and linearEquations[firstLoop][firstLoop] < -1):
        x = linearEquations[firstLoop][firstLoop]
        # LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
        for i in range(len(linearEquations[firstLoop])):
            y = linearEquations[firstLoop][i]
            linearEquations[firstLoop][i] = y/x
    # print('-----------first---------------')
    # print(firstLoop)
    middleLoop = firstLoop + 1

    while(middleLoop < numberOfEq):

        # print('---------Middle--------')
        # print(middleLoop)
        InnerLoop = 0

        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        d = linearEquations[middleLoop][firstLoop]

        while (InnerLoop < len(linearEquations[0])):
            # print('---------Inner--------')
            a = linearEquations[middleLoop][InnerLoop]  # THIS IS EQUAL TO D
            b = linearEquations[firstLoop][InnerLoop]   # THIS IS EQUAL TO C
            # linearEquations[middleLoop][InnerLoop] = linearEquations[middleLoop][InnerLoop]-linearEquations[firstLoop][InnerLoop]
            linearEquations[middleLoop][InnerLoop] = a-(d*b)
            # print(linearEquations[firstLoop][InnerLoop])
            # print(InnerLoop)

            InnerLoop = InnerLoop + 1
        middleLoop = middleLoop + 1
    firstLoop = firstLoop + 1
# for i in range(len(linearEquations)):
#     print(linearEquations[i])
# --------------------------------------------------------------------------------------------------------------------------------------
# IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
if(linearEquations[numberOfEq-1][numberOfCoef-2] != 1):
    x = linearEquations[numberOfEq-1][numberOfCoef-2]
    # LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
    for i in range(len(linearEquations[0])):
        y = linearEquations[numberOfEq-1][i]
        linearEquations[numberOfEq-1][i] = y/x


index = numberOfEq - 1
firstLoop = 0
while(index > firstLoop):

    # print('-----------first---------------')
    # print(index)
    middleLoopLimit = 0
    middleLoop = index - 1  # CHECKING NUMBERSS OF EQUATION

    while(middleLoop >= middleLoopLimit):

        # print('---------Middle--------')
        # print(middleLoop)
        InnerLoop = 0
        numberOfCoef = len(linearEquations[0])

        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        d = linearEquations[middleLoop][index]

        while (numberOfCoef-1 >= InnerLoop):
            # print('---------Inner--------')
            # THIS IS EQUAL TO D IN FIRST LOOP
            a = linearEquations[middleLoop][numberOfCoef - 1]
            # THIS IS EQUAL TO C IN FIRST LOOP
            b = linearEquations[index][numberOfCoef - 1]

            result = a-(d*b)
            linearEquations[middleLoop][numberOfCoef -
                                        1] = result  # a-(d*b)

            numberOfCoef = numberOfCoef - 1
        middleLoop = middleLoop - 1
    index = index - 1

for i in range(len(linearEquations)):
    print(chr(ord('z') + 1 - numberOfEq+i)+'='+str(linearEquations[i][i])+'\n')
