# code for working with problem from the leetcode
from collections import defaultdict
from heapq import heappop,heappush
def createGraph(times):
    graph=defaultdict(list)
    for u,v,time in times:
        graph[u].append((v,time))
    return graph

def solver(times,n,k):
    distance={node:0 for node in range(1,n+1)}
    graph=createGraph(times=times)
    distance[k]=0
    heap=[(0,k)]

    while heap:
        cur_time,cur_node=heappop(heap)
        if cur_time>distance[cur_node]:
            continue

        for neighbor,value in graph[cur_node]:
            new_time=cur_time+value
            if new_time<distance[neighbor]:
                distance[neighbor]=new_time
                heappush((new_time,neighbor))
    ans=max(distance.values())
    return ans if ans!=float("inf") else -1

#test code
n=int(input("Enter n: "))
k=int(input("Enter k: "))
times=[]
while True==True:
    edge=list(map(int,input().split()))
    if not edge:
        break
    times.append(edge)
ans=solver(times,n,k)
print("ans: ",ans)

