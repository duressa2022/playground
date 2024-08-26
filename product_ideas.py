# code for max product cons from the set or list values or intensity

# define method for working on the idea

def max_product(nums):

    min_product=nums[0]
    max_product=nums[0]
    result=nums[0]

    for num in nums[1:]:

        if num<0:

            min_product,max_product=max_product,min_product

        max_product=max(num,max_product*num)
        min_product=max(num,max_product*num)

        result=max(result,max_product)

    return result

# test code

nums=list(map(int,input("Enter comma separated values: ")))

ans=max_product(nums=nums)

print("result for problem: ",ans)

