# program for solving leetcode problem 
from heapq import heappop,heappush
from collections import defaultdict
def dfs(graph,distance,node,end,memo):
    if node in memo:
        return memo[node]
    if node==end:
        return 1
    ans=0
    for neighbor,_ in graph[node]:
        if distance[node]>distance[neighbor]:
            ans+=dfs(graph,distance,neighbor,end,memo)
            ans=(ans)%(10**9+7)
    memo[node]=ans
    return memo[node]

def djikastra(graph,n):
    distance={node:float("inf") for node in range(1,n+1)}
    distance[n]=0
    heap=[(0,n)]
    while heap:
        weight,node=heappop(heap)
        if weight>distance[node]:
            continue
        for neighbor,value in graph[node]:
            new=weight+value
            if new>distance[neighbor]:
                distance[neighbor]=new
                heappush(neighbor,(new,neighbor))
    return distance
def createGraph(edges):
    graph=defaultdict(list)
    for u,v,weight in edges:
        graph[u].append((v,weight))
        graph[v].append((u,weight))
    return graph
def solver(edges,n):
    graph=createGraph(edges=edges)
    distance=djikastra(graph,n)
    ans=dfs(graph=graph,distance=distance,node=1,end=n,memo={})
    return ans
# test code
edges=[]
while True==True:
    edge=list(map(int,input().split()))
    if not edge:
        break
    edges.append(edge)
n=int(input("Enter number of node: "))
ans=solver(edges=edges,n=n)
print("ans: ",ans)

