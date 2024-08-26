# This python code will simulate the work of not selecting consecetive products or resources 
# In the way that optimize the product cases

# method for working on the problem 

def max_product(products):

    length=len(products)

    # define helper function for working on the problem

    def solver_method(index,end):

        if index in memo:

            return memo[index]

        if index>=end:

            return 0
        
        take=products[index]+solver_method(index=index+2,end=end)

        dont=solver_method(index=index+1,end=end)

        memo[index]=max(take,dont)

        return memo[index]

    memo={}  
    ans1=solver_method(0,length-1)

    memo={}

    ans2=solver_method(1,length)

    return max(ans1,ans2)

# test code 

products=list(map(int,input("Enter your products: ").split(",")))

ans=max_product(products=products)

print("max result of the product is: ",ans)