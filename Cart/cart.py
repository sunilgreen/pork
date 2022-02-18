import sys
import numpy as np
from preprocess import preprocess
from train_test import train
from train_test import test
import sklearn
import graphviz
import pandas as pd



np.set_printoptions(threshold=sys.maxsize)

X, y = preprocess()
clf = train(X, y)

# testing = pd.read_csv("../Data/Atlas2.csv") #Atlas 1 provided four 0000 identifiers, regardless of order of Is_Pork and Is_Not_Pork

# testY = testing[["is_pork"]]
# testing = testing.drop(["is_pork"], axis=1)

# print(clf.predict(testing))






#print(clf)

dot_data = sklearn.tree.export_graphviz(clf, feature_names=list(X.columns), class_names=["Is Not Pork", "Is Pork"], out_file=None, filled=True)
graph = graphviz.Source(dot_data, format="pdf")
graph.render("visualization", "../CartVisualizations/")
