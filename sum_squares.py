#python code for working with the sum of perfect squares
from math import sqrt
def main_method(n):

    def is_perfect(num):
        return sqrt(num)-int(sqrt(num))==0
    memo={}
    def solver(num):
        if num in memo:
            return memo[num]
        if num<0:
            return float("inf")
        if num==0:
            return 0
        ans=float("inf")
        for neighbor in range(1,num+1):
            if is_perfect(neighbor):
                ans=min(ans,1+solver(num=num-neighbor))
        memo[num]=ans
        return ans
    return solver(n)
# test code 
n=int(input("Enter your number: "))
ans=main_method(n)
print("ans: ",ans)
