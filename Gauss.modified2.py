a = int(input('number of equations: '))

linearEquations = []

for i in range(a):
    equation = []
    for j in range(a+1):
        var = chr(123-a+j)
        if(j < a):
            b = float(input('Enter coefficient of '+var+': '))
        else:
            b = float(input('Enter constant value: '))
        equation.append(b)
    linearEquations.append(equation)
# ------------------------------------------------------------------------------------------------------------------

numberOfEq = len(linearEquations)  # CHECKING NUMBERS OF EQUATION
numberOfCoef = len(linearEquations[0])
firstLoop = 0
while(firstLoop < numberOfEq-1):
    # IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
    if(linearEquations[firstLoop][firstLoop] > 1 or linearEquations[firstLoop][firstLoop] < -1):
        x = linearEquations[firstLoop][firstLoop]
        # LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
        for i in range(len(linearEquations[firstLoop])):
            y = linearEquations[firstLoop][i]
            linearEquations[firstLoop][i] = y/x

    middleLoop = firstLoop + 1

    while(middleLoop < numberOfEq):

        InnerLoop = 0

        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        d = linearEquations[middleLoop][firstLoop]

        while (InnerLoop < len(linearEquations[0])):

            a = linearEquations[middleLoop][InnerLoop]  # THIS IS EQUAL TO D
            b = linearEquations[firstLoop][InnerLoop]

            linearEquations[middleLoop][InnerLoop] = a-(d*b)

            InnerLoop = InnerLoop + 1
        middleLoop = middleLoop + 1
    firstLoop = firstLoop + 1

# --------------------------------------------------------------------------------------------------------------------------------------
# IF LAST ELEMENT OF LAST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
if(linearEquations[numberOfEq-1][numberOfCoef-2] != 1):
    x = linearEquations[numberOfEq-1][numberOfCoef-2]
    # LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
    for i in range(len(linearEquations[0])):
        y = linearEquations[numberOfEq-1][i]
        linearEquations[numberOfEq-1][i] = y/x


index = numberOfEq - 1
while(index > 0):

    middleLoop = index - 1  # CHECKING NUMBERSS OF EQUATION

    while(middleLoop >= 0):

        InnerLoop = 0
        numberOfCoef = len(linearEquations[0])

        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        d = linearEquations[middleLoop][index]

        while (numberOfCoef-1 >= 0):

            # THIS IS EQUAL TO D IN FIRST LOOP
            a = linearEquations[middleLoop][numberOfCoef - 1]
            b = linearEquations[index][numberOfCoef - 1]

            result = a-(d*b)
            linearEquations[middleLoop][numberOfCoef -
                                        1] = result  # a-(d*b)

            numberOfCoef = numberOfCoef - 1
        middleLoop = middleLoop - 1
    index = index - 1

# print(linearEquations)

for i in range(len(linearEquations)):
    if(linearEquations[i][numberOfCoef-1] == 0):
        y = (abs(linearEquations[i][numberOfCoef-1]))
    else:
        y = linearEquations[i][numberOfCoef-1]
    print('\n'+chr(ord('z') + 1 - numberOfEq+i)+'=' +
          str(y)+'\n')