# solution of the problem from leetcode the sum of perfect squares
from math import sqrt
def count_number(n):
    squares=[i*i for i in range(1,int(sqrt(n))+1)]
    dp=[float("inf") for _ in range(n+1)]
    dp[0]=0

    for i in range(1,n+1):
        for square in squares:
            if square>i:
                break
            dp[i]=min(dp[i],dp[i-square])
    return dp[n]
# test code for working on the problem 
n=int(input("Enter integer: "))
ans=count_number(n)
print("ans:",ans)
