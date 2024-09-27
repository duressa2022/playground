import numpy as np
from time import sleep

def regression(X,Y,learning_rate,episodes,batch_size):
    X=np.array(X)
    Y=np.array(Y)

    features=len(X[0])
    weights=np.zeros(features)
    bias=0

    for episode in range(episodes):
        for index in range(0,len(Y),batch_size):
            x_batch=X[index:index+batch_size]
            y_batch=Y[index:index+batch_size]

            predicted=np.dot(x_batch,weights)+bias
            dw=1/(batch_size)*np.dot(x_batch.T,predicted-y_batch)
            db=1/(batch_size)*np.sum(predicted-y_batch)

            weights=weights-learning_rate*dw
            bias=bias-learning_rate*db

        if episode%100==0:
            print("current epsiode: {}".format(episode))
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
batch_size=2

weights,bias=regression(X,Y,learning_rate,episodes,batch_size)
print(weights,bias)