# linearEquations = [              # 3 EQUATIONS WITH 3 CO EFFICIENTS
#     [1.0,3.0,1.0,10.0],
#     [1.00,-2.00,-1.0,-6.0],
#     [2.0,1.0,2.0,10.0]
#     ]
# linearEquations = [              # 2 EQUATIONS WITH 2 CO EFFICIENTS
#     [1.00,1.00,2.0],
#     [-1.0,2.0,1.0],
#     ]
# linearEquations = [              # 3 EQUATIONS WITH 3 CO EFFICIENTS
#     [1.0,10.0,-1.0,10.0],
#     [10.00,1.00,1.0,12.0],
#     [1.0,-2.0,10.0,9.0]
#     ]

linearEquations = [              # 4 EQUATIONS WITH 4 CO EFFICIENTS
    [1.00,1.00,1.0,1.0,4.0],
    [1.0,2.0,-1.0,1.0,3.0],
    [3.0,-2.0,5.0,4.0,10.0],
    [1.0,2.0,3.0,4.0,10.0]
    ]
#------------------------------------------------------------------------------------------------------------------

if(linearEquations[0][0] != 1): #IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
    x = linearEquations[0][0]
    for i in range(len(linearEquations[0])): #LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
        y = linearEquations[0][i]
        linearEquations[0][i] = y/x

numberOfEq = len(linearEquations) #CHECKING NUMBERSS OF EQUATION
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

#--------------------------------------------------------------------------------------------------------------------------------------
if(linearEquations[numberOfEq-1][numberOfCoef-2] != 1): #IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
    x = linearEquations[numberOfEq-1][numberOfCoef-2]
    for i in range(len(linearEquations[0])): #LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
        y = linearEquations[numberOfEq-1][i]
        linearEquations[numberOfEq-1][i] = y/x


index = numberOfEq - 1
firstLoop = 0
while(index > firstLoop):
    
    # print('-----------first---------------')
    # print(index)
    middleLoopLimit = 0
    middleLoop = index - 1 #CHECKING NUMBERSS OF EQUATION
    
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
            a = linearEquations[middleLoop][numberOfCoef - 1]  # THIS IS EQUAL TO D IN FIRST LOOP
            b = linearEquations[index][numberOfCoef - 1]   # THIS IS EQUAL TO C IN FIRST LOOP
            # linearEquations[middleLoopLimit][InnerLoop] = linearEquations[middleLoopLimit][InnerLoop]-linearEquations[firstLoop][InnerLoop]
            result = a-((d*b)/c)
            linearEquations[middleLoop][numberOfCoef - 1] = result#a-((d*b)/c)
            # print(linearEquations[firstLoop][InnerLoop])
            # print(numberOfCoef-1)
            
            numberOfCoef = numberOfCoef - 1
        middleLoop = middleLoop - 1
    index = index - 1
for i in range(len(linearEquations)):
    print(linearEquations[i])