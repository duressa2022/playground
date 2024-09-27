import numpy as np
from time import sleep


def logistic(X,Y,learning_rate,episodes):

    def sigmod(X,weights,bias):
        return 1/(1+np.exp(np.dot(X,weights)+bias))
    
    X=np.array(X)
    Y=np.array(Y)

    features=len(X[0])
    weights=np.zeros(features)
    bias=0

    for episode in range(episodes):
        predicted=sigmod(X,weights,bias)

        dw=(-1/len(Y))*np.dot(X.T,predicted-Y)
        db=(-1/len(Y))*np.sum(predicted-Y)

        weights=weights-learning_rate*dw
        bias=bias-learning_rate*db

        if episode%100==0:
            print("current epsiode: {}".format(episode))
            print("weights: ",weights)
            print("bias: ",bias)
            print("=========================")
            sleep(0.5)
    return weights,bias

# test code 
X=[
    [2,4,8,10],
    [12,22,28,6],
    [15,17,77,25],
    [11,51,5,3]
]

Y=[ 
    1,
    1,
    0,
    0
]

learning_rate=0.01
episodes=1000

weights,bias=logistic(X,Y,learning_rate,episodes)
print(weights,bias)

