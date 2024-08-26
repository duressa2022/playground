# This is python code for helping to pridict the max profit that the invester can get

def max_profit(prices):

    # helper method for working with the problem 

    length=len(prices)

    memo={}

    def solver_method(index,case):

        if (index,case) in memo:

            return memo[(index,case)]
        
        if index>=length:

            return 0
        
        if case:

            buy_here=-prices[index]+solver_method(index=index+1,case=False)

            not_here=solver_method(index=index+1,case=True)

            memo[(index,case)]=max(buy_here,not_here)

        else:

            sell_here=prices[index]+solver_method(index=index+1,case=True)

            not_here=solver_method(index=index+1,case=False)

            memo[(index,case)]=max(sell_here,not_here)

        return memo[(index,case)]
    
    ans=solver_method(index=0,case=True)

    return ans

#test code

stock_prices=list(map(int,input("Enter comma separated price: ").split(",")))

profit=max_profit(stock_prices)

print(profit)


