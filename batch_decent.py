import numpy as np
from time import sleep

def Regression_based_Batch(X,Y,learning_rate,episodes):
    X=np.array(X)
    Y=np.array(Y)

    number_features=len(X[0])
    weights=np.zeros(number_features)
    bias=0

    for episode in range(episodes):
        predicted=np.dot(X,weights)+bias

        dw=1/(len(Y))*np.dot(X.T,predicted-Y)
        db=1/(len(Y))*np.sum(predicted-Y)

        weights=weights-learning_rate*dw
        bias=bias-learning_rate*db

        if episode%100:
            print("=======================")
            print("current episode: {}".format(episode))
            print("weights: ",weights)
            print("bias: ",bias)
            print("========================")
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

learning_rate=0.0001
episodes=1000

weights,bias=Regression_based_Batch(X,Y,learning_rate,episodes)
print(weights,bias)




