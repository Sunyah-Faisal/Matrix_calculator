                                       #addition and subtraction function
def addNsub(a,b,operator):
    '''Arguments: name of both matrices separated by commas, operator '+' or '-' \nPerforms addition and subtraction on matrices'''
    for i in range(len(a)):
        for j in range(len(a[0])):
            if operator=='+':
                ans[i][j]=a[i][j]+b[i][j]
            if operator=='-':
                ans[i][j]=a[i][j]-b[i][j]
    for k in ans:
        print(k)

                                                    #multiplication function
def mult(a,b):
    '''Arguments: name of both matrices separated by commas \nPerforms multiplication of matrices'''
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ans[i][j]+=a[i][k]*b[k][j]
    for l in ans:
        print(l)

                                                    #adjoint and determinant function
def adjNdet(a,func):
    '''Arguments: name of matrix, function name 'adj' or 'det' \nFinds adjoint and determinant of 2 by 2 matrices'''
    if func=='adj':
        mat=[[0,0],[0,0]]
        mat[0][0]=a[1][1]
        mat[0][1]=-a[0][1]
        mat[1][0]=-a[1][0]
        mat[1][1]=a[0][0]
        print('\nAdjoint matrix =')    
        for i in range(2):
            for j in range(2):
                print(mat[i][j],end=' ')
            print()
    if func=='det':
        b=a[0][0]*a[1][1]-a[1][0]*a[0][1]
        print('\nDeterminant =',b)


print('\t\tMATRIX CALCULATOR')

while True:
    print('\nOPERATIONS MENU\n')
    print('1: Addition''\n''2: Subtrction''\n''3: Multiplication''\n''4: Adjoint of 2 by 2 matrix''\n''5: Determinant of 2 by 2 matrix''\n''6: Exit''\n')
    opr=int(input('Enter option no.: '))
    
    if opr==6:
        print('Exiting the program....')
        break
    elif 1<=opr<=5:
                                                        #creating first matrix
        row1=int(input('\nEnter no. of rows for matrix 1: '))
        col_1=int(input('Enter no. of columns for matrix 1: '))
        print()
        Mat1=[]
        for i in range(1,row1+1):
            m1=[]
            for j in range(1,col_1+1):
                print('Enter value for row',i,'column',j,'of matrix 1: ',end='')
                m1.append(int(input()))
            Mat1.append(m1)
                                                        #adjoint
        if opr==4:
            if row1==col_1==2:
                adjNdet(Mat1,'adj')
            else:            
                print('\nCalculator can find adjoint of 2 by 2 matrix only')
            continue
                                                        #determinant
        if opr==5:
            if row1==col_1==2:
                adjNdet(Mat1,'det')                
            else:      
                print('\nCalculator can find determinant of 2 by 2 matrix only')
       
            continue

                                                        #creating second matrix
        row2=int(input('\nEnter no. of rows for matrix 2: '))
        col_2=int(input('Enter no. of columns for matrix 2: '))
        print()
        Mat2=[]
        for k in range(1,row2+1):
            m2=[]
            for l in range(1,col_2+1):
                print('Enter value for row',k,'column',l,'of matrix 2: ',end='')
                m2.append(int(input()))
            Mat2.append(m2)
            
                                                        #printing first matrix
        print('Matrix 1 =')
        for i in range(row1):
            for j in range(col_1):
                print(Mat1[i][j],end=' ')
            print()
            
                                                        #printing second matrix
        print('Matrix 2 =')
        for k in range(row2):
            for l in range(col_2):
                print(Mat2[k][l],end=' ')
            print()
            
                                                        #addition and subtraction
        if opr==1 or opr==2:
            ans=[]
            for x in range(row1):
                ans.append([])
            for y in range(row1):
                for z in range(col_1):                    
                    ans[y].append(z)

            if row1==row2 and col_1==col_2:
                print('Answer = ')
                if opr==1:
                    addNsub(Mat1,Mat2,'+')
                if opr==2:
                    addNsub(Mat1,Mat2,'-')
            else:
                if opr==1:
                    print('Addition cannot be performed on these matrices')
                if opr==2:
                    print('Subtraction cannot be performed on these matrices')
        
                                                        #multiplication
        if opr==3:
            ans=[]
            for r in range(row1):
                ans.append([])
            for s in range(row1):
                for t in range(col_2):
                    ans[s].append(t)                    
                    ans[s][t]=0

            if col_1==row2:
                print('Answer = ')
                mult(Mat1,Mat2)
            else:
                print('Multiplication cannot be performed on these matrices')    
    else:
        print('Enter valid option number')    
