# test code for tabulation method for working on the problem 

def solver(n):
    dp=[0 for _ in range(n+1)]
    dp[1]=1

    for index in range(2,n+1):
        dp[index]=dp[index-1]+dp[index-2]
    
    return dp[n]

# test the method
n=int(input())
print("answer: ",solver(n=n))
