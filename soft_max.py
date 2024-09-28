import numpy as np
from time import sleep

def soft_max_regression(X,Y,learning_rate,number_class,epsoides):

    def soft_max(X,W):
        z=np.dot(X,W)
        z-=np.max(z,axis=1,keepdims=True)
        exp=np.exp(z)
        return exp/np.sum(exp,axis=1,keepdims=True)
    
    number_features=len(X[0])
    weights=np.zeros((number_class,number_features))

    for episode in range(epsoides):
        predicted=soft_max(X,weights)

        dw=(1/len(Y))*np.dot(X,(predicted-Y).T)

        weights=weights-learning_rate*dw

        if episode%100==0:
            print("current episode: {}".format(episode))
            print("weights: ",weights)
            sleep(0.5)
    return weights
