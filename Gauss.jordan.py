# linearEquations = [              # 3 EQUATIONS WITH 3 CO EFFICIENTS
#     [1.0, 3.0, 1.0, 10.0],          # x = 1, y = 2, z = 3
#     [1.00, -2.00, -1.0, -6.0],
#     [2.0, 1.0, 2.0, 10.0]
# ]
linearEquations = [              # 3 EQUATIONS WITH 3 CO EFFICIENTS
    [1.0, 1.0, 1.0, 3.0],        # x = 1, y = 1, z = 1
    [3.00, 1.00, -1.0, 3.0],
    [2.0, -2.0, 2.0, 2.0]
]
# linearEquations = [              # 2 EQUATIONS WITH 2 CO EFFICIENTS
#     [1.00,1.00,2.0],             # x = 1, y = 1
#     [-1.0,2.0,1.0],
#     ]
# linearEquations = [              # 3 EQUATIONS WITH 3 CO EFFICIENTS
#     [1.0,10.0,-1.0,10.0],        # x = 1, y = 1, z = 1
#     [10.00,1.00,1.0,12.0],
#     [1.0,-2.0,10.0,9.0]
#     ]

# linearEquations = [              # 4 EQUATIONS WITH 4 CO EFFICIENTS
#     [1.00,1.00,1.0,1.0,4.0],     # w = 1, x = 1, y = 1, z = 1
#     [1.0,2.0,-1.0,1.0,3.0],
#     [3.0,-2.0,5.0,4.0,10.0],
#     [1.0,2.0,3.0,4.0,10.0]
#     ]
# ------------------------------------------------------------------------------------------------------------------

# IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
if(linearEquations[0][0] != 1):
    x = linearEquations[0][0]
    # LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
    for i in range(len(linearEquations[0])):
        y = linearEquations[0][i]
        linearEquations[0][i] = y/x

numberOfEq = len(linearEquations)  # CHECKING NUMBERSS OF EQUATION
numberOfCoef = len(linearEquations[0])
firstLoop = 0
while(firstLoop < numberOfEq-1):

    # print('-----------first---------------')
    # print(firstLoop)
    middleLoop = firstLoop + 1

    while(middleLoop < numberOfEq):

        # print('---------Middle--------')
        # print(middleLoop)
        InnerLoop = 0

        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        c = linearEquations[firstLoop][firstLoop]
        d = linearEquations[middleLoop][firstLoop]

        while (InnerLoop < len(linearEquations[0])):
            # print('---------Inner--------')
            a = linearEquations[middleLoop][InnerLoop]  # THIS IS EQUAL TO D
            b = linearEquations[firstLoop][InnerLoop]   # THIS IS EQUAL TO C
            # linearEquations[middleLoop][InnerLoop] = linearEquations[middleLoop][InnerLoop]-linearEquations[firstLoop][InnerLoop]
            linearEquations[middleLoop][InnerLoop] = a-((d*b)/c)
            # print(linearEquations[firstLoop][InnerLoop])
            # print(InnerLoop)

            InnerLoop = InnerLoop + 1
        middleLoop = middleLoop + 1
    firstLoop = firstLoop + 1

# print(linearEquations)
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
        c = linearEquations[index][index]
        d = linearEquations[middleLoop][index]

        while (numberOfCoef-1 >= InnerLoop):
            # print('---------Inner--------')
            # THIS IS EQUAL TO D IN FIRST LOOP
            a = linearEquations[middleLoop][numberOfCoef - 1]
            # THIS IS EQUAL TO C IN FIRST LOOP
            b = linearEquations[index][numberOfCoef - 1]
            # linearEquations[middleLoopLimit][InnerLoop] = linearEquations[middleLoopLimit][InnerLoop]-linearEquations[firstLoop][InnerLoop]
            result = a-((d*b)/c)
            linearEquations[middleLoop][numberOfCoef -
                                        1] = result  # a-((d*b)/c)
            # print(linearEquations[firstLoop][InnerLoop])
            # print(numberOfCoef-1)

            numberOfCoef = numberOfCoef - 1
        middleLoop = middleLoop - 1
    index = index - 1

# print(linearEquations)

for i in range(1, len(linearEquations)-1, 1):
    var = linearEquations[i][i]
    if(var != 1):
        value = linearEquations[i][len(linearEquations[0])-1]
        linearEquations[i][i] = var/var
        linearEquations[i][len(linearEquations[0])-1] = value/var

print(linearEquations)

# for i in range(len(linearEquations)):
#     print('value is: '+str(linearEquations[i][4]/linearEquations[i][i]))
for i in range(len(linearEquations)):
    print(chr(ord('z') + 1 - numberOfEq+i)+'='+str(linearEquations[i][numberOfCoef-1])+'\n')
