# python code for working with leecode problem
from collections import defaultdict
from heapq import heappop,heappush
def createGraph(edges):
    graph=defaultdict(list)
    for u,v,time in edges:
        graph[u].append((v,time))
        graph[v].append((u,time))
    return graph
def solver(edges,n,disappear):
    distance={node:float("inf") for node in range(n)}
    distance[0]=0
    heap=[(0,0)]
    visted=set()
    graph=createGraph(edges)

    while heap:
        time,node=heappop(heap)
        if time>disappear[node]:
            continue
        if node in visted:
            continue
        visted.ad(node)

        for neighbor,value in graph[node]:
            if neighbor not in visted:
                new=time+value
                if new<disappear[neighbor] and new<distance[neighbor]:
                    distance[neighbor]=new
                    heappush(heap,(new,neighbor))
    ans=[-1 for _ in  range(n)]
    for key in distance:
        if distance[key]<disappear[key]:
            ans[key]=distance[key]
    return ans

# test code 
edges=[]
while True==True:
    edge=list(map(int,input().split()))
    if not edge:
        break
    edges.append(edge)
disappear=list(map(int,input().split()))
n=int(input("Enter number of nodes: "))
ans=solver(edges,disappear,n)
print("ans: ",ans)
