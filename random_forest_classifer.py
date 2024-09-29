from advanced_classifer import DecisionTreeClassifer
import numpy as np

class RandomForestClassifer:
    def __init__(self,estimators=100,min_sample_splits=2,max_depth=float("inf")):
        self.estimators=estimators
        self.min_sample_splits=min_sample_splits
        self.max_depth=max_depth
        self.trees=[]

    def _random_sample(self,X,y):
        n_samples,n_features=X.shape
        indices=np.random.choice(n_samples,n_samples,replace=True)
        return X[indices],y[indices]
    
    def fit(self,X,y):
        for _ in range(self.estimators):
            X_sample,y_sample=self._random_sample(X,y)
            tree=DecisionTreeClassifer(min_sample_split=self.min_sample_splits,max_depth=self.max_depth)
            tree.fit(X_sample,y_sample)
            self.trees.append(tree)

    def predict(self,y):
        tree_predictions=np.array([tree.predict(y) for tree in self.trees])
        return np.array([np.argmax(np.bincount(tree_predictions[:,index])) for index in range(tree_predictions.shape[1])])