import numpy as np

class Node:
    def __init__(self,feature,threshold,left=None,right=None,value=None):
        self.feature=feature
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value

class DecisionTreeRegressor:
    def __init__(self,min_sample_split=2,max_depth=float("inf")):
        self.min_sample_split=min_sample_split
        self.max_depth=max_depth
        self.root=None

    def _mean_squared_error(self,y):
        if len(y)==0:
            return 0
        mean_y=np.mean(y)
        return np.sum((y-mean_y)**2)
    
    def _split(self,X_column,threshold):
        left_indices=np.where(X_column<=threshold)[0]
        right_indices=np.where(X_column>threshold)[0]
        return left_indices,right_indices
    
    def _best_split(self,X,y):
        n_samples,n_features=X.shape
        best_feature,best_threshold=None,None
        best_mse=float("inf")

        baseline_mse_data=self._mean_squared_error(y)

        for feature in range(n_features):
            X_column=X[:,feature]
            thresholds=np.unique(X_column)

            for threshold in thresholds:
                left_indices,right_indices=self._split(X_column,threshold)
                if len(left_indices)==0 or right_indices==0:
                    return None,None
                
                y_left,y_right=y[left_indices],y[right_indices]
                weighted_mse=(len(y_left)*self._mean_squared_error(y_left)+len(y_right)*self._mean_squared_error(y_right))/len(y)

                if weighted_mse<best_mse:
                    best_mse=weighted_mse
                    best_feature=feature
                    best_threshold=threshold
        if baseline_mse_data-best_mse<1e-9:
            return None,None
        return best_feature,best_threshold
    
    def _build_tree(self,X,y,depth=0):
        n_samples,n_features=X.shape
        n_labels=len(np.unique(y))

        if n_samples<self.min_sample_split or depth>=self.max_depth or n_labels==1:
            leaf_value=np.mean(y)
            return Node(value=leaf_value)
        
        feature,threshold=self._best_split(X,y)
        if feature is None:
            leaf_value=np.mean(y)
            return Node(value=leaf_value)
        
        left_indices,right_indices=self._split(X[:,feature],threshold)
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
        return np.array([self._traverse_tree(x,self.root) for x in X])

    




    