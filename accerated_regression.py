import numpy as np
from time import sleep

def regression(X,Y,learning_rate,beta,episodes):
    X=np.array(X)
    Y=np.array(Y)

    features=len(X[0])
    weights=np.zeros(features)
    bias=0
    velocity1=0
    velocity2=0

    for episode in range(episodes):
        predicted=np.dot(X,weights-beta*velocity1)+bias

        dw=(1/len(Y))*np.dot(X.T,predicted-Y)
        db=(1/len(Y))*np.sum(predicted-Y)

        velocity1=beta*velocity1+learning_rate*dw
        velocity2=beta*velocity2+learning_rate*db

        weights=weights-velocity1
        bias=bias-velocity2

        if episode%100==0:
            print("current episode: {}".format(episode))
            print("weights: ",weights)
            print("bias: ",bias)
            print("================================")
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

learning_rate=0.00001
episodes=1000
beta=0.9

weights,bias=regression(X,Y,learning_rate,beta,episodes)
print(weights,bias)