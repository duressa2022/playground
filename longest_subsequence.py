# code for solving longest inceasing subsequence

def main_method(nums):

    length=len(nums)
    memo={}

    def solver(index):
        if index in memo:
            return memo[index]
        ans=1
        for right in range(index+1,length):
            if nums[index]<nums[right]:
                ans=max(ans,1+solver(right))
        memo[index]=ans
        return ans
    ans=0
    for index in range(length):
        ans=max(ans,solver(index))
    return ans

# test the method
nums=list(map(int,input().split("Enter comma separated values: ")))
ans=main_method(nums=nums)
print("longest subsequence has: ",ans)
    

