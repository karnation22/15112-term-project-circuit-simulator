import math
def getGroundCount(elementGrid, groundCount):
	for row in range(len(elementGrid)):
		for col in range(len(elementGrid[0])):
			if("G" in elementGrid[row][col]): groundCount.append((row, col))
	return groundCount
def getVoltageLocation(elementGrid):
	for row in range(len(elementGrid)):
		for col in range(len(elementGrid[0])):
			if(elementGrid[row][col] == "V"): voltageLocation.append((row, col))
	return voltageLocation
def getClosestGround(elementGrid):
	groundCount = getGroundCountandVoltageLocation(elementGrid)
	VoltageLocation = getVoltageLocation(elementGrid)
	minGround  = None
	minValue = None
	for ground in groundCount:
		currentValue = (math.abs(ground[0] - VoltageLocation[0]) + math.abs(ground[1] - VoltageLocation[1]) )
		currentGround = ground
		if(minValue == None or currentValue < minValue): 
			minValue = currentValue
			minGround = ground
	#(data.startRow, data.startCol) = minGround 
	return minGround #returns a tuple of row and col
def isLegalAdvanced(elementGrid, booleanGrid):
	copyboolean = copy.deepcopy(booleanGrid)
	groundCount = getGroundCount(elementGrid)
	if(groundCount < 3): return False
	(startRow, startCol) = getClosestGround(elementGrid)
	(NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,-1), (1,0), (0,1))
	for (drow, dcol) in (NORTH, SOUTH, EAST, WEST):
		if elementGrid[startRow+drow][startCol+dcol] != 0 and copyboolean[startRow+drow][startCol+dcol]:
			copyboolean[startRow][startCol] = False
			

def getNodeCount(elementGrid, startRow, startCol):
	(NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,-1), (1,0), (0,1))
	count = 0
	for (drow, dcol) in (NORTH, WEST, SOUTH, EAST):
		if(elementGrid[startRow+drow][startCol+dcol] != 0): count +=1
	return count

def buildRecursiveDictionary(dictionary, elementGrid, booleanGrid, startRow=5, startCol=5, layer=0):
	if(layer > 0 and "G" in elementGrid[startRow][startCol]): return elementGrid[startRow][startCol]
	else: 
		(NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,-1), (1,0), (0,1))
		for (drow, dcol) in (NORTH, WEST, SOUTH, EAST):
			if(elementGrid[startRow+drow][startCol+dcol] != 0 and booleanGrid[startRow+drow][startCol+dcol]):
				booleanGrid[startRow][startCol] = False
				nodeCount = getNodeCount(elementGrid, startRow, startCol)
				curElem = elementGrid[startRow][startCol]
				if(nodeCount > 2): #go two directions instead of one
					dictionary[curElem] = [dict(), dict()] 
 					dictionary[curElem][0] = buildRecursiveDictionary(dictionary[curElem][0], elementGrid, 
						booleanGrid, startRow+1, startCol, layer+1)
					dictionary[curElem][1] = buildRecursiveDictionary(dictionary[curElem][1], elementGrid, 
						booleanGrid, startRow, startCol+1, layer+1)
					if(dictionary != None): return dictionary
				else:
					dictionary[curElem] = dict()
					dictionary[curElem] = buildRecursiveDictionary(dictionary[curElem], elementGrid, 
						booleanGrid, startRow+drow, startCol+dcol, layer+1)
					if(dictionary != None): return dictionary


dictionary = dict()
groundCount = [ ]
voltageLocation = [ ]
elementGrid = [
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,    0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,    0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,    0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0,"CW","W1","CW1","W2", "CW2",  0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0,"V",  0,  "R2",   0,   "R4",  0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0,"G1", 0,  "R3",   0,   "G3",  0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,  "G2",   0,    0,    0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,    0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,    0,      0,     0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,    0,      0,     0, 0, 0]]

elementGrid2 = [
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0,"CW", 0, "CW1",   0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0,"V",  0,  "R2",   0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0,"G1", 0,  "G2",   0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,   0,   0,   0, 0, 0], 
[0, 0, 0, 0, 0, 0,   0,   0,     0,    0,   0,   0,   0, 0, 0]]

booleanGrid = [
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, True,  True,  True,  True,  True,   True,  True, False, False, False], 
[False, False, False, False, False, True,  False, True,  False, True,  False,  True, False, False, False], 
[False, False, False, False, False, True,  False, True,  False, True,  False,  True, False, False, False], 
[False, False, False, False, False, False, False, True,  False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]


print(buildRecursiveDictionary(dictionary, elementGrid, booleanGrid))