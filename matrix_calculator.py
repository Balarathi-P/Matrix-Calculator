import pickle

def formatted_printing(op,result,L1,L2=[]):
    if L2 ==[]:
        if op != 5:
            operator = identify_operator(op)
            print("The resultant matrix obtained upon taking the",operator,"of the matrix")
            print_mat(L1)
            print("is")
            print_mat(result)

        else:
            print("The determinant of the matrix")
            print_mat(L1)
            print("is",result)
    else:
        operator = identify_operator(op)
        print("The resultant matix obtained upon the",operator,"of")
        print_mat(L1)
        print("and")
        print_mat(L2)
        print("is")
        print_mat(result)

def adjoint(L):
    matrix = []
    if len(L) == 2:
        ret_matrix = [[L[1][1], (-1)*L[0][1] ],[(-1)*L[1][0] , L[0][0]]]
    
    else:
        for i in range(len(L)):#row
            sub_mat =[]
            copy1 = L[0:i] + L[i+1:]
            for j in range(len(L)):#column
                copy2 =list(range(len(copy1)))            
                for k in range(len(copy1)):
                    copy2[k]=  copy1[k][0:j]+copy1[k][j+1:]
                cofac = ((-1)**(i+j))*determinant(copy2)
                sub_mat.append(cofac)
                
            matrix.append(sub_mat)
    
        ret_matrix = transpose(matrix)

    return ret_matrix

            
def determinant(L):
    total =0
    if len(L) == 2:
        sum = L[0][0] * L[1][1] - L[0][1]*L[1][0]
        return sum
    for i in range(len(L)):
        copy = L[1:]
        length = len(copy)
        for j in range(length):
            copy[j]=copy[j][:i]+copy[j][i+1:]
        
        sign = (-1) ** (i%2)
        sub_det = determinant(copy)

        total+= (sign) * L[0][i]*sub_det

    

    return total                                                  
    
def transpose(L):
    matrix=[]
    for i in range(len(L[0])):
        sub_mat = []
        for j in range(len(L)):
            element = L[j][i]
            sub_mat.append(element)

        matrix.append(sub_mat)

    return matrix


def inverse(L):
    adjoint_var = adjoint(L)
    determinant_var = determinant(L)
    inverse_mat =[]
    for i in range(len(adjoint_var)):#row
        sub_mat =[]
        for j in range(len(adjoint_var)): #column
            element = round(adjoint_var[i][j] / determinant_var,2)
            sub_mat.append(element)
        inverse_mat.append(sub_mat)
    
    return inverse_mat

def multiplication(L1,L2):
    num = 0
    matrix =[]
    for a in range(len(L1)):
        sub_mat = []
        for b in range(len(L2[0])):
            for c in range(len(L2)):
                n = L1[a][c] * L2[c][b]
                num+=n
            sub_mat.append(num)
            num =0
        
        matrix.append(sub_mat)

    return matrix
     
            
def subtraction(L1,L2):
    diff = 0
    matrix =[]
    for i in range(len(L1)):
        sub_mat = []
        for j in range(len(L1[0])):
            diff = L1[i][j] - L2[i][j]
            sub_mat.append(diff)
        matrix.append(sub_mat)
    
    return matrix

def addition(L1,L2):
    sum = 0
    matrix =[]
    for i in range(len(L1)):
        sub_mat = []
        for j in range(len(L1[0])):
            sum = L1[i][j] + L2[i][j]
            sub_mat.append(sum)

        matrix.append(sub_mat)   

    return matrix   

def inverse_check(L=[]):
    if L == []:
        while True:
            print("Enter the Matrix")
            print()
            matrix1 = matrix_input()
            det = determinant(matrix1)
            if det == 0:
                print('The determinant of the matrix is zero. Inverse cannot be calculated. Please enter a different matrix')
                print()
            else:
                return ["y",matrix1]
                
    else:
        det = determinant(L)
        if det == 0:
            return "n"
        else:
            return "y"
            

