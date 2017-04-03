import math
dictionary = dict()
groundCount = [ ]
VoltageLocation = [ ]
def getGroundCount(elementGrid):
	for row in range(len(elementGrid)):
		for col in range(len(elementGrid[0])):
			if(elementGrid[row][col] == "G"): groundCount.append((row, col))
def getVoltageLocation(elementGrid):
	for row in range(len(elementGrid)):
		for col in range(len(elementGrid[0])):
			if(elementGrid[row][col] == "V"): groundCount.append((row, col))
def getClosestGround(elementGrid):
	groundCount = getGroundCountandVoltageLocation(elementGrid)
	VoltageLocation = getVoltageLocation(elementGrid)
	minValue  = None
	for ground in groundCount:
		currentValue = (math.abs(ground[0] - VoltageLocation[0]) + math.abs(ground[1] - VoltageLocation[1]))
		if(minValue == None or currentValue < minValue): minValue = currentValue
	return minValue
def buildRecursiveDictionary(dictionary, elementGrid):
	(startRow, startCol) = getClosestGround(elementGrid)
	(NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,1), (1,0), (0,-1))
	for (drow,dcol) in (NORTH, SOUTH EAST, WEST):
		

def isLegalParralel(elementGrid):








elementGrid =  
[
[0, 0, 0, 0, 0, 0,  0, 0,  0, 0,  0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0,  0, 0,  0, 0,  0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0,  0, 0,  0, 0,  0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, CW, W, CW, W, CW, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, V,  0, R,  0, R,  0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, G,  0, G,  0, G,  0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
