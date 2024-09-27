import numpy as np
from time import sleep

def regression(X,Y,learning_rate,beta,episodes):
    X=np.array(X)
    Y=np.array(Y)

    features=len(X[0])
    weights=np.zeros(features)
    bias=0
    velocity_for_weights=0
    velocity_for_bias=0

    for episode in range(episodes):
        predicted=np.dot(X,weights)+bias

        dw=(1/len(Y))*np.dot(X.T,predicted-Y)
        db=(1/len(Y))*np.sum(predicted-Y)

        velocity_for_weights=beta*velocity_for_weights+learning_rate*dw
        velocity_for_bias=beta*velocity_for_bias+learning_rate*db

        weights=weights-velocity_for_weights
        bias=bias-velocity_for_bias

        if episode%100==0:
            print("current episode: {}".format(episode))
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

learning_rate=0.00001
episodes=1000
beta=0.9

weights,bias=regression(X,Y,learning_rate,beta,episodes)
print(weights,bias)