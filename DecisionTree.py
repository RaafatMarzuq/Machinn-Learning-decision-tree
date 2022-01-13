from random import  randrange

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
            self.left = None
            self.right= None
            self.tag=tag
            self.isLeaf=True
            self.counter=0
            self.coordinate = randrange(8) 
            self.matchTag=0
            self.dontMatchTag=0
            self.vectors =[]

        
        def fringe(root):
                result = []
                if root.left:
                    result.extend(root.left.fringe())
                if root.right:
                    result.extend(root.right.fringe())
                if not result:
                    result = [root]
                return result  



        def insertQ1A(self ,vector,k):
            if k > 0:
                coordinate= self.coordinate
                print("coordinate1 = {}".format(coordinate))
                if vector[coordinate] == 0:
                    if self.left is None:
                        print("vector = {}".format(vector))
                        print("coordinate = {}".format(coordinate))
                        print("vector[coordinate] = {}".format(vector[coordinate]))
                        self.left = Tree(0)
                        k-=1
                        print("new left node")
                    else:
                        self.isLeaf=False
                        print("left")
                        self.left.insertQ1A(vector,k-1)
                elif vector[coordinate]==1:
                    if self.right is None:
                        print("vector = {}".format(vector))
                        print("coordinate = {}".format(coordinate))
                        print("vector[coordinate] = {}".format(vector[coordinate]))
                        self.right=Tree(1)
                        k-=1
                        print("new right node")
                    else:
                        self.isLeaf=False
                        print("right")
                        self.right.insertQ1A(vector,k-1)
            if k==0:
                    print("last level")   
                    if self.tag == vector[8]:
                                self.matchTag+=1
                    elif self.tag != vector[8]:
                                self.dontMatchTag+=1   
                    print("matching vector = {}".format(self.matchTag))
                    print("Not matching vector = {}".format(self.dontMatchTag))
                

            

f = open("vectors.txt", "r")
lines = f.read().splitlines() 
f.close() 


tree = Tree(-1)

for v in lines[:10]:
            
            line=v.split()
            vector = [int(i) for i in line]
            for j in range(2):
                print("{})".format(j+1))
                tree.insertQ1A(vector,2)
            print(" ")

leaves= tree.fringe()
for i in leaves:
    print(i.tag)
    print("The number of the matching vectors is {}".format(i.matchTag))
    print("The number of the not matching vectors is {}".format(i.dontMatchTag))


