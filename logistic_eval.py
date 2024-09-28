import numpy as np

def accuracy(actual,predicted):
    number=0
    for val1,val2 in zip(actual,predicted):
        if val1==val2:
            number+=1
    return number/len(actual)

def precision(actual,predicted):
    counter_true=0
    counter_false=0
    for val1,val2 in zip(actual,predicted):
        if val1==1 and val2==1:
            counter_true+=1
        elif val1==0 and val2==1:
            counter_false+=1        
    return counter_true/(counter_true+counter_false) if counter_true+counter_false!=0 else 0
def recall(actual,predicted):
    counter_true=0
    counter_false=0
    for val1,val2 in zip(actual,predicted):
        if val1==1 and val2==1:
            counter_true+=1
        if val1==1 and val2==0:
            counter_false+=1
    return counter_true/(counter_true+counter_false) if counter_true+counter_false!=0 else 0
def F1(actual,predicted):
    pre=precision(actual,predicted)
    rec=recall(actual,predicted)
    return (2*pre*rec)/(pre+rec) if pre+rec!=0 else 0



