import numpy as np
class FeedForword:
    def __init__(self,input_size,hidden_size1,hidden_size2,hidden_size3,output_size,learning_rate=0.01):
        self.input_size=input_size
        self.hidden_size1=hidden_size1
        self.hidden_size2=hidden_size2
        self.hidden_size3=hidden_size3
        self.output_size=output_size
        self.learning_rate=learning_rate

        self.w1=np.random.random((self.input_size,self.hidden_size1))
        self.b1=np.random.random((1,self.hidden_size1))
        self.w2=np.random.random((self.hidden_size1,self.hidden_size2))
        self.b2=np.random.random((1,self.hidden_size2))
        self.w3=np.random.random((self.hidden_size2,self.hidden_size3))
        self.b3=np.random.random((1,self.hidden_size3))
        self.w4=np.random.random((self.hidden_size3,self.output_size))
        self.b4=np.random.random((1,self.output_size))

    def _sigmod(self,z):
        return 1/(1+np.exp(-z))
    
    def _ms_error(self,y,ypred):
        return np.mean((y-ypred)**2)
    
    def _der_ms_error(self,y,ypred):
        return -np.mean(y-ypred)
    
    def _der_sigmod(self,z):
        return self._sigmod(z)*(1-self._sigmod(z))


    def _forward(self,X):
        self.z1=np.dot(X,self.w1)+self.b1
        self.a1=self._sigmod(self.z1)

        self.z2=np.dot(self.a1,self.w2)+self.b2
        self.a2=self._sigmod(self.z2)

        self.z3=np.dot(self.a2,self.w3)+self.b3
        self.a3=self._sigmod(self.z3)

        self.z4=np.dot(self.a3,self.w4)+self.b4
        self.a4=self.z4

        return self.a4
    def _backpropagate(self,X,y):
        self.da4=self._der_ms_error(y,self.a4)
        self.dz4=self.da4*self._der_sigmod(self.z4)
        self.dw4=np.dot(self.dz4,self.a3)
        self.db4=self.dz4

        self.da3=np.dot(self.dz4,self.w4)
        self.za3=self.da3*self._der_sigmod(self.z3)
        self.dw3=self.dz3*np.dot(self._sigmod(self.z3),self.a2)
        self.db3=np.dot(self.da3,self._der_sigmod(self.z3))

        self.da2=np.dot(self.dz3,self.w3)
        self.za2=self.da2*self._der_sigmod(self.z2)
        self.dw2=self.dz2*np.dot(self._sigmod(self.z2),self.a1)
        self.db2=np.dot(self.da2,self._der_sigmod(self.z2))

        self.da1=np.dot(self.dz2,self.w2)
        self.za1=self.da1*self._der_sigmod(self.z1)
        self.dw1=self.dz1*np.dot(self._sigmod(self.z1),X)
        self.db1=np.dot(self.da1,self._der_sigmod(self.z1))

        self.w1-=self.learning_rate*self.dw1
        self.w2-=self.learning_rate*self.dw2
        self.w3-=self.learning_rate*self.dw3
        self.w4-=self.learning_rate*self.dw4

        self.b1-=self.learning_rate*self.db1
        self.b2-=self.learning_rate*self.db2
        self.b3-=self.learning_rate*self.db3
        self.b4-=self.learning_rate*self.db4

    def train(self,X,y,episodes=1000):
        for episode in range(episodes):
            ypred=self._forward(X)

            self._backpropagate(X,y)

            ms_error=self._ms_error(y,ypred)

            if episode%100==0:
                print("at episode: {} loss: {}".format(episode,ms_error))

    def predict(self,X):
        return self._forward(X)
    

class FeedForword:
    def __init__(self,input_size,hidden_size1,hidden_size2,hidden_size3,output_size,learning_rate=0.01):
        self.input_size=input_size
        self.hidden_size1=hidden_size1
        self.hidden_size2=hidden_size2
        self.hidden_size3=hidden_size3
        self.output_size=output_size
        self.learning_rate=learning_rate
        
        self.w1=np.random.random(self.input_size,self.hidden_size1)
        self.b1=np.random.random(1,self.hidden_size1)
        self.w2=np.random.random(self.hidden_size1,self.hidden_size2)
        self.b2=np.random.random(1,self.hidden_size2)
        self.w3=np.random.random(self.hidden_size2,self.hidden_size3)
        self.b3=np.random.random(1,self.hidden_size3)
        self.w4=np.random.random(self.hidden_size3,self.output_size)
        self.b4=np.random.random(1,self.output_size)
    def _sigmod(self,z):
        return 1/(1+np.exp(-z))
    def _ms_error(self,y,ypred):
        return np.mean((y-ypred)**2)
    def _der_ms_error(self,y,ypred):
        return -np.mean(y-ypred)
    def _der_sigmod(self,z):
        return self._sigmod(z)*(1-self._sigmod(z))
    def _forward(self,X):
        self.z1=np.dot(X,self.w1)+self.b1
        self.a1=self._sigmod(self.z1)
        
        self.z2=np.dot(self.a1,self.w2)+self.b2
        self.a2=self._sigmod(self.z2)
        
        self.z3=np.dot(self.a2,self.w3)+self.b3
        self.a3=self._sigmod(self.z3)
        
        self.z4=np.dot(self.a4,self.w4)+self.b4
        self.a4=self.z4
        return self.a4
    
    def _backpropagate(self,X,y):
        self.da4=self._der_ms_error(y,self.a4)
        self.dz4=self.da4*self._der_sigmod(self.z4)
        self.dw4=np.dot(self.dz4,self.a3)
        self.db4=self.dz4
        
        self.da3=np.dot(self.dz4,self.w4)
        self.za3=self.da3*self._der_sigmod(self.z3)
        self.dw3=self.dz3*np.dot(self._sigmod(self.z3),self.a2)
        self.db3=np.dot(self.da3,self._der_sigmod(self.z3))
        
        self.da2=np.dot(self.dz3,self.w3)
        self.za2=self.da2*self._der_sigmod(self.z2)
        self.dw2=self.dz2*np.dot(self._sigmod(self.z2),self.a1)
        self.db2=np.dot(self.da2,self._der_sigmod(self.z2))
        
        self.da1=np.dot(self.dz2,self.w2)
        self.za1=self.da1*self._der_sigmod(self.z1)
        self.dw1=self.dz1*np.dot(self._sigmod(self.z1),X)
        self.db1=np.dot(self.da1,self._der_sigmod(self.z1))
        
        self.w1-=self.learning_rate*self.dw1
        self.w2-=self.learning_rate*self.dw2
        self.w3-=self.learning_rate*self.dw3
        self.w4-=self.learning_rate*self.dw4
        
        self.b1-=self.learning_rate*self.b1
        self.b2-=self.learning_rate*self.b2
        self.b3-=self.learning_rate*self.b3
        self.b4-=self.learning_rate*self.b4
        
    def train(self,X,y,episodes=1000):
        for episode in range(episodes):
            ypred=self._forward(X)
            self._backpropagate(X,y)
            ms_error=self._ms_error(y,ypred)
            if episode%100==0:
                print("at episode: {} loss: {}".format(episode,ms_error))
    def predict(self,X):
        return self._forward(X)













