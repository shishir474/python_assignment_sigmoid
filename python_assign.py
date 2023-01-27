
# python assignment

class Solution:
    def dfs(self, board, i, j):
        n = len(board) # n rows
        m = len(board[0]) # m cols

        # created two lists, xdir and ydir to cover neighbours of the current cell
        xdir=[-1,0,1,0]
        ydir=[0,1,0,-1]

        # marking cell as '-1' indicating that this '0' will not be converted to 'X'
        board[i][j]='-1'

        #  check all the neighbours of current cell. Ensure that the neighbour cell is within the board and it has 'O' placed in it
        for k in range(4):
            newi = i+xdir[k]
            newj = j+ydir[k]
            #check if the neighbouring cell is safe to visit. 
            if(newi>=0 and newi<n and newj>=0 and newj<m and board[newi][newj]=='O'):
                self.dfs(board, newi, newj)

                

    def solve(self, board: list[list[str]]) -> None:
        n = len(board) # n rows
        m = len(board[0]) # m cols

        #APPROACH:
        # first cover all 0s at boundary. Call dfs from O encoutered at boundary and mark all the Os as -1
        # Now all the leftover 0s are of interest to us. Replace all these Os with X
        # now traverse the matrix again and check for -1. These are the 0s which aren't converted into X. Convert all -1s back to O 


        # 0th row
        for i in range (m):
            if board[0][i]=='O':
                self.dfs(board,0,i)
        # n-1th row
        for i in range (m):
            if board[n-1][i]=='O':
                self.dfs(board,n-1,i)
        # 0th col
        for i in range (n):
            if board[i][0]=='O':
                self.dfs(board,i,0)
        # m-1th col
        for i in range (n):
            if board[i][m-1]=='O':
                self.dfs(board,i,m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=='-1':
                    board[i][j]='O'




# enter num of rows and cols in board
n = int(input('enter number of rows: '))
m = int(input('Enter number of columns: '))

#creating board
board = []
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(input())
    board.append(temp)

obj = Solution()

obj.solve(board)

print(board)