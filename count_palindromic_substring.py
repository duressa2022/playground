# code for counting palindromic substring
def expansion(left,right,s):
    counter=0
    while left>=0 and right<len(s) and s[left]==s[right]:
        counter+=1
        left-=1
        right+=1
    return counter

def count_subString(s):
    length=len(s)
    counter=0
    for index in range(length):
        odd=expansion(index,index)
        even=expansion[index,index+1]
        counter+=odd+even
    return counter
# testing the working of the the methods
s=input("Enter your string here: ")
ans=count_subString(s)
print("your answer is: ",ans)
    