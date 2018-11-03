#Exercise 1
def average_above_zero(tab):
    """
    brief: computes the average of the positives values 
    Args:
        tab: a list of numeric values
    Return:
        the compiled average
    Raises:
        ValueError if no positive value is found
        ValueError if input tab is not a list
    """

    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
        
    average=-99
    valSum=0.0
    nPositiveValues=0
    
    for val in tab:
        if val>0:
            valSum=valSum+float(val)
            nPositiveValues=nPositiveValues+1

    if nPositiveValues<=0:
        raise ValueError('no positive value found')
    average=valSum/nPositiveValues
    return float(average)

#Test exercise 1
test_tab=[1,2,3,-5]
moy=average_above_zero(test_tab)
print('The average of positive values average = {v}'.format(v=moy))


#Exercise 2
def max_value(tab):
    """
    brief: give max number of a list
    Args:
        tab: a list of numeric values
    Return:
        the max number
        the index max number
    Raises:
        ValueError if tab is not a list
        ValueError if tab is empty
    """

    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
        
    if len(tab)==0:
        raise ValueError('provided list is empty')
        
    maxVal=-99
    idx=-11
    NMAX=len(tab)
    
    for index in range(0,NMAX):
        if tab[index] > maxVal:
            maxVal=tab[index]
            idx=index
            
    return maxVal,idx

#Test exercise 2
test_tab=[1,2,3,-5]
maxValue=max_value(test_tab)
print('The maximum value = {v} and his index is = {b}'.format(v=maxValue[0],b=maxValue[1] ))

#Exercise 3
import numpy as np
def reverseTable(tab):
    """
    brief: reverse a tab
    Args:
        tab: a list of numeric values
    Return:
        the reversed tab
    Raises:
        ValueError if input tab is not a list
    """

    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    
    lengthTab = len(tab)
    loopMaxID = int(np.floor(lengthTab)/2)
    lengthTab-=1
    for idx in range(loopMaxID):
        element = tab[lengthTab - idx]
        tab[lengthTab-idx]=tab[idx]
        tab[idx]=element
    return tab

#Test exercise 3
print('The table is : '+str(test_tab))
reversedTable=reverseTable(test_tab)
print('The reversed table is : '+str(reversedTable))

#Exercise 4 bounding Box
def roi_bbox(inputMat):

    if not(isinstance(inputMat, np.ndarray)):
        raise ValueError('Expected a list as input')
        
    if not(inputMat.dtype == np.bool):
        raise ValueError('Expected input of type numpy.bool')
        
    lmin=inputMat.shape[0]
    lmax=0
    cmin=inputMat.shape[1]
    cmax=0   
    
    for l in range(inputMat.shape[0]):
        for c in range(inputMat.shape[1]):
            if inputMat[l,c]==True:
                if l<lmin:
                    lmin=l
                if l>lmax:
                    lmax=l
                if c<cmin:
                    cmin=c
                if c>cmax:
                    cmax=c
    
    roi=[
        [lmin, cmin],
        [lmin, cmax],
        [lmax, cmin],
        [lmax,cmax]
        ]
        
    return np.array(roi)
    
#Test exercise 4
inputMat=np.zeros((5,6),dtype=np.bool)

inputMat[2,3] = True
inputMat[2,4] = True
inputMat[3,3] = True
inputMat[3,4] = True

inputMat[2:4,3:5]=np.ones((2,2),dtype=np.bool)

print("inputMat : " + str(inputMat))
roi = roi_bbox(inputMat)
print('roi : ' + str(roi))

#Exercise 5 random array filling
def random_array_filling(matrix,cellNumberToBeFilled):
    line = 0
    count = 0
    column = 0
    if cellNumberToBeFilled>matrix.size:
         raise ValueError('cellNumberToBeFilled is bigger than the matrix size')
    if matrix.dtype!="<U1":
         raise ValueError('Wrong array type')
    while count < cellNumberToBeFilled:
        column=random.randrange(0,len(matrix[0])-1)
        line=random.randrange(0,len(matrix)-1)
        if matrix[line][column]!="." :
            matrix[line][column]="."
            count+=1
            
    return matrix

