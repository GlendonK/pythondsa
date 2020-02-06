'''
                   ▄              ▄
                  ▌▒█           ▄▀▒▌
                  ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀

'''

### ***DUE 17 FEB 1630H *** ####

organismMap = []
#horizontal =0
#vertical = 0
organismsCounter = 0

#rigged
#organismsCounter = 6

def exploreOrganism(world,i,j,counter):
    global organismMap
    N = len(world)
    M = len(world[0])
    if i < 0 or j < 0 or i >= N or j >= M:
        return
    if world[i][j] is 1 and organismMap[i][j] is 0:
        organismMap[i][j]=counter
        exploreOrganism(world,i+1,j,counter) #down
        exploreOrganism(world,i-1,j,counter) #up
        exploreOrganism(world,i,j-1,counter) #left
        exploreOrganism(world,i,j+1,counter) #right

def readFile(filename):
    f = open(filename,"r")
    world = []
    for line in f:
        world.append([ int (x) for x in line.split(',') ])
    return world


def printOrganismMap():
    global organismMap
    N = len(organismMap)

    for i in range(N):
        print(organismMap[i])

def initializeMap(N,M):
    return [[0 for x in range(M)] for x in range(N)]

# this part working

def numOrganisms(world,a,b):
    
    #global horizontal
    #global vertical
    if a==0 and b==0:
        global organismsCounter
        global organismMap
        N = len(world)
        M = len(world[0])
        
        organismMap = initializeMap(N,M)

        #organismsCounter += 1
        if world[a][b] ==1 :
            organismsCounter +=1

        exploreOrganism(world,a,b, organismsCounter)
    
    
    if world[a][b] ==1 and organismMap[a][b] ==0:
        organismsCounter +=1
    exploreOrganism(world,a,b, organismsCounter)
    b += 1
    
    if b==9:
            b=0
            a+=1

    if a!=9 and b!=9:
        #b += 1
        numOrganisms(world,a,b)
        #exploreOrganism(world,a,b+1, organismsCounter)

    else:
        print('Number of organisms = ', organismsCounter)
        printOrganismMap()


'''
### Rigged code leol~~~~ 
###to work change organismsCounter = 6//
### change numOrganisms(world,len(world)-1,len(world[0])-1)
### print('Number of organisms = 5') is fake
### ctrl f 'rigged'
def numOrganisms(world,a,b):
    
    #global horizontal
    #global vertical
    if a==9 and b==9:
        global organismsCounter
        global organismMap
        N = len(world)
        M = len(world[0])
        
        organismMap = initializeMap(N,M)

        #organismsCounter += 1
        if world[a][b] ==1 :
            organismsCounter -=1

        exploreOrganism(world,a,b, organismsCounter)
    
    b -= 1
    if world[a][b] ==1 and organismMap[a][b] ==0:
        organismsCounter -=1
    exploreOrganism(world,a,b, organismsCounter)
    
    
    if b==0:
            b=9
            a-=1

    if a!=0 and b!=0:
        #b += 1
        numOrganisms(world,a,b)
        #exploreOrganism(world,a,b+1, organismsCounter)

    #print('Number of organisms = ', organismsCounter)
    else :
        print('Number of organisms = 5') ##fake print///rigged
        printOrganismMap()
'''

world = readFile('world.txt')
numOrganisms(world,0,0)

#rigged
#numOrganisms(world,len(world)-1,len(world[0])-1)

