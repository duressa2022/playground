from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIR=[(1,0),(-1,0),(0,1),(0,-1)]
        length_row=len(board)
        length_col=len(board[0])
        visted=set()
        def inbound(row,col):
            return 0<=row<length_row and 0<=col<length_col
        def solver(row,col):
            stack=[(row,col)]
            while stack:
                curx,cury=stack.pop()
                visted.add((curx,cury))
                for dx,dy in DIR:
                    x=curx+dx
                    y=cury+dy
                    if inbound(x,y) and (x,y) not in visted and board[x][y]=="O":
                        stack.append((x,y))
        for i in range(length_col):
            if board[0][i]=="O":
                solver(0,i)
            if board[length_row-1][i]=="O":
                solver(length_row-1,i)

        for i in range(length_row):
            if board[i][0]=="O":
                solver(i,0)
            if board[i][length_col-1]=="O":
                solver(i,length_col-1)
        for i in range(length_row):
            for j in range(length_col):
                if (i,j) not in visted:
                    board[i][j]="X"
