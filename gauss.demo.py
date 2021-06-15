# linearEquations = [              # 3 EQUATIONS WITH 3 CO EFFICIENTS
#     [10.00,1.00,1.0,12.0],
#     [1.0,10.0,-1.0,10.0],
#     [1.0,-2.0,10.0,9.0]
#     ]
linearEquations = [              # 3 EQUATIONS WITH 3 CO EFFICIENTS
    [1.0,10.0,-1.0,10.0],
    [10.00,1.00,1.0,12.0],
    [1.0,-2.0,10.0,9.0]
    ]
# linearEquations = [              # 4 EQUATIONS WITH 4 CO EFFICIENTS
#     [10.00,1.00,1.0,12.0,1],
#     [1.0,10.0,-1.0,10.0,1],
#     [1.0,-2.0,10.0,9.0,1],
#     [1,2,3,4,5]
#     ]
# linearEquations = [              # 2 EQUATIONS WITH 2 CO EFFICIENTS
#     [1.00,1.00,2.0],
#     [-1.0,2.0,1.0],
#     ]

if(linearEquations[0][0] != 1): #IF 1ST ELEMENT OF 1ST EQUATION IS NOT EQUAL TO 1 THEN CONVERTING IT.....
    x = linearEquations[0][0]
    for i in range(len(linearEquations[0])): #LOOP FOR DIVIDING EVERY ELEMENT OF 1ST LIST BY 1ST ELEMENT OF THAT LIST
        y = linearEquations[0][i]
        linearEquations[0][i] = y/x

numberOfEq = len(linearEquations) #CHECKING NUMBERSS OF EQUATION
firstLoop = 0
while(firstLoop < numberOfEq-1):
    
    print('-----------first---------------')
    print(firstLoop)
    middleLoop = firstLoop + 1
    
    while(middleLoop < numberOfEq):
        
        print('---------Middle--------')
        print(middleLoop)
        InnerLoop = 0
        
        # VARIABLES FOR ROW MULTIPLICATION OPERATION
        c = linearEquations[firstLoop][firstLoop]
        d = linearEquations[middleLoop][firstLoop]

        while (InnerLoop < len(linearEquations[0])):
            print('---------Inner--------')
            a = linearEquations[middleLoop][InnerLoop]  # THIS IS EQUAL TO D
            b = linearEquations[firstLoop][InnerLoop]   # THIS IS EQUAL TO C
            # linearEquations[middleLoop][InnerLoop] = linearEquations[middleLoop][InnerLoop]-linearEquations[firstLoop][InnerLoop]
            linearEquations[middleLoop][InnerLoop] = a-((d*b)/c)
            # print(linearEquations[firstLoop][InnerLoop])
            print(middleLoop)
            
            InnerLoop = InnerLoop + 1
        middleLoop = middleLoop + 1
    firstLoop = firstLoop + 1

print(linearEquations)