import numpy as np
class Node:
    def __init__(self,feature=None,threshold=None,left=None,right=None,value=None):
        self.feature=feature
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value

class DecisionTreeClassifer:
    def __init__(self,min_sample_split=2,max_depth=float("inf"),criterion="entropy"):
        self.min_sample_split=min_sample_split
        self.max_depth=max_depth
        self.criterion=criterion
        self.root=None

    def _entropy(self,y):
        if len(y)==0:
            return 0
        
        Class,counts=np.unique(y,return_counts=True)
        probs=counts/len(y)
        return -np.sum(p*np.log2(p+1e-9) for p in probs)
    
    def _gini(self,y):
        if len(y)==0:
            return 0
        
        Class,counts=np.unique(y,return_counts=True)
        probs=counts/len(y)
        return 1-np.sum(p**2 for p in probs)
    
    def _split(self,X_column,threshold):
        if isinstance(threshold,(int,float)):
            left_indices=np.where(X_column<=threshold)
            right_indices=np.where(X_column>threshold)
        else:
            left_indices=np.where(X_column==threshold)
            right_indices=np.where(X_column!=threshold)
        return left_indices,right_indices
    
    def _best_split(self,X,y):
        n_samples,n_features=X.shape
        best_feature,best_threshold=None,None
        best_error=float("inf")

        baseline_error=self._entropy(y) if self.criterion=="entropy" else self._gini(y)

        for feature in range(n_features):
            X_column=X[:,feature]
            thresholds=np.unique(X_column)

            for threshold in thresholds:
                left_indices,right_indices=self._split(X_column,threshold)
                if len(left_indices)==0 or len(right_indices)==0:
                    continue

                y_left,y_right=y[left_indices],y[right_indices]
                if self.criterion=="entropy":
                    weighted_error=(len(y_left)*self._entropy(y_left)+len(y_right)*self._entropy(y_right))/len(y)
                elif self.criterion=="gini":
                    weighted_error=(len(y_left)*self._gini(y_left)+len(y_right)*self._gini(y_right))/len(y)

                if weighted_error<best_error:
                    best_error=weighted_error
                    best_feature=feature
                    best_threshold=threshold

        if baseline_error-best_error<1e-9:
            return None,None
        return best_feature,best_threshold
    
    def _build_tree(self,X,y,depth=0):
        n_samples,n_features=X.shape
        n_labesl=len(y)

        if n_samples<self.min_sample_split or depth>=self.max_depth or n_labesl==1:
            leaf_value=np.argmax(np.bincount(y))
            return Node(value=leaf_value)
        
        feature,threshold=self._best_split(X,y)
        if feature is None:
            leaf_value=np.argmax(np.bincount(y))
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
        
        if isinstance(node.threshold,(int,float)):
            if x[node.feature]<=node.threshold:
                return self._traverse_tree(x,node.left)
            else:
                return self._traverse_tree(x,node.right)
        else:
            if x[node.feature]==node.threshold:
                return self._traverse_tree(x,node.left)
            else:
                return self._traverse_tree(x,node.right)
            
    def predict(self,X):
        return np.array([self._traverse_tree(x,self.root) for x in X])
    




    