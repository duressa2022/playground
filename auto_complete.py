#python code for impelementing auto complete featurees by using trie 

#create a node to represent the node for the trie
class TrieNode:
    def __init__(self) -> None:
        self.children=[None for _ in range(26)]
        self.isEnd=False

#create a class to work on with the autcomplete feature

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
    
    # method for putting the word in the trie
    def insert(self,word):
        cur=self.root
        for char in word:
            loc=ord(char)-ord("a")
            if not cur.children[loc]:
                cur.children[loc]=TrieNode()
            cur=cur.children[loc]
        cur.isEnd=True

    # method for searching the word in the trie
    def SearchWord(self,word):
        cur=self.root
        for char in word:
            loc=ord(char)-ord("a")
            if not cur.children[loc]:
                return False
            cur=cur.children[loc]
        return cur.isEnd
    
    #method for searching the prefix in the trie

    def SearchPrefix(self,prefix):
        cur=self.root
        for char in prefix:
            loc=ord(char)-ord("a")
            if not cur.children[loc]:
                return False
            loc=cur.children[loc]
        return True
    
    #method for generating all words for given prefix

    def GenerateWith(self,prefix):
        wordsWithGivenPrefix=[]
        cur=self.root
        for char in prefix:
            loc=ord(char)-ord("a")
            if not cur.children[loc]:
                return wordsWithGivenPrefix
            cur=cur.children[loc]
        stack=[(cur,list(prefix))]
        while stack:
            node,word=stack.pop()
            if node.isEnd:
                wordsWithGivenPrefix.append(word)
            for index,neighbor in enumerate(cur.children):
                if neighbor:
                    stack.append((neighbor,word.append(char(ord("a")+index))))
        return wordsWithGivenPrefix
    
# code for testing the code that is given above

# generate random list of words for storing in .
words=["gen","generate","rand","random","message","messages"]


# create a instance of the trie for working and populate the trie
trie=Trie()

for word in words:
    trie.insert(word=word)

# create an input to simulate the search bar for searching the data
search_term=input("Enter your ideas: ")

possibleWords=trie.GenerateWith(search_term)

#list out possible words based on the given information 
for possible in possibleWords:
    print(possible)