#Test exercise 5
matrix=np.array([["","","","","",""],["","","","","",""]])
matrix=np.array([[0,0,0,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0]])
testLen = len(matrix)
randomX=random_array_filling(matrix,4)
print(randomX)

#Exercise 6 remove whitespace in string
def remove_whitespaces(p_string):
    count = 0
    while count<len(p_string):
        if(p_string[count] == " "):
            p_string = p_string[0:count]+p_string[count+1:len(p_string)-1] 
        count = count + 1
    return p_string

#Test exercise 6
print(remove_whitespace("This is my      string test                 1"))

#Exercise 7 Random item selection

#Exercise 8 launch_dice
import random
def launch_dice():
    score = 0
    while True:
        diceTry = random.randint(1,6)
        score+= diceTry
        print("Dés lancé par l'ordinateur : "+str(diceTry))
        
        if diceTry == 1:
            score = 0
            break
        
        roll = input('Relancé le dé ? o/n')
        if roll == 'n':
            break
        
    print("Le score obtenue est de : " + str(score))
    return "a"

#launch_dice()




"""

    #init max_value and its index
    max_val=input_list[0]
    max_idx=0
    #compute the average of positive elements of a list
for item in input_list:
        #select only positive items
        if max_val<item:
            max_val=item

    #generic style : iterate over the range of list indexes
    for idx in range(len(input_list)):
        #select only positive items
        if max_val<input_list[idx]:
            max_val=input_list[idx]
            max_idx=idx


    #generic style : iterate over the range of list indexes
    for idx, item in enumerate(input_list):
        #select only positive items
        if max_val<item:
            max_val=item
            max_idx=idx

    return max_val, max_idx



#test max_value function
#1 basic test, expected answer=2
mylist=[-1,2,-20]
mymax, mymaxidx=max_value(mylist)
mymax_tuple=max_value(mylist)
mymax=mymax_tuple[0]
print('Max value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
#==> message : "Max value of [-1, 2, -20] is (2, 1)"

#2 error test : Exception expected
max_value([])
"""

"""
# hints to solve the roi_bbox function exercise: numpy basics

#matrix processing lib
import numpy

#create a numpy matrix with specific dimensions
size_rows=10
size_cols=10
myMat=numpy.zeros([size_rows, size_cols], dtype=int)
#set a value in a specific cell
myMat[1,3]=1

#fil something in the matrix, the basic way (a very slow python way...)
for row in range(5,8):
    for col in range(7,9):
        myMat[row,col]=1

#get time to measure processing speed
import time
init_time=time.time()

#filling something in the matrix, a nicer way
myMat[2:4,5:9]=1 #assign a scalar to each cell of a subarray
myMat[4:7,7:9]=numpy.ones([3,2]) #copy an array in a subarray
print(myMat)

#get ellapsed time
filling_time=time.time() -init_time
print('data prefecting time='+str(filling_time))

#fake bounding box coordinates matrix
xmin=0
xmax=100
ymin=0
ymax=200
#how to fill the 4x2 bbox coordinates matrix, method 1 using 1D numpy arrays (ugly?)
bbox_coords=numpy.zeros([4, 2], dtype=int)
bbox_coords[0,:]=numpy.array([ymin, xmin])
bbox_coords[1,:]=numpy.array([ymin, xmax])
bbox_coords[2,:]=numpy.array([ymax, xmin])
bbox_coords[3,:]=numpy.array([ymax, xmax])
#how to fill the 4x2 bbox coordinates matrix, method 2 using lists (shorter way)
#->create a list of lists
coordsList=[[ymin, xmin],[ymin, xmax],[ymax, xmin],[ymax, xmax]]
#->convert to an array
coords_array=numpy.array(coordsList)
"""



















