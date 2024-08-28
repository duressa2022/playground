# code for working with the longest chain

def main_method(pairs):
    pairs.sort(key=lambda x:x[1])
    length=len(pairs)
    memo={}

    def solver(index):
        if index in memo:
            return memo[index]
        
        ans=1
        for right in range(index+1,length):
            if pairs[index][1]<pairs[right][0]:
                ans=max(ans,1+solver(right))
        memo[index]=ans
        return ans
    
    ans=0
    for index in range(length):
        ans=max(ans,solver(index))
    return ans

# test code 
pairs=[]
while True==True:
    chain=list(map(int,input("Enter pairs: ").split()))
    if not chain:
        break
    pairs.append(chain)
ans=main_method(pairs=pairs)
print("ans: ",ans)

