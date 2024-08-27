# This is python code that implements diskastras algorithems for working

from collections import defaultdict
from heapq import heappop,heappush

# method for working with the problem
def max_probablity_path(edgelist,n,prob_list,start,end):
    graph=defaultdict(list)

    for index in range(len(edgelist)):
        u,v,weight=edgelist[index][0],edgelist[index][1],prob_list[index]
        graph[u].append((v,weight))
        graph[v].append((u,weight))

    queue=[(-1,start)]
    probs={node:0 for node in range(n)}
    probs[start]=1

    while queue:
        cur,node=heappop(queue)
        cur=-cur

        if cur==end:
            return cur
        
        for neighbor,other in graph[node]:
            current=cur*other
            if current>probs[neighbor]:
                probs[neighbor]=current
                heappush(queue,(-current,neighbor))

    return 0

# test code for working with the problem
n=int(input("Enter number of nodes: "))
edgelist=[]
probs=[]
while True:
    edge=list(map(int,input("Enter edges,weights: ")))

    if len(edge)!=3:
        break
    edgelist.append([edge[0],edge[1]])
    probs.append(edge[2])
start,end=list(map(int,input().split("Enter start and end node: ")))

ans=max_probablity_path(edgelist=edgelist,n=n,prob_list=probs,start=start,end=end)

print("probs for the path is: ",ans)




