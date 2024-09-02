# problem from the leetcode
from collections import defaultdict
from heapq import heappop,heappush
def createGraph(flights):
    graph=defaultdict(list)
    for start,dst,price in flights:
        graph[start].append((dst,price))
    return graph

def solver(flights,src,dst,k):
    graph=createGraph(flights=flights)
    distance={(src,0):0}
    heap=[(0,src,k)]

    while heap:
        cost,node,steps=heappop(heap)
        if steps>k:
            continue
        for neighbor,value in graph[node]:
            new=cost+value
            if (neighbor,steps+1) not in distance or distance[(neighbor,steps+1)]>new:
                distance[(neighbor,steps+1)]=new
                heappush(heap,(new,neighbor,steps+1))
    ans=[]
    for d,kvalue in distance:
        if d==dst and kvalue<=k:
            ans.append((distance[(d,kvalue)]))
    return -1 if len(ans)==0 else min(ans)
# test code 

flights=[]
while True==True:
    edge=list(map(int,input().split()))
    if not edge:
        break
    flights.append(edge)
src=int(input("Enter src: "))
dst=int(input("Enter dst: "))
k=int(input("Enter k: "))
ans=solver(flights,src,dst,k)
print("Ans: ",ans)
            