def square_check(L=[]):
    if L==[]:
        while True:
            print("Enter the matrix")
            matrix1 = matrix_input()
            print()
            if len(matrix1)==len(matrix1[0]):
                break
            else:
                print("Invalid Input. Try Again")
                print()
        
        return matrix1
    
    else:
        if len(L)==len(L[0]):
            return "y"
        else:
            return "n"
        

def multiplication_check(L=[]):
    if L ==[]:
        while True:
            print("Enter the First Matrix")
            matrix1 = matrix_input()
            print()
            print("Enter the Second Matrix")
            print()
            matrix2 = matrix_input()
            if len(matrix1[0]) == len(matrix2):
                break
            else:
                print("Invalid Input. Try Again")
                print()
        
        return [matrix1,matrix2]

    else:
        while True:
            print("Enter the matrix")
            matrix1 = matrix_input()
            print()

            if len(L[0])==len(matrix1):
                break
            else:
                print("Invalid Input. Try again")
                print()
            
        return matrix1
       
    
def addition_check(L=[]):
    if L==[]:
        while True:
            print("Enter the first matrix")
            matrix1 = matrix_input()
            print()
            print("Enter the second matrix")
            matrix2 = matrix_input()
            print()

            if len(matrix1)==len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
                break
            else:
                print("Invalid Input.Try Again")
                print()
        return [matrix1,matrix2]
    else:
        while True:
            print("Enter the matrix")
            matrix1 = matrix_input()
            print()
            if len(matrix1)==len(L) and len(matrix1[0]) == len(L[0]):
                break
            else:
                print("Invalid Input.Try Again")
                print()
        return matrix1

def identify_operator(n):
    if n == 1:
        op = "Addition"
        return op
    elif n==2:
        op = "Subtraction"
        return op

    elif n==3:
        op = "Multiplication"
        return op
    
    elif n == 4:
        op = "Transpose"
        return op
    
    elif n==5:
        op = "Determinant"
        return op
    
    elif n == 6:
        op = "Adjoint"
        return op
    
    elif n== 7:
        op = "Inverse"
        return op
    

def delete(username,password,operator,L1,L2,res):
    global file 
    reclist = []
    file.seek(0,0)
    while True:
        try:
            rec = pickle.load(file)
            reclist.append(rec)
        except EOFError:
            break
    file.truncate(0)

    for i in range(len(reclist)):
        if reclist[i][0] == username:
            reclist[i][1] = password
            reclist[i][2] = operator
            reclist[i][3] = L1
            reclist[i][4] = L2
            reclist[i][5] = res
    for i in reclist:
        pickle.dump(i,file)    
    
def matrix_input():
    while True:
        try:
            row = int(input("Enter the number of rows in the matrix : "))
            if row == 0:
                print("Invalid Input. Try again")
                continue
            column = int(input("Enter the number of columns in the matrix : "))
            if column == 0:
                print("Invalid Input.Try Again")
                continue

            break
        except ValueError:
            print("Invalid input. Try again")
        
    Matrix = []

    for i in range(row):
        column_list = []
        for j in range(column):
            while True:
                try:            
                    print("Enter an integer value for row",i+1,"column",j+1,": ",end = " ")
                    element = int(input())
                    column_list.append(element)
                    break
        
                except ValueError:
                    print("Invalid input. Try again")
            
        Matrix.append(column_list)

    return Matrix

def operator_input():
    print("The  matrix operations that can be performed are :")
    print('''1.Addition
2.Subtraction
3.Multiplication
4.Transpose
5.Determinant
6.Adjoint
7.Inverse ''')
    print()
    while True:
        op = int(input("Enter the operation you would like to perform(1/2/3/4/5/6/7) : "))
        print()
        if op in [1,2,3,4,5,6,7]:
            break
        else:
            print("Invalid operation. Enter again ")
            print()
    
    return op


