from itertools import count
from random import  randrange


class Node:
    def __init__(self , isleaf = False, tag=1) :
        self.left=None
        self.right=None
        self.tag=tag
        self.isLeaf=isleaf
        self.counter=0
        self.coordinate = 0
        self.matchTag=0
        self.dontMatchTag=0
    
class Tree:
        def __init__(self,k):
            self.root=Node()
            self.k=k
            self.matches=0


def Recursion(k, coordinate_num, vectors ,t):
    t1=Tree(k)
    for i in range(coordinate_num):
        t=Tree(k)
        t.root.coordinate=i
        # print("coooooooooooo", t.root.coordinate)

        # print("gggggg",t1.root.coordinate)

        for j in range(coordinate_num): # to get the best left and right node 
            if(j!=i):
                t.root.left=Node()
                left=t.root.left
                count1=0 
                count2=0
                for v in vectors:
                    if(v[i]==0 and v[j]==0 and v[8]==0):
                        count1+=1
                    elif(v[i]==0 and v[j]==0 and v[8]==1):               
                        count2+=1 

                    if(v[i]==0 and v[j]==1 and v[8]==1) : 
                        count1+=1
                    elif(v[i]==0 and v[j]==1 and v[8]==0):
                        count2+=1
                if( count1>count2 and count1>left.matchTag):
                    left.left=Node(True,0)
                    left.right=Node(True,1)
                    left.counter=1
                    left.matchTag=count1
                    left.coordinate=j
                elif count2>left.matchTag:
                    left.left=Node(True,1)
                    left.right=Node(True,0)
                    left.counter=2
                    left.matchTag=count2
                    left.coordinate=j
                # print("left matching = ", left.matchTag)

                
                t.root.right=Node()
                right=t.root.right
                count1=0 
                count2=0
                for v in vectors:
                    if(v[i]==1 and v[j]==0 and v[8]==0):
                        count1+=1 
                    elif(v[i]==1 and v[j]==0 and v[8]==1):               
                        count2+=1 

                    if(v[i]==1 and v[j]==1 and v[8]==1) : 
                        count1+=1
                    elif (v[i]==1 and v[j]==1 and v[8]==0):
                        count2+=1
                if( count1>count2 and count1> right.matchTag):
                    right.left=Node(True,0)
                    right.right=Node(True,1)
                    right.counter=1
                    right.matchTag=count1
                    right.coordinate=j
                elif count2>right.matchTag:
                    right.left=Node(True,1)
                    right.right=Node(True,0)
                    right.counter=2
                    right.matchTag=count2
                    right.coordinate=j
                # print("right matching = ", right.matchTag)

        print("coordinate = ", t.root.coordinate)
        print("t right = ", t.root.right.matchTag)
        print("t left = ", t.root.left.matchTag)
        print("t left coord = ", t.root.left.coordinate)
        print("t right coord = ", t.root.right.coordinate)
        print("t left counter = ", t.root.left.counter)
        print("t right counter = ", t.root.right.counter)



        t.root.matchTag=t.root.left.matchTag+t.root.right.matchTag
        if(t.root.matchTag>t1.root.matchTag):
            t1=t
            # print("false", t1.root.coordinate)
            # print("false", t1.root.left.coordinate)
            # print("false", t1.root.right.coordinate)



    return t1
                
                   
                            
 
  


if __name__ == '__main__':
    
    all_vectors = []
    f = open("vectors.txt", "r")
    for line_data in f:
        single_vector = line_data.split()
        single_vector = [int(single_vector[0]), int(single_vector[1]), int(single_vector[2]),int(single_vector[3]),int(single_vector[4]),int(single_vector[5]),int(single_vector[6]),int(single_vector[7]),int(single_vector[8])]
        # print(single_vector[8])
        all_vectors.append(single_vector)
    t=Tree(3)

    # t=Recursion(3,8,all_vectors ,t)
    # print ("coordinate",t.root.coordinate)
    # print ("coordinate",t.root.right.coordinate)
    # print ("coordinate",t.root.left.coordinate)
    count1=0
    count2=0
    for i in all_vectors:
        if(i[5]==0 and i[7]==0 and i[8]==1):
            count1+=1
        if(i[5]==0 and i[7]==1 and i[8]==0):
            count1+=1
        if(i[5]==1 and i[7]==0 and i[8]==0):
            count2+=1
        if(i[5]==1 and i[7]==1 and i[8]==1):
            count2+=1
    print(count1)
    print(count2)
        
