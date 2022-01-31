import sys
import numpy as np
from preprocess import preprocess
from train_test import train
from train_test import test
import sklearn
import graphviz


np.set_printoptions(threshold=sys.maxsize)

X, y = preprocess()
clf = train(X, y)

print(clf)

dot_data = sklearn.tree.export_graphviz(clf, feature_names=list(X.columns), class_names=["Is Pork", "Is Not Pork"], out_file=None, filled=True)
graph = graphviz.Source(dot_data, format="pdf")
graph.render("visualization", "../CartVisualizations/")
