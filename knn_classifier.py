from collections import Counter
import numpy as np

def knn_classifier(X,Y,k,xtest):
    X=np.array(X)
    Y=np.array(Y)

    predictions=[]
    for test in xtest:
        distance=np.array([np.sum((test-train)**2) for train in X])

        kth_nearest_index=np.argsort(distance)

        kth_nearest_value=np.array([Y[index] for index in kth_nearest_index])

        counter=Counter(kth_nearest_value)

        predictions.append(counter.most_common(1)[0][0])
    return predictions