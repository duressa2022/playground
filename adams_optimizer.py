import numpy as np

class Adams:
    def __init__(self,learning_rate,beta1=0.9,beta2=0.99,epsilon=1e-8):
        self.learning_rate=learning_rate
        self.epsilon=epsilon
        self.beta1=beta1
        self.beta2=beta2
        self.v=None
        self.m=None
        self.time=0


    def update(self,parms,grads):
        if self.v==None:
            self.v=np.zeros(len(grads))
        if self.m==None:
            self.m=np.zeros(len(grads))

        self.time+=1

        self.v=self.beta1*self.v + (1-self.beta1)*grads**2
        self.m=self.beta2*self.m + (1-self.beta2)*grads

        self.v=self.v/(1-self.beta1*self.time)
        self.m=self.m/(1-self.beta2*self.time)

        parms=parms-self.learning_rate/(np.sqrt(self.v)+self.epsilon)
        return parms