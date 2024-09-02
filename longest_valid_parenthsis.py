# python code for working with longest valid parenthesis

def longest_valid(s):
    stack=[-1]
    max_length=0

    for index,char in enumerate(s):
        if char=="(":
            stack.append(index)
        else:
            stack.pop()
            if len(stack)==0:
                stack.append(index)
            else:
                max_length=max(max_length,index-stack[-1])
    

    return max_length

# test code for working with the user
s=input("Enter string to check: ")
ans=longest_valid(s)
print("The length of longest is: ",ans)