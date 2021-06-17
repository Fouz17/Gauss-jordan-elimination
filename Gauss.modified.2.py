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

for i in range(numberOfEq-1):
    # IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
    if(linearEquations[i][i] > 1 or linearEquations[i][i] < -1):
        x = linearEquations[i][i]
        # LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
        for ii in range(len(linearEquations[i])):
            y = linearEquations[i][ii]
            linearEquations[i][ii] = y/x

    for j in range(i+1, numberOfEq, 1):

        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        d = linearEquations[j][i]

        for k in range(len(linearEquations[0])):

            a = linearEquations[j][k]  # THIS IS EQUAL TO D
            b = linearEquations[i][k]   # THIS IS EQUAL TO C

            linearEquations[j][k] = a-(d*b)

# --------------------------------------------------------------------------------------------------------------------------------------
# IF LAST ELEMENT OF LAST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
if(linearEquations[numberOfEq-1][numberOfCoef-2] != 1):
    x = linearEquations[numberOfEq-1][numberOfCoef-2]
    # LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
    for i in range(len(linearEquations[0])):
        y = linearEquations[numberOfEq-1][i]
        linearEquations[numberOfEq-1][i] = y/x


for i in range(numberOfEq - 1, 0, -1):

    for j in range(i-1, -1, -1):

        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        d = linearEquations[j][i]

        for k in range(numberOfCoef-1, -1, -1):

            # THIS IS EQUAL TO D IN FIRST LOOP
            a = linearEquations[j][k]
            # THIS IS EQUAL TO C IN FIRST LOOP
            b = linearEquations[i][k]

            result = a-(d*b)
            linearEquations[j][k] = result  # a-(d*b)

for i in range(len(linearEquations)):
    print('\n'+chr(ord('z') + 1 - numberOfEq+i)+'=' +
          str(linearEquations[i][numberOfCoef-1])+'\n')