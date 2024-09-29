from decision_regressor import DecisionTreeRegressor
import numpy as np

class RandomForestRegressor:
    def __init__(self,estimators,min_sample_split=2,max_depth=float("inf")):
        self.estimators=estimators
        self.min_sample_split=min_sample_split
        self.max_depth=max_depth
        self.trees=[]

    def _random_sample(self,X,y):
        n_samples,n_features=X.shape
        indices=np.random.choice(n_samples,n_samples,replace=True)
        return X[indices],y[indices]
    
    def fit(self,X,y):
        for _ in range(self.estimators):
            X_sample,y_sample=self._random_sample(X,y)
            tree=DecisionTreeRegressor(min_sample_split=self.min_sample_split,max_depth=self.max_depth)
            self.trees.append(tree)
    
    def predict(self,y):
        tree_predictions=np.array([tree.predict(y) for tree in self.trees])
        return np.mean(tree_predictions,axis=0)

        