import numpy as np

class SimpleNetwork:
    def __init__(self,input_size,hidden_size1,hidden_size2,hidden_size3,out_size,learning_rate):
        self.input_size=input_size
        self.hidden_size1=hidden_size1
        self.hidden_size2=hidden_size2
        self.hidden_size3=hidden_size3
        self.out_size=out_size
        self.learning_rate=learning_rate

        self.w1=np.random.randn(self.input_size,self.hidden_size1)
        self.b1=np.random.randn(1,self.hidden_size1)

        self.w2=np.random.rand(self.hidden_size1,self.hidden_size2)
        self.b2=np.random.randn(1,self.hidden_size2)

        self.w3=np.random.rand(self.hidden_size2,self.hidden_size3)
        self.b3=np.random.randn(1,self.hidden_size3)

        self.w4=np.random.randn(self.hidden_size3,self.out_size)
        self.b4=np.random.randn(1,self.out_size)

    def _relu(self,Z):
        return np.maximum(Z,0)
    
    def _derivative_relu(self,Z):
        return np.where(Z>0,1,0)
    
    def _sigmod(self,Z):
        return 1/(1+np.exp(-Z))
    
    def _derivative_sigmod(self,Z):
        return self._sigmod(Z)*(1-self._sigmod(Z))
    
    def _ms_error(self,y,y_pred):
        return np.mean((y-y_pred)**2)
    
    def _derivative_ms(self,y,y_pred):
        return np.mean((y_pred-y))

    def forward(self,X):
        self.z1=np.dot(X,self.w1)+self.b1
        self.a1=self._relu(self.z1)

        self.z2=np.dot(self.a1,self.w2)+self.b2
        self.a2=self._relu(self.z2)

        self.z3=np.dot(self.a2,self.w3)+self.b3
        self.a3=self._relu(self.z3)

        self.z4=np.dot(self.a3,self.w4)+self.b4
        self.a4=self._sigmod(self.z4)
        return self.a4

    def back_propagete(self,X,y):
        n=y.shape[0]

        da4=self._derivative_ms(y,self.a4)
        dz4=da4*self._derivative_sigmod(self.z4)
        dw4=np.dot(self.a3.T,dz4)/n
        db4=np.sum(dz4,axis=0,keepdims=True)

        da3=np.dot(da4,self.w4)
        dz3=da3*self._derivative_relu(self.z3)
        dw3=np.dot(self.a2.T,dz3)/n
        db3=np.sum(dz3,axis=True,keepdims=True)

        da2=np.dot(da3,self.w3)
        dz2=da2*self._derivative_relu(self.z2)
        dw2=np.dot(self.a1.T,dz2)/n
        db2=np.sum(dz2,axis=True,keepdims=True)

        da1=np.dot(da2,self.w2)
        dz1=da1*self._derivative_relu(self.z1)
        dw1=np.dot(X.T,dz3)/n
        db1=np.sum(dz1,axis=0,keepdims=True)

        self.w1=self.w1-self.learning_rate*dw1
        self.b1=self.b1-self.learning_rate*db1

        self.w2=self.w2-self.learning_rate*dw2
        self.b2=self.b2-self.learning_rate*db2

        self.w3=self.w3-self.learning_rate*dw3
        self.b3=self.b2-self.learning_rate*db3

        self.w4=self.w4-self.learning_rate*dw4
        self.b4=self.b4-self.learning_rate*db4
    
    def train(self,X,y,epoches=1000):

        for epoch in range(epoches):
            y_pred=self.forward(X)

            loss=self._ms_error(y,y_pred)

            self.back_propagete(X,y)

            if epoch%100==0:
                print("on current epoch loss is: {}".format(loss))


# test code
X=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
y=np.array([1,2,3])

model=SimpleNetwork(input_size=3,hidden_size1=3,hidden_size2=3,hidden_size3=3,out_size=1,learning_rate=0.01)
model.train(X=X,y=y,epoches=1000)


     
