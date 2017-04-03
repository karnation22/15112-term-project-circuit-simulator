def solveCircuit(data, booleandata):	
	NineCount = 0 
	#Check to see for one 9 - determine ground starting point
	for row in range(len(data)):
		for col in range(len(data[0])):
			if data[row][col] == 9: 
				NineCount +=1
				(startRow, startCol) = (row, col)

	if(NineCount == 2):
		def AllNonZero(data):
			nonZeroCount = 1
			for row in range(len(data)):
				for col in range(len(data[0])):
					if(data[row][col] != 0): nonZeroCount += 1
			return nonZeroCount

		def loopCircuit(data, booleandata, startRow, startCol):
			finalList=[]
			(NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,1), (1,0), (0,-1))
			nonZeroCount = AllNonZero(data)
			for element in range(nonZeroCount):
				for (drow, dcol) in (NORTH, EAST, SOUTH, WEST):
					if(data[startRow+drow][startCol+dcol] != 0 and booleandata[startRow+drow][startCol+dcol]):
						finalList.append(data[startRow][startCol])
						booleandata[startRow+drow][startCol+dcol] = False
						startRow += drow
						startCol += dcol
						break
				if(element == nonZeroCount-1): 
					print("I made it here")
					print (data[startRow][startCol] == 9)

			return finalList
		finalList = loopCircuit(data, booleandata, startRow, startCol)
	return finalList
		#9,8,6,8,8,8,8,8,1,8,8, "Completed"
	

booleandata = [
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, True, True, True, False, False, False, False, False, False], 
[False, False, False, False, False, False, True, False, True, False, False, False, False, False, False], 
[False, False, False, False, False, False, True, False, True, False, False, False, False, False], 
[False, False, False, False, False, False, True, False, True, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
]

data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 6, 0, 1, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


print(solveCircuit(data, booleandata))

