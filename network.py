import numpy as np
from time import sleep
class SimpleNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, hidden_size3, out_size, learning_rate):
        self.input_size = input_size
        self.hidden_size1 = hidden_size1
        self.hidden_size2 = hidden_size2
        self.hidden_size3 = hidden_size3
        self.out_size = out_size
        self.learning_rate = learning_rate

        self.w1 = np.random.randn(self.input_size, self.hidden_size1)
        self.b1 = np.random.randn(1, self.hidden_size1)

        self.w2 = np.random.rand(self.hidden_size1, self.hidden_size2)
        self.b2 = np.random.randn(1, self.hidden_size2)

        self.w3 = np.random.rand(self.hidden_size2, self.hidden_size3)
        self.b3 = np.random.randn(1, self.hidden_size3)

        self.w4 = np.random.randn(self.hidden_size3, self.out_size)
        self.b4 = np.random.randn(1, self.out_size)

    def _relu(self, Z):
        return np.maximum(Z, 0)
    
    def _derivative_relu(self, Z):
        return np.where(Z > 0, 1, 0)
    
    def _sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))
    
    def _derivative_sigmoid(self, Z):
        sig = self._sigmoid(Z)
        return sig * (1 - sig)
    
    def _ms_error(self, y, y_pred):
        return np.mean((y - y_pred) ** 2)
    
    def _derivative_ms(self, y, y_pred):
        return 2 * (y_pred - y) / y.size

    def forward(self, X):
        self.z1 = np.dot(X, self.w1) + self.b1
        self.a1 = self._relu(self.z1)

        self.z2 = np.dot(self.a1, self.w2) + self.b2
        self.a2 = self._relu(self.z2)

        self.z3 = np.dot(self.a2, self.w3) + self.b3
        self.a3 = self._relu(self.z3)

        self.z4 = np.dot(self.a3, self.w4) + self.b4
        self.a4 = self._sigmoid(self.z4)
        return self.a4

    def back_propagate(self, X, y):
        n = X.shape[0]

        da4 = self._derivative_ms(y, self.a4)
        dz4 = da4 * self._derivative_sigmoid(self.z4)
        dw4 = np.dot(self.a3.T, dz4) / n
        db4 = np.sum(dz4, axis=0, keepdims=True) / n

        da3 = np.dot(dz4, self.w4.T)
        dz3 = da3 * self._derivative_relu(self.z3)
        dw3 = np.dot(self.a2.T, dz3) / n
        db3 = np.sum(dz3, axis=0, keepdims=True) / n

        da2 = np.dot(dz3, self.w3.T)
        dz2 = da2 * self._derivative_relu(self.z2)
        dw2 = np.dot(self.a1.T, dz2) / n
        db2 = np.sum(dz2, axis=0, keepdims=True) / n

        da1 = np.dot(dz2, self.w2.T)
        dz1 = da1 * self._derivative_relu(self.z1)
        dw1 = np.dot(X.T, dz1) / n
        db1 = np.sum(dz1, axis=0, keepdims=True) / n

        self.w1 -= self.learning_rate * dw1
        self.b1 -= self.learning_rate * db1

        self.w2 -= self.learning_rate * dw2
        self.b2 -= self.learning_rate * db2

        self.w3 -= self.learning_rate * dw3
        self.b3 -= self.learning_rate * db3

        self.w4 -= self.learning_rate * dw4
        self.b4 -= self.learning_rate * db4
    
    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            y_pred = self.forward(X)
            loss = self._ms_error(y, y_pred)
            self.back_propagate(X, y)

            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")
             

