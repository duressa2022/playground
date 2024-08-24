# This code simulate how edit distance algorthem is used for measuring the similarity of words

from heapq import heappop,heappush
# define method for working on the similarity of words

def EditDistance(word1,word2):
    n,m=len(word1),len(word2)
    memo={}

    def solver(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        
        if i==n:
            return m-j
        if j==m:
            return n-i
        
        if word1[i]==word2[j]:
            memo[(i,j)]=solver(i+1,j+1)
        else:
            update=1+solver(i+1,j+1)
            delete=1+solver(i+1,j)
            insert=1+solver(i,j+1)

            memo[(i,j)]=min(update,delete,insert)
        return memo[(i,j)]
    return solver(0,0)

# method for getting most k similar words

def GetSimilarWords(database,term,k):
    possibleWords=[]

    for word in database:
        measure=EditDistance(word1=word,word2=term)
        heappush(possibleWords,(measure,word))
    
    resultWords=[]

    for _ in range(k):
        word=heappop(possibleWords)
        resultWords.append(word)
    
    return resultWords

# testing code for providing simple database
database=["gen","generate","rand","random","message","messages"]

# simulate the search bar here by getting input from the user

search_term=input("Enter your ideas: ")

possibleWords=GetSimilarWords(database=database,term=search_term,k=1)
for word in possibleWords:
    print(word)



    

    


