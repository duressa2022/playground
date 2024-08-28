# solves leetcodes sub island problem  by using dfs

# dfs method for working with the problem 
def main_method(grid1,grid2):
    row_length=len(grid2)
    col_length=len(grid2[0])

    def inbound(row,col):
        if row<0 or col<0 or row>=row_length or col>=col_length:
            return True
        return False
    
    Dirs=[(1,0),(-1,0),(0,1),(0,-1)]

    def solver(row,col):
        if inbound(row=row,col=col):
            return True
        if grid2[row][col]:
            return True
        grid2[row][col]=0

        island=True
        for dx,dy in Dirs:
            x=row+dx
            y=col+dy
            if not solver(x,y):
                island=False
        return island
    
    counter=0
    for row in range(row_length):
        for col in range(col_length):
            if grid2[row][col]==1 and solver(row=row,col=col):
                counter+=1

    return counter
#test code 
n=int(input("Enter number of rows: "))
grid1=[]
for _ in range(n):
    grid1.append(list(map(int,input("Enter comma separated values").split())))

grid2=[]
for _ in range(n):
    grid2.append(list(map(int,input("Enter comma separated values").split())))

ans=main_method(grid1=grid1,grid2=grid2)
print("number of sub island is: ",ans)
