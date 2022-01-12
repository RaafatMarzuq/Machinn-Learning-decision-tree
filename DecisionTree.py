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
        def __init__(self):
            self.left = None
            self.right= None
            self.tag=None
            self.isLeaf=True
            self.counter=0
            self.coordinate = randrange(8) 
            self.matchTag=0
            self.dontMatchTag=0

        #  def _insert(self):
        #      if 

        def insertQ1A(self ,vector):
            coordinate= self.coordinate
            print(coordinate)
            
            print("vector[coordinate] = {}".format(vector[coordinate]))
            if vector[coordinate] == 0:
                print(vector)
                if self.left is None:
                    self.left = Tree()
                    print("new left node")
                else:
                    self.isLeaf=False
                    self.left.insertQ1A(vector)
            elif vector[coordinate]==1:
                print(vector)
                if self.right is None:
                    self.right=Tree()
                    print("new right node")
                else:
                    self.isLeaf=False
                    self.right.insertQ1A(vector)
            




            

      
               

f = open("vectors.txt", "r")
lines = f.read().splitlines() # List with stripped line-breaks
f.close() # Close file

# print(lines)
tree = Tree()

for v in lines:
            line=v.split()
            vector = [int(i) for i in line]
            for j in range(3):
                tree.insertQ1A(vector)
# print("The number of the notmatching vectors is {}\n".format(tree.dontMatchTag))

# tree.printValues()
