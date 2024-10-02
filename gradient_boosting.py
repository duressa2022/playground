import numpy as np
class Node:
    def __init__(self,feature=None,threshold=None,left=None,right=None,value=None):
        self.feature=feature
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value

class DecisionTreeRegressor:
    def __init__(self,min_sample_splits=2,max_depth=float("inf")):
        self.min_sample_splits=min_sample_splits
        self.max_depth=max_depth
        self.root=None

    def _mean_squared_error(self,y):
        if len(y)==0:
            return np.inf
        
        mean_y=np.mean(y)
        return np.sum((y-mean_y**2))
    
    def _splits(self,X_column,threshold):
        left_indices=np.where(X_column<=threshold)
        right_indices=np.where(X_column>threshold)
        return left_indices,right_indices
    
    def _best_splits(self,X,y):
        n_samples,n_features=X.shape
        best_feature,best_threshold=None,None
        best_error=float("inf")

        baseline_error=self._mean_squared_error(y)

        for feature in range(n_features):
            X_column=X[:,feature]
            thresholds=np.unique(X_column)

            for threshold in thresholds:
                left_indices,right_indices=self._splits(X_column,threshold)
                if len(left_indices)==0 or len(right_indices)==0 or len(left_indices)<self.min_sample_splits or len(right_indices)<self.min_sample_splits:
                    continue

                y_left,y_right=y[left_indices],y[right_indices]
                weighted_error=(len(y_left)*self._mean_squared_error(y_left)+len(y_right)*self._mean_squared_error(y_right)/len(y))

                if weighted_error<best_error:
                    best_error=weighted_error
                    best_feature=feature
                    best_threshold=threshold

            if baseline_error-best_error<1e-9:
                return None,None
            return best_feature,best_threshold
        
    def _build_tree(self,X,y,depth=0):
        n_samples,n_features=X.shape
        n_labels=np.unique(y)

        if n_samples<self.min_sample_splits or depth>self.max_depth or n_labels==1:
            leaf_value=np.mean(y)
            return Node(value=leaf_value)
        
        feature,threshold=self._best_splits(X,y)
        if feature is None:
            leaf_value=np.mean(y)
            return Node(value=leaf_value)
        

        left_indices,right_indices=np.split(X[:,feature],threshold)
        left_subtree=self._build_tree(X[left_indices],y[left_indices],depth+1)
        right_subtree=self._build_tree(X[right_indices],y[right_indices],depth+1)

        return Node(feature=feature,threshold=threshold,left=left_subtree,right=right_subtree)
    
    def fit(self,X,y):
        self.root=self._build_tree(X,y)

    def _traverse_tree(self,x,node):
        if node.value is not None:
            return node.value
        if x[node.feature]<=node.threshold:
            return self._traverse_tree(x,node.left)
        else:
            return self._traverse_tree(x,node.right)
        
    def predict(self,X):
        return np.array([self.predict(x,self.root) for x in X])
    
class GradeintBoostingClassifer:
    def __init__(self,n_estimators,learning_rate=0.01,max_depth=3):
        self.n_estimators=n_estimators
        self.mean_prediction=None
        self.learning_rate=learning_rate
        self.max_depth=3
        self.models=[]

    def fit(self,X,y):
        n_samples,n_features=X.shape
        self.mean_prediction=np.mean(y)
        self.current_prediction=np.full(n_samples,self.mean_prediction)

        for _ in range(self.n_estimators):
            model=DecisionTreeRegressor(self.max_depth)
            error=y-self.mean_prediction
            model.fit(X,error)
            current_error=model.predict(X)

            self.current_prediction+=self.learning_rate*current_error
            self.models.append(model)

    def predict(self,X):
        predictions=np.full(X.shape[0],self.mean_prediction)
        for model in self.models:
            predictions+=self.learning_rate*model.predict(X)
        return predictions

        




        
