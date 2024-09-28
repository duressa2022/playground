import numpy as np

def r_squared(actual,predicted):
    actual=np.array(actual)
    predicted=np.array(predicted)

    actual_mean=np.mean(actual)

    actual_variance=np.sum((actual-actual_mean)**2)
    regression_var=np.sum((predicted-actual_mean)**2)

    return regression_var/actual_variance

def msError(actual,predicted):
    actual=np.array(actual)
    predicted=np.array(predicted)

    return np.mean((predicted-actual)**2)

def rmsError(actual,predicted):
    actual=np.array(actual)
    predicted=np.array(predicted)

    return np.sqrt(np.mean((predicted-actual)**2))

def maError(actual,predicted):
    actual=np.array(actual)
    predicted=np.array(predicted)

    return np.mean(np.abs(predicted-actual))

def mpaError(actual,predicted):
    actual=np.array(actual)
    predicted=np.array(predicted)

    return 100*np.mean(np.abs(predicted/actual-1))

