# code for solving division problem from the leetcode

# method for working with the problem 
from collections import defaultdict
def createGraph(equations,values):
    graph=defaultdict(list)
    for index in range(len(values)):
        u,v=equations[index]
        graph[u].append((v,values[index]))
        graph[v].append((u,1/values[index]))
    return graph     

def mainProgram(equations,values,queries):
    graph=createGraph(equations=equations,values=values)
    def solver(start,end,visted=set()):
        if start not in graph or end not in graph:
            return -1
        if start==end:
            return 1
        visted.add(start)

        for neighbor,value in graph[start]:
            if neighbor not in visted:
                ans=solver(neighbor,end,visted)
                if ans!=-1:
                    return ans*value
        return -1
    
    ans=[]
    for u,v in queries:
        cur=solver(u,v)
        ans.append(cur)
    return ans

# test code
E=[]
while True==True:
    edge=list(map(str,input("Enter vars: ").split()))
    if not edge:
        break
    E.append(edge)
V=[]
while True==True:
    value=list(map(int,input().split()))
    if not value:
        break
    V.append(value)
Q=[]
while True==True:
    query=list(map(str,input().split()))
    if not query:
        break
    V.append(query)
ans=mainProgram(E,V,Q)
print("List of results: ",ans)


