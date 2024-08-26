# This is program will compute the shortest path between two nodes
from heapq import heappop,heappush
def shortest_path(graph,start,end):
    current_path={node:node for node in graph}

    queue=[(start,0)]
    visted=set()

    while queue:
        cur,distance=heappop(queue)
        if cur==end:
            path=[]
            while cur!=current_path[cur]:
                path.append(cur)
                cur=current_path[cur]
            path.append(cur)
            return True,reversed(path)

        if cur in visted:
            continue
        visted.add(cur)

        for neighbor,weight in graph[cur]:
            if neighbor not in visted:
                path[neighbor]=cur
                heappush(queue,(distance+weight,neighbor))
    return False,[]
#test code for testing the working of the function
#temp graph that represent the link between the nodes

graph={
    "city":[("city",10)]
}
#get the start and end from the user

start=input("Enter the start of your journey: ")
end=input("Enter the end of your journey: ")

#based on the condition get the needed path from the
exist,paths=shortest_path(graph=graph,start=start,end=end)
if not exist:
    print("No path between {} and {}".format(start,end))
else:
    print("This is the sequenece of the path")
    for path in paths:
        print(path,end=="--->")

