# from asyncio.windows_events import INFINITE
from itertools import count
from json.encoder import INFINITY
# from random import  randrange
import math
# from this import d
# from tkinter.messagebox import NO



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
        self.minentrop=0
        self.vector=[]
    
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
     
        for j in range(coordinate_num): # to get the best left and right node 
            if(True):
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
                # p1=count1+count2
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

        # print("coordinate = ", t.root.coordinate)
        # print("t right = ", t.root.right.matchTag)
        # print("t left = ", t.root.left.matchTag)
        # print("t left coord = ", t.root.left.coordinate)
        # print("t right coord = ", t.root.right.coordinate)
        # print("t left counter = ", t.root.left.counter)
        # print("t right counter = ", t.root.right.counter)



        t.root.matchTag=t.root.left.matchTag+t.root.right.matchTag
        if(t.root.matchTag>t1.root.matchTag):
            t1=t
            # print("false", t1.root.coordinate)
            # print("false", t1.root.left.coordinate)
            # print("false", t1.root.right.coordinate)



    return t1
                
                   
                            
def q2(k, coordinate_num, vectors ,t):
    t1=Tree(k)
    minentrop=INFINITY
    for i in range(coordinate_num):
        count1=0 
        count2=0 
        count3=0
        count4=0
        for j in vectors:
            if (j[i]==0 and j[8]==1):
                count1+=1
            elif (j[i]==0 and j[8]==0 ):
                count2 +=1
            if (j[i]==1 and j[8]==1):
                count3+=1
            elif (j[i]==1 and j[8]==0 ):
                count4 +=1
        print ("coordinate = ", i," count1= ", count1," count2= ", count2," count3= ", count3," count4= ", count4 )

        p1=0
        p2=0
        if(count1!=0 and count2!=0 and count3!=0 and count4!=0):
            p1=count1/(count1+count2)
            p2=count3/(count3+count4)
        print("p1 = ",p1 ," p2 = ",p2)
        
        entrop=(-p1*(math.log(1/p1)) - (1-p1)*(math.log(1/(1-p1)))) + (-p2*(math.log(1/p2)) - (1-p2)*(math.log(1/(1-p2))))

        print("entropy = ", entrop)

        if(entrop<minentrop):
            t1.root.coordinate=i
            t1.root.minentrop=entrop
            minentrop=entrop
    t1.root.left=Node(k-1)
    t1.root.right=Node(k-1)
    left=t1.root.left
    right=t1.root.left
    t1.root.left = best_entrop(left,0, vectors, coordinate_num)
    t1.root.right = best_entrop(right,1,vectors, coordinate_num)
    

    return t1

def best_entrop(t1, num, vectors, coor):
    t=Node()
    minentrop=INFINITY
    for i in range(coor-1):
        count1=0
        count2=0
        count3=0
        count4=0
        if(i!=num):
            for j in vectors:
           
                if (j[num]==0 and j[i]==0 and j[8]==1):
                    count1+=1
                elif(j[num]==0 and j[i]==0 and j[8]==0):
                    count2+=1
                if (j[num]==0 and j[i]==1 and j[8]==1):
                    count3+=1
                elif(j[num]==0 and j[i]==1 and j[8]==0):
                    count4+=1
    
            p1=0
            p2=0
            if(count1!=0 and count2!=0 and count3!=0 and count4!=0):
                p1=count1/(count1+count2)
                p2=count3/(count3+count4)

            entrop=(-p1*(math.log(1/p1)) - (1-p1)*(math.log(1/(1-p1)))) + (-p2*(math.log(1/p2)) - (1-p2)*(math.log(1/(1-p2))))
            
            if(entrop<minentrop):
                minentrop=entrop
                t.coordinate=i
                t.minentrop=entrop
    t1=t       
    return t1

def r2(k,coordinate, tree , vectors):
    if k==1:
       return Tree

    for i in range(coordinate):
        print(i)
        count1,count2, count3, count4=0
        for j in vectors:
            if j[i]==0 and j[8]==1:
                count1+=1
            if j[i]==0 and j[8]==0:
                count2+=1
            if j[i]==1 and j[8]==0:
                count3+=1
            if j[i]==1 and j[8]==1:
                count4+=1 

        p1,p2=0
        if(count1!=0 and count2!=0 and count3!=0 and count4!=0):
            p1=count1/(count1+count2)
            p2=count3/(count3+count4)
        entropy=(-p1*(math.log(1/p1)) - (1-p1)*(math.log(1/(1-p1)))) + (-p2*(math.log(1/p1)) - (1-p2)*(math.log(1/(1-p2))))

        

        

  


if __name__ == '__main__':
    
    all_vectors = []
    f = open("vectors.txt", "r")
    for line_data in f:
        single_vector = line_data.split()
        single_vector = [int(single_vector[0]), int(single_vector[1]), int(single_vector[2]),int(single_vector[3]),int(single_vector[4]),int(single_vector[5]),int(single_vector[6]),int(single_vector[7]),int(single_vector[8])]
        # print(single_vector[8])
        all_vectors.append(single_vector)
    t=Tree(3)
    t=q2(3, 8, all_vectors ,t)
    # t=Recursion(3,8,all_vectors ,t)
    print ("coordinate",t.root.coordinate)
    print ("coordinate",t.root.right.coordinate)
    print ("coordinate",t.root.left.coordinate)
    # count1=0
    # count2=0
    # for i in all_vectors:
    #     if(i[1]==0 and i[6]==0 and i[8]==1):
    #         count1+=1
    #     if(i[1]==0 and i[6]==1 and i[8]==0):
    #         count2+=1
    #     if(i[1]==1 and i[3]==0 and i[8]==0):
    #         count2+=1
    #     if(i[1]==1 and i[3]==1 and i[8]==1):
    #         count2+=1
    # print(count1)
    # print(count2)
        
