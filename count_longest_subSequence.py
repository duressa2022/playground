# code for working with the problem 

def main_method(nums):

    length=len(nums)
    memo={}
    def solver(index):
        if index in memo:
            return memo[index]
        
        max_length=1
        max_counter=1
        for right in range(index+1,length):
            if nums[index]<nums[right]:
                cur_length,cur_counter=solver(index)
                if cur_length+1>max_length:
                    max_length=cur_length+1
                    max_counter=cur_counter
                elif cur_length+1==max_length:
                    max_counter+=cur_counter
        memo[index]=(max_length,max_counter)
        return memo[index]
    max_length=0
    max_counter=0
    for index in range(length):
        cur_length,cur_counter=solver(index)
        if cur_length>max_length:
            max_length=cur_length
            max_counter=cur_counter
        elif cur_length==max_length:
            max_counter+=cur_counter
    return max_counter

# test code 
nums=list(map(int,input("Enter comma separated values: ")))
ans=main_method(nums)
print("ans: ",ans)

