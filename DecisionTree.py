from typing import no_type_check
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("vectors.txt")


from random import random, randrange

class Node:
    def __init__(self,coordinate,tag) :
        self.left=None
        self.right=None
        self.tag=tag
        self.isLeaf=True
        self.counter=0
        self.coordinate = coordinate
        self.matchTag=0
        self.dontMatchTag=0

class Tree:

    def __init__(self,tag,k):
            self.root = None
            self.k=k

    def insertA(self ,Vector):
        if self.root is None:
            print(Vector)
            coordinate = randrange(8)
            print(coordinate)
            self.root= Node(coordinate, -1)
        else:
            print("root is not None")
            self.insertQ1(self.root,Vector)

    def insertQ1(self,cur_node,Vector):
            
            if self.root is None:
                print(Vector)
                coordinate = randrange(8)
                print(coordinate)
                self.root= Node(coordinate, -1)
            else:
                print("root is not None")
                self.insertQ1(self.root,Vector)

            if  Vector[coordinate] == 0:
                if cur_node.left is None:
                    coordinate = randrange(8)
                    cur_node.left = Node(coordinate,0)
                    print (" new left node ")
                else:
                    print("left is not None")
                    self.insertQ1(cur_node.left , Vector)
            else:
                if cur_node.right is None:
                    coordinate = randrange(8)
                    cur_node.right = Node(coordinate,1)
                    print (" new right node ")
                else:
                    print("right is not None")
                    self.insertQ1(cur_node.right , Vector)

            
      
               



tree = Tree(-1,3)
root = tree.root


for i in range(tree.k):
    for v in df:
        tree.insertQ1(root,v)
# print("The number of the notmatching vectors is {}\n".format(tree.dontMatchTag))

# tree.printValues()
