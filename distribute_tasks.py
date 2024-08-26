# This is python impelementatio of tasks disribution among k employee with optimal time

# method for checking wether can divide tasks into k subtasks where time is optimal

def can_divide(tasks,k,max_time):
    current_sum=0

    division=1

    for task in tasks:

        if current_sum+task>max_time:

            division+=1
            current_sum=task

        else:

            current_sum+=task

        if division>k:
            return False
        
    return True

# method for working with binary search 

def solver_method(tasks,k):

    left,right,best=max(tasks),sum(tasks),0

    while left<=right:

        mid=(left+right)//2

        if can_divide(tasks=tasks,k=k,max_time=mid):

            best=mid

            right=mid-1

        else:

            left=mid+1

    return best

#test code for working this method

# define tasks and employee
tasks=list(map(int,input("Enter comma separated values: ").split(",")))

employee=int(input("Enter number of employee do you have: "))

ans=solver_method(tasks=tasks,k=employee)

print("best way to divide is: ",ans)

