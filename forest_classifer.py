from advanced_classifer import DecisionTreeClassifer
import numpy as np

class RandomForestClassifer:
    def __init__(self,estimators=10,min_sample_split=2,max_depth=float("inf")):
        self.estimators=estimators
        self.min_sample_split=min_sample_split
        self.max_depth=max_depth
        self.trees=[]

    def _bootstrap_sample(self,X,y):
        n_sample,n_features=X.shape
        indices=np.random.choice(n_sample,n_sample,replace=True)
        return X[indices],y[indices]

    def fit(self,X,y):
        for _ in range(self.estimators):
            x_sample,y_sample=self._bootstrap_sample(X,y)
            tree=DecisionTreeClassifer(min_sample_split=self.min_sample_split,max_depth=self.max_depth)
            tree.fit(x_sample,y_sample)
            self.trees.append(tree)

    def predict(self,X):
        predictions=np.array([tree.predict(X) for tree in self.trees])
        return np.array([np.bincount(X[:,index]) for index in range(predictions.shape[1])])
