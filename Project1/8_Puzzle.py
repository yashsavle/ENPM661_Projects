import numpy as np

# Set Goal Configuration of the puzzle
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#goal = np.array(goal)
#goal = goal.reshape(3, 3)


#defining lists to be used in the calculations
init_node= []
nodes = []
node_info = []
node_info.append([0,0])
c= 0
solu=[]
#Input initial State of the puzzle
print("Enter Initial Node")
for i in range(9):
    n= input()
    init_node.append(int(n))
ct_node=init_node[:]
#ct_node=np.array(ct_node)
nodes.append(ct_node)
#print(ct_node)


#Function to check if the Solution Exists
def check_sol(l1):
    x= l1[:]
    x.remove(0)
    count = 0
    for i in range(0,len(x)):

        for j in range(i,len(x)):
            if(x[j]<x[i]):
                count = count + 1
    if(count%2==0):
        print('This case is Solvable')
        print('Please wait, the solution is being formulated')
        return(1)
    else:
        return (0)

# Function to find the location of Blank(0) tile
def BlankTileLocation(l1):
    x = l1[:]
    x=np.array(x)
    x= x.reshape(3,3)

    for i in range(0,3):
        for j in range(0,3):
            if (x[i, j]==0):
                return([i,j])

# Function to Shift Zero to LEFT
def ActionMoveLeft(x):
    #x = l1[:]
    x = np.array(x)
   # print(x)
    x = x.reshape(3, 3)
    [a,b] = BlankTileLocation(x)
    temp =[]
    if b==0:
        return ([0,x])
    else:
        temp =x[a,b-1]
        x[a,b-1]= x[a,b]
        x[a,b]= temp
        #print(x)
        return([1,x])


# Function to Shift Zero to RIGHT
def ActionMoveRight(x):
    #x = l1[:]
    x = np.array(x)
    x = x.reshape(3, 3)
    [a, b] = BlankTileLocation(x)
    temp = []
    if b == 2:
        return ([0, x])
    else:
        temp = x[a, b + 1]
        x[a, b + 1] = x[a, b]
        x[a, b] = temp
        return ([1, x])

# Function to Shift Zero to UP
def ActionMoveUp(x):
   # x = l1[:]
    x = np.array(x)
    x = x.reshape(3, 3)
    [a, b] = BlankTileLocation(x)
    temp = []
    if a == 0:
        return ([0, x])
    else:
        temp = x[a-1, b]
        x[a-1, b ] = x[a, b]
        x[a, b] = temp
        return ([1, x])

# Function to Shift Zero to DOWN
def ActionMoveDown(x):
    #x = l1[:]
    x = np.array(x)
    x = x.reshape(3, 3)
    [a, b] = BlankTileLocation(x)
    temp = []
    if a == 2:
        return ([0, x])
    else:
        temp = x[a+1, b ]
        x[a+1, b ] = x[a, b]
        x[a, b] = temp
        return ([1, x])

#Function to check if new node exists in the List of all Nodes
def exist(n1,n2):
    for n in range(0,len(n2)):
        n1= np.reshape(n1,(1,9))
        #print(n1)
       # print(n2[n])
        if np.array_equal(n1[0],n2[n]):
            return 1

        return 0


# Function to add new node to the node list
def AddNode(newNode):

    present = exist(newNode,nodes)
    if present==1:
        return [present]
    else:
        newNode= newNode.reshape(1,9)
        newNode= newNode.tolist()

        return [newNode]

# Function to Retrace the node Tree to obtain the solution
def generate_path(nodes,node_info):
    #rev = node_info.reverse()
    #print(rev)
   # print(nodes)
    add = node_info[-1]
    #print(add)
    dest =  node_info[0]
    #print(dest)
    while add != dest:
        #add=index[0]
        #print(nodes[add[0]])
        solu.append(nodes[add[0]])
        add = node_info[add[1]]
    solu.append(nodes[add[0]])
    return solu

# MAIN
#Check whether Solution Exists
chk= check_sol(init_node)
if chk==1:
    v=0
#for v in range(0,len(nodes)):
    #print(ct_node)

    #Sequence to Generate new nodes by combinations of Left, Right, Up, Down
    while (np.array_equal(ct_node,goal)== False):
        test = ActionMoveLeft(ct_node)
        if test[0]==1:
            [a] = AddNode(test[1])
            if a!=1:

                nodes.append(a[0])
                c = c + 1
                node_info.append([c,v])
               # a=np.array(a)
                goal= np.array(goal)

                #If Goal node is found break out of loop
                if np.array_equal(a[0],goal)== True:
                    #print('exit')
                    break


        test = ActionMoveRight(ct_node)
        if test[0] == 1:
            [a] = AddNode(test[1])
            if a != 1:

                nodes.append(a[0])
                c = c + 1
                node_info.append([c, v])
                # a=np.array(a)
                goal = np.array(goal)

                # If Goal node is found break out of loop
                if np.array_equal(a[0], goal) == True:
                    #print('exit')
                    break

        test = ActionMoveUp(ct_node)
        if test[0] == 1:
            [a] = AddNode(test[1])
            if a != 1:

                nodes.append(a[0])
                c = c + 1
                node_info.append([c, v])
                # a=np.array(a)
                goal = np.array(goal)

                # If Goal node is found break out of loop
                if np.array_equal(a[0], goal) == True:
                    #print('exit')
                    break

        test = ActionMoveDown(ct_node)
        if test[0] == 1:
            [a] = AddNode(test[1])
            if a != 1:

                nodes.append(a[0])
                c = c + 1
                node_info.append([c, v])
                # a=np.array(a)
                goal = np.array(goal)

                # If Goal node is found break out of loop
                if np.array_equal(a[0], goal) == True:
                    #print('exit')
                    break

        v=v+1
        ct_node = nodes[v]
    print('Solution Found')

else:
    print('This case is Unsolvable')


#print(nodes)
#print(node_info)

# Call Function to Generate Solution
solution = generate_path(nodes,node_info)
solution.reverse()
print(solution)
#ans= check_sol(init_node)
#print(ans)
#loc= BlankTileLocation(init_node)
#print(loc)

# Write Solution in Text File
nodePath= open('nodePath.txt','w')
for i in solution:
    for j in i:
        nodePath.write('%s '%j)
    nodePath.write("\n")
nodePath.close()

# Write Information about node number and Parent node in text file
NodesInfo= open('NodesInfo.txt', 'w')
for i in node_info:
    for j in i:
        NodesInfo.write('%s '%j)
    NodesInfo.write("\n")
NodesInfo.close()

# Write All explored nodes in Text file
n1= open('Nodes.txt','w')
for i in nodes:
    for j in i:
        n1.write('%s '%j)
    n1.write("\n")
n1.close()

