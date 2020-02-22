import timeit

# Set Goal Configuration of the puzzle
goal = str(123456780)



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
start =  timeit.timeit()
#ct_node=init_node[:]
#ct_node=np.array(ct_node)
#nodes.append(init_node)
s = [str(i) for i in init_node]
ct_node = str("".join(s))
ct_node = str(ct_node)
nodes.append(ct_node)


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
        return 1
    else:
        return 0

# Function to find the location of Blank(0) tile
def BlankTileLocation(x):

    for i in range(0,len(x)):
            #print(x[i])
            if (x[i]=='0'):
                #print(type(i))
                return i
                break

# Function to Shift Zero to LEFT
def ActionMoveLeft(x):

    b = BlankTileLocation(x)
    #print(b)
    if b==0 or b==3 or b==6:
        return [0,x]
    else:
        a= list(x)
        a[b],a[b-1] = a[b-1],a[b]
        y = ''.join(a)
       # print(y)
        return [1,y]


# Function to Shift Zero to RIGHT
def ActionMoveRight(x):
    #x = l1[:]
    #x = np.array(x)
   # x = x.reshape(3, 3)
    b= BlankTileLocation(x)
    #print(b)
    #temp = []
    if b == 2 or b==5 or b==8:
        return ([0, x])
    else:
        a = list(x)
        a[b], a[b + 1] = a[b + 1], a[b]
        y = ''.join(a)
        #print(y)
        return ([1, y])

# Function to Shift Zero to UP
def ActionMoveUp(x):
    b = BlankTileLocation(x)
   # print(b)
    if b == 0 or b== 1 or b==2:
        return ([0, x])
    else:
        a = list(x)
        a[b], a[b - 3] = a[b - 3], a[b]
        y = ''.join(a)
        #print(y)
        return ([1, y])

# Function to Shift Zero to DOWN
def ActionMoveDown(x):
    b = BlankTileLocation(x)
    #print(b)
    if b == 6 or b==7 or b==8:
        return ([0, x])
    else:
        a = list(x)
        a[b], a[b + 3] = a[b + 3], a[b]
        y = ''.join(a)
        #print('done')
        return ([1, y])

#Function to check if new node exists in the List of all Nodes


# Function to add new node to the node list
def AddNode(newNode,nodes):
    for n in nodes:
        if newNode == n:
            present =1
        else:
            present = 0
    if present==1:
        return 1
    else:
        return (newNode)

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
    while ct_node != goal:
        test = ActionMoveLeft(ct_node)

        if test[0]==1:
            a = AddNode(test[1],nodes)
            if a!=1:
                nodes.append(a)
                c = c + 1
                node_info.append([c,v])
               # a=np.array(a)
               # goal= np.array(goal)


                #If Goal node is found break out of loop
                if a== goal :
                    #print('exit')
                    break


        test = ActionMoveRight(ct_node)

        if test[0] == 1:
            a = AddNode(test[1],nodes)
            if a != 1:
                nodes.append(a)
                c = c + 1
                node_info.append([c, v])
                # a=np.array(a)
                # goal= np.array(goal)

                # If Goal node is found break out of loop
                if a == goal:
                    # print('exit')
                    break

        test = ActionMoveUp(ct_node)
        if test[0] == 1:
            a = AddNode(test[1],nodes)
            if a != 1:
                nodes.append(a)
                c = c + 1
                node_info.append([c, v])
                # a=np.array(a)
                # goal= np.array(goal)

                # If Goal node is found break out of loop
                if a == goal:
                    # print('exit')
                    break

        test = ActionMoveDown(ct_node)
        if test[0] == 1:
            a = AddNode(test[1],nodes)
            if a != 1:
                nodes.append(a)
                c = c + 1
                node_info.append([c, v])
                # a=np.array(a)
                # goal= np.array(goal)

                # If Goal node is found break out of loop
                #print(a)
                if a == goal:
                    print('exit')
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
count = 0
for i in range(0,len(solution)):
    x= solution[i]
    for count in range(0,3):
        for j in range(count,len(x),3):
            var = x[j]
            nodePath.write('%s '%var)
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
for i in range(0,len(nodes)):
    x= nodes[i]
    for count in range(0,3):
        for j in range(count,len(x),3):
            var = x[j]
            n1.write('%s '%var)
    n1.write("\n")
n1.close()
end =  timeit.timeit()

# Calulate time taken to solve
delta = end -start
print(delta)
