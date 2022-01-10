import pandas
from sklearn import tree
# import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("vectors.txt")


class Tree:
    def __init__(self, val = None):
            if val != None:
                self.val = val
            else:
                self.val = None
                
            self.left = None
            self.right = None

    def insert(self, val):
            if self.val:
                if val < self.val:
                        if self.left is None:
                            self.left = Tree(val)
                        else:
                            self.left.insert(val)
                elif val > self.val:
                        if self.right is None:
                            self.right = Tree(val)
                        else:
                            self.right.insert(val)
            else:
                self.val = val