import numpy as np
from time import sleep

def regression(X,Y,learning_rate,epsilon,episodes):
    X=np.array(X)
    Y=np.array(Y)

    features=len(X[0])
    weights=np.zeros(features)
    bias=0
    G1=0
    G2=0

    for epsiode in range(episodes):
        predicted=np.dot(X,weights)+bias

        dw=(1/len(Y))*np.dot(X.T,predicted-Y)
        db=(1/len(Y))*np.sum(predicted-Y)

        G1+=np.sum(dw**2)
        G2+=db**2

        weights=weights-(learning_rate/np.sqrt(G1+epsilon))
        bias=bias-(learning_rate/np.sqrt(G2+epsilon))

        if epsiode%100==0:
            print("current epsiode: {}".format(epsiode))
            print("weights: ",weights)
            print("bias: ",bias)
            sleep(0.5)
    return weights,bias


# test code 
X=[
    [3,4,2,5],
    [15,20,12,25],
    [15,20,12,25],
    [10,5,20,3]
]

Y=[ 
    30,
    45,
    22,
    55
]

learning_rate=0.001
episodes=1000
epsilon=0.00000000001

weights,bias=regression(X,Y,learning_rate,epsilon,episodes)
print(weights,bias)