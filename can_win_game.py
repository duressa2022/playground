# code for working with can game

def can_win(maxNumber,target):
    memo={}
    def solver(cur,used):
        if used in memo:
            return memo[used]
        for move in range(1,maxNumber+1):
            if used&(1<<move)==0:
                new=used|(1<<move)
                if cur-move<=0 or not solver(cur=cur-move,used=new):
                    memo[used]=True
                    return True
        memo[used]=False
        return False
    ans=solver(target,0)
    return ans
# test code for working with the product
maxNumber=int(input("Enter your max range: "))
target=int(input("Enter your target: "))
ans=can_win(maxNumber=maxNumber,target=target)
print("ans: ",ans)


