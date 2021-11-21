from sklearn.tree import DecisionTreeClassifier

def train(X_train, y_train, threshold=None):

    if threshold is None:
        clf = DecisionTreeClassifier()
    else:   
        clf = DecisionTreeClassifier(min_impurity_decrease=threshold)
    clf = clf.fit(X_train,y_train)

    return clf

def test(X_test, clf):
    return clf.predict(X_test)