import numpy as np
from time import sleep

def Regression_based_Batch(X,Y,learning_rate,episodes):
    X=np.array(X)
    Y=np.array(Y)

    number_feature=len(X[0])
    weights=np.zeros(number_feature)
    bias=0

    for episode in range(episodes):
        predicated=np.dot(X,weights)+bias

        dw=1/(len(Y))*np.dot(X.T,predicated-Y)
        db=1/(len(Y))*np.sum(predicated-Y)

        weights=weights-learning_rate*dw
        bias=bias-learning_rate*db

        if episode%100==0:
            print("weights: ",weights)
            print("bias:",bias)
            print("Episode for: ",episode)
            sleep(0.5)
    return weights,bias

# test code 
X=[
    [3,4,2,5],
    [150,200,120,250],
    [150,200,120,250],
    [10,5,20,3]
]

Y=[ 
    300000,
    450000,
    220000,
    550000
]

learning_rate=0.1
episodes=1000

weights,bias=Regression_based_Batch(X,Y,learning_rate,episodes)
print(weights,bias)