def print_mat(L):
    for i in L:
        print(i)

file = open("LoginDetailstm.dat","a+b")
temp = open("temp.dat","a+b")
while True:
    print("******Welcome to matrix calculator******")
    print("\n")
    account_info = input("Do you have an existing account ?(Y/N) : ").lower()

    if account_info == "y":
        while account_info == "y":
            file.seek(0,0)
            username = input("Enter user name : ")
            print()
            password = input("Enter the password : ")
            print()
            while True:
                try:
                    location = file.tell()
                    L = pickle.load(file)
                    if L[0]==username and L[1]==password:
                        print("You have logged in successfully")
                        print()
                        proceed = "y"        
                        break
            
                except EOFError:
                    print("Invalid Username or Password")
                    print()
                    account_info= input("Would you like to try again(Y/N) : ").lower()
                    if account_info == "y":
                        proceed = "n" 
                        break                       
                    elif account_info == "n":
                        proceed = "n"
                        break
                    else:
                        print("Try again")
                        proceed = "n"

            break
            
                        

        while proceed == "y" :
            retrive = input("Would you like to retrive your previous calculation?(Y/N) : ").lower()
            print()
            if retrive in ["y","n"]:
                break
            else:
                print("Enter a valid input")
    
            

    
    elif account_info == "n":
        retrive = "n"
        enter2 = "y"
        check = "y"
        while enter2 == "y":
            file.seek(0,0)
            username = input("Enter your username : ")
            print()
            try:
                while True:
                    L = pickle.load(file)
                    if L[0] == username:
                        check = "n"
                        print("The username already exists. Please try again")
                        print()
                        break
            except EOFError:
                check = "y"
            
            if check == "n":
                continue

            password1 = input("Enter your password : ")
            password2 = input("Re-type your password : ")
            print()
            if password1 == password2:
                password  = password1
                location = file.tell()
                account = [username,password1,0,0,0,0]
                pickle.dump(account,file)
                enter2 = "n"
                print("Your account has been created")
                print()
                break
            else:
                print("There seems to be an error in your password. Please do type again")
                print()
        break

    else:
        print("Invalid option. Try again")
        print()
    
    break

#Retriving the previous matrix



