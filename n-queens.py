def isSafe(board,curr_row,curr_col,size):


    for row in range(curr_row):
        if board[row][curr_col]==1:
            return False
        
    
    row,col=curr_row,curr_col
    while row >=0 and col >=0:
        if board[row][col]==1:
            return False
        
        row -=1
        col -=1

    row,col=curr_row,curr_col
    while row >=0 and col < size:
        if board[row][col]==1:
            return False
        
        row -=1
        col +=1


    return True

def solve_n_queens(board,row,size):

    if row >= size:
        return True
    

    for col in range(size):
        if isSafe(board,row,col,size):
            board[row][col]=1
            if solve_n_queens(board,row+1,size):
                return True
            
            board[row][col]=0

    return False

def display_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))


def main():

    size = int(input("Enter the No of Queens = "))
    board = [[0 for _ in range(size)]for _ in range (size)]


    if solve_n_queens(board,0,size):
        print("\n The Solution is :- ")
        display_board(board)
    else:
        print("No Solution Exists")


if __name__== "__main__":
    main()
