from typing import no_type_check
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("vectors.txt")


from random import random, randrange

# class Node:
#     def __init__(self,coordinate,tag) :
#         self.left=None
#         self.right=None
#         self.tag=tag
#         self.isLeaf=True
#         self.counter=0
#         self.coordinate = coordinate
#         self.matchTag=0
#         self.dontMatchTag=0

class Tree:

    def __init__(self,tag,k):
            self.left=None
            self.right=None
            self.tag=tag
            self.isLeaf=True
            self.counter=0
            self.coordinate = randrange(8)
            self.matchTag=0
            self.dontMatchTag=0
            self.k =k
    # def printValues(self):
    #     if self.root.left:
    #         self.root.left.printValues()
    #     print(self.root.tag)
    #     if self.root.right:
    #         self.root.right.printValues()
    # def insert(self,Vector):
    #             if Vector[self.coordinate] == 1:
    #                 self.coordinate = randrange(8)
    #                 print(1)
    #                 print("coordinat is = {}".format(self.coordinate))
    #                 self.left=Tree(1,self.k)
    #                 self.isLeaf=False
    #             else:
    #                 self.coordinate = randrange(8)
    #                 print(0)
    #                 print("coordinat is = {}".format(self.coordinate))
    #                 self.left=Tree(0,self.k)
    #                 self.isLeaf=False

    def insertQ1(self,Vector):
        print(Vector)
            # print("coordinat is = {}".format(self.coordinate))
        if self.tag==-1:
            if Vector[self.coordinate] == 1:
                if self.right is None:
                    print("coordinat is = {}".format(self.coordinate))
                    self.coordinate = randrange(8)
                    print(1) 
                    self.right=Tree(1,self.k)
                    self.isLeaf=False
                else:
                    self.right.insertQ1(Vector)
            else:
                if self.left is None:
                    print("coordinat is = {}".format(self.coordinate))
                    self.coordinate = randrange(8)
                    print(0)
                    self.left=Tree(0,self.k)
                    self.isLeaf=False
                else:
                    self.left.insertQ1(Vector)
        if self.tag==0:
            if Vector[self.coordinate] == 1:
                if self.right is None:
                    print("coordinat is = {}".format(self.coordinate))
                    self.coordinate = randrange(8)
                    print(1) 
                    self.right=Tree(1,self.k)
                    self.isLeaf=False
                else:
                    self.right.insertQ1(Vector)
            else:
                if self.left is None:
                    print("coordinat is = {}".format(self.coordinate))
                    self.coordinate = randrange(8)
                    print(0)
                    self.left=Tree(0,self.k)
                    self.isLeaf=False
                else:
                    self.left.insertQ1(Vector)  
        if self.tag==1:
            if Vector[self.coordinate] == 1:
                if self.right is None:
                    print("coordinat is = {}".format(self.coordinate))
                    self.coordinate = randrange(8)
                    print(1) 
                    self.right=Tree(1,self.k)
                    self.isLeaf=False
                else:
                    self.right.insertQ1(Vector)
            else:
                if self.left is None:
                    print("coordinat is = {}".format(self.coordinate))
                    self.coordinate = randrange(8)
                    print(0)
                    self.left=Tree(0,self.k)
                    self.isLeaf=False
                else:
                    self.left.insertQ1(Vector)      
               
                # self.insert(Vector)
            
                # if self.tag == 0 :
                #     if self.left:
                #         self.left.insertQ1(Vector)
                #         self.isLeaf=False
                #     else:
                #         self.left=Tree(0,self.k)
                # else:
                #     if self.right:
                #         self.right.insertQ1(Vector)
                #         self.isLeaf=False
                #     else:
                #         self.right=Tree(1,self.k)
                
                # if self.isLeaf:
                #     self.counter +=1
                #     if self.tag == Vector[8] :
                #             self.matchTag +=1
                #     else:
                #             self.dontMatchTag +=1

tree = Tree(-1,3)
vector = [[0 ,1 ,0 ,0 ,1 ,1, 0 ,0 ,1],[1 ,0 ,0 ,1 ,0 ,1, 1, 1 ,0] ,[1, 1, 1, 0, 0, 0 ,0, 0, 1]]


for v in df:
    for i in range(tree.k):
        tree.insertQ1(v)
print("The number of the matching vectors is {}\n".format(tree.matchTag))

# tree.printValues()
