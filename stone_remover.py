# program for working with max number of stones that is removed
class UnionFind:
    def __init__(self,points):
        self.parent={(x,y):(x,y) for x,y in points}
        self.rank={(x,y):0 for x,y in points}
    def find(self,val):
        while val!=self.parent[val]:
            self.parent[val]=self.parent[self.parent[val]]
            val=self.parent[val]
        return val
    def union(self,x,y):
        xroot=self.find(x)
        yroot=self.find(y)

        if xroot!=yroot:
            xrank=self.rank[xroot]
            yrank=self.rank[yroot]
            if xrank>yrank:
                self.parent[xroot]=yroot
            elif xrank<yrank:
                self.parent[yroot]=xroot
            else:
                self.parent[xroot]=yroot
                self.rank[yroot]+=1

# method for solving the problem 
def max_removed_stones(points):
    uf=UnionFind(points=points)
    length=len(points)

    for i in range(length):
        for j in range(i+1,length):
            if points[i][0]==points[j][0] or points[i][1]==points[j][1]:
                uf.union(points[i],points[j])

    counter=0
    for key in uf.parent:
        if uf.parent[key]!=key:
            counter+=1
    return counter
# test code for working with the solution
points=[]
while True==True:
    point=list(map(int,input("Enter x and y coordinates: ").split()))
    if not point:
        break
    points.append(point)
ans=max_removed_stones(points=points)
print("ans: ",ans)
