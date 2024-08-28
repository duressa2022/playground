# python code for working woth the problem

def main_method(s):

    length=len(s)
    memo={}
    def solver(left,right):
        if (left,right) in memo:
            return memo[(left,right)]
        if left>right:
            return 0
        if left==right:
            return 1
        
        if s[left]==s[right]:
            memo[(left,right)]=2+solver(left=left+1,right=right-1)
        else:
            memo[(left,right)]=max(solver(left=left+1,right=right),solver(left=left,right=right-1))

        return memo[(left,right)]
    ans=solver(0,length-1)
    return ans

# test code
s=input("Enter your string: ")
ans=main_method(s)
print("Your result is: ",ans)


        