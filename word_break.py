# solution for word break 1 problem from the leetcode

def word_break(s,wordDict):
    words=set(wordDict)
    length=len(s)
    dp=[False for _ in range(length+1)]
    dp[0]=True

    for i in range(1,length+1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i]=True
                break
    return dp[length]
# test code
s=input("Enter your word: ")
words=[]
while True==True:
    data=input("Enter word: ")
    if not data:
        break
    words.append(data)

ans=word_break(s,wordDict=words)
print("Your result is: ",ans)
