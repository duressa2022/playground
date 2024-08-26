# code for working with parenthesis

def generate_possible(expression):

    def solver_method(exp):
        if exp.isdigit():
            return [int(exp)]
        
        ans=[]

        for index,char in enumerate(exp):

            if char=="+" or char=="-" or char=="*":

                left=solver_method(exp[:index])
                right=solver_method(exp[index+1:])

                for val in left:
                    for ual in right:
                        if char=="+":
                            ans.append(val+ual)
                        elif char=="-":
                            ans.append(val-ual)
                        else:
                            ans.append(val*ual)

        return ans
    ans=solver_method(exp=expression)
    return ans

# test your code here

exp=input("Enter algebric exp: ")

ans=generate_possible(expression=exp)

print("your result is: ",ans)

