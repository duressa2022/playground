# python code
from collections import defaultdict
from heapq import heappop,heappush
def createGraph(edges):
    graph=defaultdict(list)
    for u,v,time in edges:
        graph[u].append((v,time))
        graph[v].append((u,time))
    return graph
def djikastra(graph,n):
    distance={node:float("inf") for node in range(n)}
    distance[0]=0
    ways=[0 for node in range(n)]
    ways[0]=1
    heap=[(0,0)]
    mod=10**7+9
    while heap:
        time,node=heappop(heap)
        if time>distance[node]:
            continue
        for neighbor,value in graph[node]:
            new=time+value
            if new>distance[neighbor]:
                distance[neighbor]=new
                ways[neighbor]=ways[node]
            elif new==distance[neighbor]:
                ways[neighbor]=(ways[neighbor]+ways[node])%mod
    return ways[n-1]%mod
def solver(edges,n):
    graph=createGraph(edges)
    ans=djikastra(graph,n)
    return ans
edges=[]
while True==True:
    edge=list(map(int,input().split()))
    if not edge:
        break
    edges.append(edge)
n=int(input("Enter number of nodes: "))
ans=solver(edges=edges,n=n)
print("ans: ",ans)