import numpy as np
from time import sleep

def regression(X,Y,learning_rate,episodes):
    X=np.array(X)
    Y=np.array(Y)

    features=len(X[0])
    weights=np.zeros(features)
    bias=0

    for episode in range(episodes):
        for _ in range(len(X)):
            index=np.random.randint(0,len(X))
            x_index=X[index:index+1]
            y_index=Y[index:index+1]

            predicted=np.dot(x_index,weights)+bias
            dw=2*np.dot(x_index.T,predicted-y_index)
            db=np.sum(predicted-y_index)

            weights=weights-learning_rate*dw
            bias=bias-learning_rate*db
        if episode%100==0:
            print("==================")
            print("current epsoide: {}".format(episode))
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

weights,bias=regression(X,Y,learning_rate,episodes)
print(weights,bias)

