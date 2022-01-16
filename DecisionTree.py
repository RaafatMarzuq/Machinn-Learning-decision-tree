from asyncio.windows_events import INFINITE
from errno import ENFILE
from logging import root
from random import  randrange
import math
from re import T
from turtle import left, right
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
        def __init__(self,tag):
            self.name=""
            self.left = None
            self.right= None
            self.tag=tag
            self.isLeaf=True
            self.counter=0
            self.coordinate = 0
            self.vectors_with_tag_1 = 0 
            self.matchTag=0
            self.vectors_with_tag_0=0
            self.vectors =[]
            self.min_error_coordinates=[]
            
       
        def getLeaves(root):
                result = []
                if root.left:
                    
                    result.extend(root.left.getLeaves())
                if root.right:
                    result.extend(root.right.getLeaves())
                if not result:
                    if root.vectors_with_tag_0 < root.vectors_with_tag_1:
                        root.tag = 1
                    else:
                        root.tag=0

                    result = [root]
                return result  

        def generateTree(self ,vectors, k,l,r):
                    self.left = Tree(0)
                    self.left.coordinate = l
                    self.right = Tree(1)
                    self.right.coordinate=r
                    for v in vectors:
                            self.insertQ1A(v , k-1)
                    leaves= self.getLeaves()
                    err_in_tree =0
                    for i in leaves:
                        if i.tag ==0 :
                            err_in_tree+= (i.vectors_with_tag_1)
                        elif i.tag == 1:
                            err_in_tree+=(i.vectors_with_tag_0 )
                
                    return (err_in_tree/150)
            
        def insertQ1A(self ,vector,k):
            if k > 0:
                coordinate= self.coordinate 
                if vector[coordinate] == 0:
                    if self.left is None:
                        self.left = Tree(0)
                        self.left.name = "<-- left"
                        self.left.insertQ1A(vector,k-1)
                        k-=1
                    else:
                        self.isLeaf=False
                        self.left.name = "<-- left"
                        self.left.insertQ1A(vector,k-1)
                elif vector[coordinate]==1:
                    if self.right is None:
                        self.right=Tree(1)
                        self.right.name = "right -->"
                        self.right.insertQ1A(vector,k-1)
                        k-=1
                    else:
                        self.isLeaf=False
                        self.right.name = "right -->"
                        self.right.insertQ1A(vector,k-1)
            if k==0:
                # print("last level")
                    self.counter+=1
                    if vector[8] ==1:
                                self.vectors_with_tag_1+=1
                    elif vector[8] == 0 :
                                self.vectors_with_tag_0+=1   
        def getEntropy(self):
            binary_entropy=1
            if self.counter == 0:
                return binary_entropy
            else:
                if self.vectors_with_tag_0 ==0 or self.vectors_with_tag_1==0:
                    binary_entropy=0
                else:
                        p= float(self.vectors_with_tag_0/self.counter)
                       
                        binary_entropy = (-(p)*(math.log2(p))) - ((1-p)*(math.log2(1-p)))
            
            return binary_entropy

        def split(self,vectors,i):
                n = len(vectors[0]) -1
                best_i=0
                left,right = Tree(0) ,Tree(1)
                left_entropy = INFINITE
                right_entropy=INFINITE
                min_B_entropy = INFINITE
                self.left = Tree(0)
                self.right= Tree(1)
                # print("left vectors = {}".format(self.left.vectors))
                # print("right vectors = {}".format(self.right.vectors))
                for v in vectors: 
                    if v[i] == 0 and v[n]==0:
                        self.left.counter+=1
                        self.left.vectors_with_tag_0+=1
                        self.left.vectors.append(v)                    
                    elif v[i] == 0  and v[n]==1:
                        self.left.counter+=1
                        self.left.vectors_with_tag_1 +=1
                        self.left.vectors.append(v)
                    elif v[i] == 1 and v[n] == 0:
                        self.right.counter+=1
                        self.right.vectors_with_tag_0+=1
                        self.right.vectors.append(v)
                    elif v[i] == 1 and v[n] == 1 :
                        self.right.counter+=1
                        self.right.vectors_with_tag_1+=1
                        self.right.vectors.append(v)
                    
                    left_entropy = self.left.getEntropy()
                    right_entropy = self.right.getEntropy()
                    if  (left_entropy + right_entropy) < min_B_entropy:
                        min_B_entropy = left_entropy + right_entropy
                        best_i=i
                        left = self.left
                        right=self.right
                    
                        
                    # print("left  = {}".format(left.vectors))
                    # print("right  = {}".format(right.vectors))
                    return [best_i,left,right] 
                    

        def insertQ1B(self,k,vectors):
            
            n = len(vectors[0])

            for i in range(n):
                self.split(vectors,i)
            
            return 

            

            
            
            




                    




def Q1A(vectors , k):
    n= len(vectors[0])-1
    min_error= INFINITE
    best_indexs=[]
    for i in range(n):
        for l in range(n): 
           for r in range(n):
                tree = Tree(-1)
                tree.coordinate=i
                tree.name="Root" 
                # print("new tree")   
                tree_error= tree.generateTree(vectors,k,l,r)
                if tree_error < min_error:
                    min_error= tree_error
                    tree.min_error_coordinates.append("Root cooardinare {}".format(i))
                    tree.min_error_coordinates.append("Left Node cooardinare {}".format(l))
                    tree.min_error_coordinates.append("Right Node cooardinare {}".format(r))
                    # print("new min error = {:.2f}".format(min_error))
                    
                    best_indexs=[tree,min_error]
                    
    
    return best_indexs


def main(vectors,k):
        best_tree= Q1A(vectors,k)
        tree =Tree(-1)
        tree =best_tree[0]
        tree_error=best_tree[1]   
        for i in tree.min_error_coordinates:
            print(i)
        print("with error = {:.2f}".format(tree_error))
        
        # print("The {} levels tree with the lowest error is the one with:".format(k)) 
        # print("root cooardinate {}".format(best_coordinates[0]))
        # print("left node coordinate {}".format(best_coordinates[1]))
        # print("right node coordinate {}".format(best_coordinates[2]))
        # print("with error = {:.2f}".format(best_coordinates[3]))
    # tree=Tree(-1)
    # tree.insertQ1B(3,vectors)

if __name__ == '__main__':
   
    f = open("vectors.txt", "r")
    lines = f.read().splitlines() 
    f.close() 
    vectors = []
    for v in lines:    
                line=v.split()
                vector = [int(i) for i in line]
                vectors.append(vector)
    
    main(vectors,3)