while True:
    if retrive == "y":
        print("Retriving the previous calculations ....")
        input("Press enter to get your result")

        file.seek(0,0)
        try:
            while True:
                location = file.tell()
                row = pickle.load(file)
                if row[0] == username:
                    if row[3]!=0:
                        if row[2] in [1,2,3]:
                            op = identify_operator(row[2])
                            print("The operation performed was",op)                    
                            print("The first matrix is ")
                            print_mat(row[3])
                            print("The second matrix is ")
                            print_mat(row[4])
                            print("The resultant matrix is ")
                            print_mat(row[5])
                            result = row[5][::]
                            retrive_result = "y"

                            
                        elif row[2] in [4,6,7]:
                            op =identify_operator(row[2])
                            print("The operation performed was",op)                    
                            print("The input matrix is ")
                            print_mat(row[3])
                            print("The resultant matrix is ")
                            print_mat(row[5])
                            result = row[5][::]
                            retrive_result="y"

                        elif row[2]==5:
                            print("No resultant matrix as the operation performed was determinant")
                            print("The input matrix is ")
                            print_mat(row[3])
                            while True:
                                determinant_check = input("Would you prefer to retrive the matrix upon which the operation was performed ?(Y/N):").lower()
                                if determinant_check in ["y","n"]:
                                    if determinant_check == "y":
                                        result = row[3][::]
                                        print("The matrix is : ")
                                        print_mat(result)
                                        retrive_result = "y"
                                    else:
                                        retrive_result = "n"
                                    break
                                    
                                else:
                                    print("Invalid input. Please try again")

                        else:
                            print("No previous calculations were done")
                            retrive_result = "n"
                            break

        except EOFError:
            pass

    elif retrive == "n":
        retrive_result="n"

    cond = retrive_result == "y"
    if cond:
        matrix2 = result[::]
    operator = operator_input()

    if operator in [1,2]:
        if cond:
            matrix1 = addition_check(matrix2)
        else:
            matrix1,matrix2 = addition_check()
        matrix_conditions = [operator,matrix1,matrix2]
            
    elif operator == 3:
        if cond:
            matrix1 = multiplication_check(matrix2)
        else:
            matrix1,matrix2 = multiplication_check()
        matrix_conditions = [operator,matrix1,matrix2]

    elif operator == 4:
        if cond:
            pass

        else:
            matrix2 = matrix_input()
        matrix_conditions = [operator,matrix2]

    elif operator in[5,6]:
        if cond:
            determinant_check = square_check(matrix2)
            if determinant_check == "y":
                matrix_conditions = [operator,matrix2]

            else:
                print("Invalid matrix")
                print()
                while True:
                    print("Enter a new matrix")
                    print()
                    matrix2 = matrix_input()
                    check = square_check(matrix2)
                    if check == 'y':
                        break
                    else:
                        print("Invalid matrix. Please try Again")
                        print()
                matrix_conditions = [operator,matrix2]

        else:
            while True:
                matrix2 = matrix_input()
                determinant_check = square_check(matrix2)
                if determinant_check == "y":
                    matrix_conditions = [operator,matrix2]
                    break
                else:
                    print("Invalid Input. Please try Again")
                    print()
        
    elif operator == 7:
        if cond:
            inverse_check = inverse_check(matrix2)
            if inverse_check == "y":
                matrix_conditions = [operator,matrix2]
            
            else:
                print("Invalid matrix")
                print()
                while True:
                    print("Enter a new matrix")
                    matrix2 = matrix_input()
                    print()
                    check = inverse_check(matrix2)
                    if check == 'y':
                        break
                    else:
                        print("Invalid matrix. Please try Again")
                matrix_conditions = [operator,matrix2]

        else:
            while True:
                inverse_checker,matrix2 = inverse_check()
                if inverse_checker == "y":
                    matrix_conditions = [operator,matrix2]
                    break
                else:
                    print("Invalid Input. Please try Again")

    file.seek(location,0)
    if operator in [1,2,3]:
        mat_1,mat_2 = matrix_conditions[1:3]
        
        if operator == 1:
            
            res = addition (mat_1,mat_2)
            formatted_printing(operator,res,mat_1,mat_2)

        elif operator == 2:
        
            res = subtraction(mat_1,mat_2)
            formatted_printing(operator,res,mat_1,mat_2)
        elif operator == 3:
        
            res = multiplication(mat_1,mat_2)
            formatted_printing(operator,res,mat_1,mat_2)
        
        matrix_info = [username,password,operator,mat_1,mat_2,res]
        delete(username,password,operator,mat_1,mat_2,res)

    else:              

        if operator == 4:
            mat = matrix_conditions[1]
            res = transpose(mat)
            formatted_printing(operator,res,mat)
        elif operator == 5:
            mat = matrix_conditions[1]
            res = determinant(mat)
            formatted_printing(operator,res,mat)
        elif operator == 6:
            mat = matrix_conditions[1]
            res = adjoint(mat)
            formatted_printing(operator,res,mat)
        elif operator == 7:
            mat = matrix_conditions[1]
            res = inverse(mat)
            formatted_printing(operator,res,mat)

        matrix_info = [username,password,operator,mat,0,res]
        delete(username,password,operator,mat,0,res)

    ans = input("Do you wish to continue?(Y/N) : ").lower()
    print()
    

    if ans == "y":
        retrive = input("Do you wish to continue with your previous result? (Y/N) : ")
    else:
        print("Thank You for using Matrix Calculator")
        break
