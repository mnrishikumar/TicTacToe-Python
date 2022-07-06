#main function 
import random

def main():
    print("hello world")
    matrix = initialize_matrix()
    symbol = choose_symbol()
    csymbol = allocate_symbol(symbol)
    
    if symbol == 'X':
        for i in range(9):
            print(i)
            if(i%2 == 0):
                print("The matrix is:")
                for i in range(3):
                    for j in range(3):
                        print(matrix[i][j],end=" ")
                    print()
                choose_value(matrix,symbol)
                print("The matrix is:")
                for i in range(3):
                    for j in range(3):
                        print(matrix[i][j],end=" ")
                    print()
                if check_row(matrix) or check_column(matrix) or check_diagonal(matrix):
                    print("You win!")
                    break

            else:
                choose_best_move(matrix,symbol,csymbol,i)
                print("Computer has played its move")                
                if check_row(matrix) or check_column(matrix) or check_diagonal(matrix):
                    print("The matrix is:")
                    for i in range(3):
                        for j in range(3):
                            print(matrix[i][j],end=" ")
                        print()
                    print("The computer wins!")
                    break
        if (check_row(matrix) or check_column(matrix) or check_diagonal(matrix)):
            y=1
        else:   
            print("The game is a draw");                 

    if symbol == 'O':
        for i in range(9):
            if(i%2 == 0):
                choose_best_move(matrix,symbol,csymbol,i)
                print("Computer has played its move")                
                if check_row(matrix) or check_column(matrix) or check_diagonal(matrix):
                    print("The matrix is:")
                    for i in range(3):
                        for j in range(3):
                            print(matrix[i][j],end=" ")
                        print()
                    print("The computer wins!")
                    break
                

            else:
                print("The matrix is:")
                for i in range(3):
                    for j in range(3):
                        print(matrix[i][j],end=" ")
                    print()
                choose_value(matrix,symbol)
                print("The matrix is:")
                for i in range(3):
                    for j in range(3):
                        print(matrix[i][j],end=" ")
                    print()
                if check_row(matrix) or check_column(matrix) or check_diagonal(matrix):
                    print("You win!")
                    break
                
        if (check_row(matrix) or check_column(matrix) or check_diagonal(matrix)):
            y=1
        else:   
            print("The game is a draw");        

