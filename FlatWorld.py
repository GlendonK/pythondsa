organismMap = []

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

def numOrganisms(world):
    global organismMap
    N = len(world)
    M = len(world[0])
    organismsCounter = 0
    organismMap = initializeMap(N,M)

    organismsCounter += 1
    exploreOrganism(world,0,0, organismsCounter)

    print('Number of organisms = ', organismsCounter)
    printOrganismMap()

world = readFile('world.txt')
numOrganisms(world)
