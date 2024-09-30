from decision_regressor import DecisionTreeRegressor
import numpy as np

class RandomForestRegressor:
    def __init__(self,estimators=10,min_sample_splits=2,max_depth=float("inf")):
        self.estimators=estimators
        self.min_sample_splits=min_sample_splits
        self.max_depth=max_depth
        self.trees=[]

    def _bootstrap_sample(self,X,y):
        n_samples,n_features=X.shape
        indices=np.random.choice(n_samples,n_samples,replace=True)
        return X[indices],y[indices]
    
    def fit(self,X,y):
        for _ in range(self.estimators):
            x_sample,y_sample=self._bootstrap_sample(X,y)
            tree=DecisionTreeRegressor(min_sample_split=self.min_sample_splits,max_depth=self.max_depth)
            tree.fit()
            self.trees.append(tree)

    def predict(self,X):
        predictions=np.array([tree.predict(X) for tree in self.trees])
        return np.mean(predictions,axis=0)