#function that chooses the best move for the computer to play
def choose_best_move(matrix,symbol,csymbol,t):
    
    tsymbol = csymbol
    for (j) in range(2):
        for (i) in range(3):
            if matrix[i][0]==matrix[i][1] and matrix[i][0]==tsymbol and matrix[i][2]==i*3+3:
                matrix[i][2]=csymbol
                return    
            if matrix[i][0]==matrix[i][2] and matrix[i][0]==tsymbol and matrix[i][1]==i*3+2:
                matrix[i][1]=csymbol
                return
            if matrix[i][1]==matrix[i][2] and matrix[i][1]==tsymbol and matrix[i][0]==i*3+1:
                matrix[i][0]=csymbol
                return
        for (i) in range(3):
            if matrix[0][i]==matrix[1][i] and matrix[0][i]==tsymbol and matrix[2][i]==2*3+i+1:
                matrix[2][i]=csymbol
                return
            if matrix[0][i]==matrix[2][i] and matrix[0][i]==tsymbol and matrix[1][i]==1*3+i+1:
                matrix[1][i]=csymbol
                return
            if matrix[1][i]==matrix[2][i] and matrix[1][i]==tsymbol and matrix[0][i]==0*3+i+1:
                matrix[0][i]=csymbol
                return
            
        if matrix[0][0]==matrix[1][1] and matrix[0][0]==tsymbol and matrix[2][2]==9:
            matrix[2][2]=csymbol
            return
        
        elif matrix[0][0]==matrix[2][2] and matrix[0][0]==tsymbol and matrix[1][1]==5:
            matrix[1][1]=csymbol
            return

        elif matrix[1][1]==matrix[2][2] and matrix[1][1]==tsymbol and matrix[0][0]==1:
            matrix[0][0]=csymbol
            return
        
        elif matrix[0][2]==matrix[1][1] and matrix[0][2]==tsymbol and matrix[2][0]==7:
            matrix[2][0]=csymbol
            return

        elif matrix[0][2]==matrix[2][0] and matrix[0][2]==tsymbol and matrix[1][1]==5:
            matrix[1][1]=csymbol
            return

        elif matrix[1][1]==matrix[2][0] and matrix[1][1]==tsymbol and matrix[0][2]==3:
            matrix[0][2]=csymbol
            return
        
        tsymbol=symbol

    if t==1:
        if matrix[0][0]==symbol or matrix[2][0]==symbol or matrix[0][2]==symbol or matrix[2][2]==symbol:
            matrix[1][1]=csymbol
            return 
        elif matrix[1][1]==symbol:
            matrix[0][0]=csymbol
            return
        elif matrix[0][1]==symbol or matrix[2][1]==symbol or matrix[1][0]==symbol or matrix[1][2]==symbol:
            matrix[1][1]=csymbol
            return

    if t==3:
        if matrix[1][1]==csymbol:
            if matrix[0][0]==matrix[2][2] or matrix[0][2]==matrix[2][0]:
                matrix[0][1]=csymbol
                return 
            elif matrix[0][0]==matrix[1][2] or matrix[0][0]==matrix[2][1]:
                matrix[2][2]=csymbol
                return   
            elif matrix[0][2]==matrix[1][0] or matrix[0][2]==matrix[2][1]:
                matrix[2][0]=csymbol
                return
            elif matrix[2][2]==matrix[1][0] or matrix[2][2]==matrix[0][1]:
                matrix[0][0]=csymbol
                return 
            elif matrix[2][0]==matrix[1][2] or matrix[2][0]==matrix[0][1]:
                matrix[0][2]=csymbol
                return     
        if matrix[1][1]==matrix[2][2]:
            matrix[0][2]=csymbol
            return
        if matrix[1][0]==matrix[0][1] or matrix[1][0]==matrix[0][2] or matrix[1][0]==matrix[1][2]:
            matrix[0][0]=csymbol
            return
        if matrix[1][0]==matrix[2][1] or matrix[1][0]==matrix[2][2]:
            matrix[2][0]=csymbol
            return
        if matrix[0][1]==matrix[1][2] or matrix[0][1]==matrix[2][2] or  matrix[0][1]==matrix[2][1]:
            matrix[0][2]=csymbol
            return
        if matrix[0][1]==matrix[2][0] or matrix[0][1]==matrix[1][0]:
            matrix[0][0]=csymbol
            return
        if matrix[1][2]==matrix[0][1] or matrix[1][2]==matrix[0][0]:
            matrix[0][2]=csymbol
            return
        if matrix[1][2]==matrix[2][1] or matrix[1][2]==matrix[2][0]:
            matrix[2][2]=csymbol
            return
        if matrix[2][1]==matrix[0][0] or matrix[2][1]==matrix[1][0]:
            matrix[2][0]=csymbol
            return
        if matrix[2][1]==matrix[1][2] or matrix[2][1]==matrix[0][2]:
            matrix[2][2]=csymbol
            return     
    choose_random_value(matrix,csymbol)
  
                         


#function to initialize 3*3 matrix with values 1,2,3,4,5,6,7,8,9
def initialize_matrix():
    matrix = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = i*3+j+1
    return matrix

#function for the user to choose between 'X' and 'O'
def choose_symbol():
    symbol = input("Enter 'X' or 'O': ")
    while symbol not in ['X','O']:
        symbol = input("Enter 'X' or 'O': ")
    return symbol

#function to allocate the csymbol to 'X' if symbol is 'X' and 'O' if symbol is 'O'
def allocate_symbol(symbol):
    if symbol == 'X':
        return 'O'
    else:
        return 'X'

#function to let user choose a value from 1 to 9
def choose_value(matrix,symbol):
    b = 0
    while (b == 0) or value not in range(1,10):
        value = int(input("Enter a value from 1 to 9: "))
        for i in range(3):
             for j in range(3):
                if matrix[i][j] == value:
                    b = 1
                    matrix[i][j] = symbol
                
#function to choose a random value from 1 to 9 and check if it is available
def choose_random_value(matrix,csymbol):
    value = random.randint(1,9)
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == value:
                matrix[i][j] = csymbol
                return
    return choose_random_value(matrix,csymbol)

    
#function to check if the elements in the rows are same
def check_row(matrix):
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            return True
    return False


#function to check if the elements in the columns are same
def check_column(matrix):
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            return True
    return False

#function to check if the elements the diagonals are same
def check_diagonal(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return True
    return False



main()