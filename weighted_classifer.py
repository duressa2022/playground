from collections import Counter
import numpy as np
class Node:
    def __init__(self,feature=None,threshold=None,left=None,right=None,value=None):
        self.feature=feature
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value

class DecisionTreeClassfier:
    def __init__(self,min_sample_splits=2,max_depth=float("inf"),criterion="entropy"):
        self.min_sample_splits=min_sample_splits
        self.max_depth=max_depth
        self.criterion=criterion
        self.root=None

    def _gini(self,y,sample_weights):
        if len(y)==0:
            return 0
        
        Classes,counts=np.unique(y,return_counts=True)
        total_weight=np.sum(sample_weights)

        gini=1
        for cls,count in zip(Classes,counts):
            mask=(y==cls)
            weighted_class_count=np.sum(sample_weights[mask])
            weighted_class_prob=weighted_class_count/total_weight
            gini-=weighted_class_prob**2
        return gini
    
    def _entropy(self,y,sample_weights):
        if len(y)==0:
            return 0
        
        Classes,counts=np.unique(y,return_counts=True)
        total_weight=np.sum(sample_weights)

        entropy=0
        for cls,count in zip(Classes,counts):
            mask=(y==cls)
            weighted_class_count=np.sum(sample_weights[mask])
            weighted_class_prob=weighted_class_count/total_weight
            entropy+=weighted_class_prob*np.log2(weighted_class_prob+1e-9)
        return -entropy
    
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
                if self.criterion=="entropy":
                    weighted_error=(len(y_left)*self._entropy(y_left,sample_weights)+len(y_right)*self._entropy(y_right,sample_weights))/len(y)
                elif self.criterion=="gini":
                    weighted_error=(len(y_left)*self._gini(y_left,sample_weights)+len(y_right)*self._gini(y_right,sample_weights))/len(y)

                if weighted_error<best_error:
                    best_error=weighted_error
                    best_feature=feature
                    best_threshold=threshold

        if baseline_error-best_error<1e-9:
            return None,None
        return best_feature,best_threshold
    
    def _leaf_value(self,y,sample_weights):
        counter=Counter()
        classes=np.unique(y)

        for cls in classes:
            mask=(y==cls)
            counter[cls]=np.sum(sample_weights[mask])
        
        return counter.most_common(1)[0][0]


    def _build_tree(self,X,y,sample_weights,depth=0):
        n_samples,n_features=X.shape
        n_labels=len(np.unique(y))

        if n_samples<self.min_sample_splits or depth>=self.max_depth or n_labels==1:
            leaf_value=self._leaf_value(y,sample_weights)
            return Node(value=leaf_value)
        
        feature,threshold=self._best_split(X,y,sample_weights)
        if feature is None:
            leaf_value=self._leaf_value(X,y,sample_weights)
            return Node(value=leaf_value)
        
        left_indices,right_indices=self._split(X[:,feature],threshold)
        left_subtree=self._build_tree(X[left_indices],y[left_indices],sample_weights)
        right_subtree=self._build_tree(X[right_indices],y[right_indices],sample_weights)

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


class AdaptiveBoosting:
    def __init__(self,n_estimators=100,base_estimator=None,learning_rate=1):
        self.n_estimators=n_estimators
        self.base_estimator=base_estimator
        self.learning_rate=learning_rate
        self.estimators=[]
        self.performances=[]

    def _clone_estimator(self):
        return self.base_estimator if self.base_estimator else DecisionTreeClassfier(max_depth=1)

    def fit(self,X,y):
        n_samples,n_features=X.shape
        sample_weights=np.ones(n_samples)/n_samples

        for _ in range(self.n_estimators):
            estimator=self._clone_estimator()
            estimator.fit(X,y,sample_weights)
            y_pred=estimator.predict(y)

            total_weight=np.sum(sample_weights)
            error=np.sum(sample_weights[y!=y_pred])/total_weight
            performance=0.5*np.log((1-error)/error)*self.learning_rate

            sample_weights=sample_weights*np.exp(performance)
            sample_weights=sample_weights/np.sum(sample_weights)
            self.estimators.append(estimator)
            self.performances.append(performance)

    def binary_predict(self,X):
        predictions=np.array([performance*estimator.predict(X) for performance,estimator in zip(self.performances,self.estimators)])
        final_prediction=np.sign(np.sum(predictions,axis=0))
        return (final_prediction>0).astype(int)
    
    def multi_class_predict(self,X):
        n_samples=X.shape[0]
        n_classes=len(np.unique(X))

        predictions=np.zeros((n_samples,n_samples))
        for performance,estimator in zip(self.performances,self.estimators):
            y_pred=estimator.predict(X)

            for cls in range(n_classes):
                predictions[:,cls]+=performance*(y_pred==cls)

        return np.argmax(predictions,axis=1)
    
    










    

