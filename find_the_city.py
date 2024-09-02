# program to solve leetcode problem
from collections import defaultdict
from heapq import heappop,heappush
def createGraph(city):
    graph=defaultdict(list)
    for u,v,cost in city:
        graph[u].append((v,cost))
        graph[v].append((u,cost))
    return graph

def solver(graph,node,n,max_distance):
    distance={node:float("inf") for node in range(n)}
    distance[node]=0
    heap=[(0,node)]
    while heap:
        cost,cur_node=heappop(heap)
        if cost>distance[cur_node]:
            continue
        for neighbor,value in graph[node]:
            new=cost+value
            if distance[neighbor]>new:
                distance[neighbor]=new
    counter=0
    for key in distance:
        if distance[key]<=max_distance:
            counter+=1
    return counter
def mainSolver(edge,n,max_distance):
    graph=createGraph(edge)
    min_value=float("inf")
    city=-1
    for node in range(n):
        current=solver(graph,node,n,max_distance)
        if current<min_value or (current==min_value and node>city):
            city=node
            min_value=current
    return city

# test code 

edges=[]
while True==True:
    edge=list(map(int,input().split()))
    if not edge:
        break
    edges.append(edge)

n=int(input())
max_distance=int(input())
ans=mainSolver(edges,n,max_distance)
print("ans: ",ans)


