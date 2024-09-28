import numpy as np

def knn_regressor(X,Y,k,xtest):
    X=np.array(X)
    Y=np.array(Y)
    xtest=np.array(xtest)
    ytest=np.array(ytest)

    predictions=[]

    for test in xtest:
        distance=np.array([np.sum((test-train)**2) for train in X])

        kth_nearest_index=np.argsort(distance)[:k]

        kth_nearest_value=np.array([Y[index] for index in kth_nearest_index])

        predictions.append(np.mean(kth_nearest_value))

  
    return predictions
        
