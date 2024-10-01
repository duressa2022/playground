import numpy as np

class Node:
    def __init__(self,feature=None,threshold=None,left=None,right=None,value=None):
        self.feature=feature
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value

class DecisionTreeClassifier:
    def __init__(self,min_sample_splits=2,max_depth=float("inf"),criterion="entropy"):
        self.min_sample_splits=min_sample_splits
        self.max_depth=max_depth
        self.criterion=criterion
        self.root=None

    def _entropy(self,y,sample_weights):
        if len(y)==0:
            return np.inf
        
        Classes,counts=np.unique(y,return_counts=True)
        total_weight=np.sum(sample_weights)
        
        entropy=0
        for cls,count in zip(Classes,counts):
            mask=(y==cls)
            class_weight_count=np.sum(sample_weights[mask])
            class_weight_prob=class_weight_count/total_weight
            entropy+=class_weight_prob*np.log2(class_weight_prob+1e-9)
        return -entropy
    
    def _gini(self,y,sample_weights):
        if len(y)==0:
            return np.inf
        
        classes,counts=np.unique(y,return_counts=True)
        total_weight=np.sum(sample_weights)

        gini=1
        for cls,count in zip(classes,counts):
            mask=(y==cls)
            class_weight_count=np.sum(sample_weights[mask])
            class_weight_prob=class_weight_count/total_weight
            gini-=class_weight_prob**2
        return gini
    
    def _split(self,X_column,threshold):
        if isinstance(threshold,(int,float)):
            left_indices=np.where(X_column<=threshold)
            right_indices=np.where(X_column>threshold)
        else:
            left_indices=np.where(X_column==threshold)
            right_indices=np.where(X_column!=threshold)
        return left_indices,right_indices
    
    def _best_split(self,X,y,sample_weights):
        n_samples,n_features=X.shape
        best_feature,best_threshold=None,None
        best_error=float("inf")

        baseline_error=self._entropy(y,sample_weights) if self.criterion=="entropy" else self._gini(y,sample_weights)

        for feature in range(n_features):
            X_column=X[:,feature]
            thresholds=np.unique(X_column)

            for threshold in thresholds:
                left_indices,right_indices=self._split(X_column,threshold)
                if len(left_indices)==0 or len(right_indices)==0 or len(left_indices)<self.min_sample_splits or len(right_indices)<self.min_sample_splits:
                    continue

                y_left,y_right=y[left_indices],y[right_indices]
                left_weight,right_weight=sample_weights[left_indices],sample_weights[right_indices]

                if self.criterion=="entropy":
                    weighted_error=(len(y_left)*self._entropy(y_left,left_weight)+len(y_right)*self._entropy(y_right,right_weight))/len(y)
                else:
                    weighted_error=(len(y_left)*self._gini(y_left,left_weight)+len(y_right)*self._gini(y_right,right_weight))/len(y)
                
                if weighted_error<best_error:
                    best_error=weighted_error
                    best_feature=feature
                    best_threshold=threshold

        if baseline_error-best_error<1e-9:
            return None,None
        return best_feature,best_threshold
    
    def _build_tree(self,X,y,samples_weights,depth):
        n_samples,n_features=X.shape
        n_labels=np.unique(y)

        if n_samples<self.min_sample_splits or depth>=self.max_depth or n_labels==1:
            leaf_value=(np.sum(y)>0).astype(int)
            return Node(value=leaf_value)
        
        feature,threshold=self._best_split(X,y,samples_weights)
        if feature is None:
            leaf_value=(np.sum(y)>0).astype(int)
            return Node(value=leaf_value)
        
        left_indices,right_indices=self._split(X[:,feature],threshold)
        left_subtree=self._build_tree(X[left_indices],y[left_indices],samples_weights[left_indices],depth+1)
        right_subtree=self._build_tree(X[right_indices],y[right_indices],samples_weights[right_indices],depth+1)
        return Node(feature=feature,threshold=threshold,left=left_subtree,right=right_subtree)
    
    def fit(self,X,y,sample_weights):
        self.root=self._build_tree(X,y,sample_weights)
            
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
    

class AdaBoostClassifer:
    def __init__(self,n_estimators=100,learning_rate=1):
        self.n_estimators=n_estimators
        self.learning_rate=learning_rate
        self.models=[]

    def fit(self,X,y):
        n_samples,n_features=X.shape

        sample_weights=np.ones(n_samples)/n_samples
        
        for _ in range(self.n_estimators):
            model=DecisionTreeClassifier(max_depth=1)
            model.fit(X,y,sample_weights)
            y_pred=model.predict(X)

            error=np.sum(sample_weights[y_pred!=y])/np.sum(sample_weights)
            performance=0.5*np.log2((1-error)/(error+1e-9))

            sample_weights=self.learning_rate*sample_weights*np.exp(-performance*y*y_pred)
            sample_weights=sample_weights/len(sample_weights)

            self.models.append((model,performance))

    def predict(self,X):
        predictions=np.array([model.predict(X)*performance for model,performance in self.models])
        final_prediction=np.sum(predictions,axis=0)
        return (final_prediction>0).astype(int)

        
    



