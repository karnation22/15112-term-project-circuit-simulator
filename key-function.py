def solveCircuit(data):##THIS IS THE MEAT####### 
    def getGroundCount(data):
        #Check to see for one ground - determine ground starting point
        for row in range(len(data.elementGrid)):
            for col in range(len(data.elementGrid[0])):
                if type(data.elementGrid[row][col]) == Ground: 
                    data.GroundCount +=1
                    (data.startRow, data.startCol) = (row, col)
    def AllNonZero(data):
        nonZeroCount = 1
        for row in range(len(data.elementGrid)):
            for col in range(len(data.elementGrid[0])):
                if(data.elementGrid[row][col] != 0): nonZeroCount += 1
        return nonZeroCount
    def isLegalCircuitSeries(data):
        #Next, check for a complete connection
        (NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,1), (1,0), (0,-1))
        nonZeroCount = AllNonZero(data)
        copyboolean = copy.deepcopy(data.booleanGrid)
        #we start at a ground
        for element in range(nonZeroCount-1):
            conditionalPenetration = 0
            for (drow, dcol) in (NORTH, WEST, SOUTH, EAST):
                #makes sure we don't go back in line
                if(data.elementGrid[data.startRow+drow][data.startCol+dcol] != 0 and 
                    copyboolean[data.startRow+drow][data.startCol+dcol]):
                    conditionalPenetration += 1
                    copyboolean[data.startRow+drow][data.startCol+dcol] = False
                    data.startRow += drow
                    data.startCol += dcol
                    break
            #Check to see if last element is ground
            if(element == nonZeroCount-2): 
                if (type(data.elementGrid[data.startRow][data.startCol]) != Ground): return False
            #check to see if every element aside from this is connected to another element
            elif(conditionalPenetration != 1): return False
        return True

        #ONLY FOR SERIES CIRCUITS!!
    def determineVoltageandCurrentSeries(data):
        if(isLegalCircuitSeries(data) and len(data.acVoltage) == 0 and len(data.acCurrent) == 0):
            data.isLegalCircuit = True
            if(len(data.dcVoltage) > 0 and len(data.dcCurrent) == 0):
                totalVoltageSupply = 0
                for dcVoltage in data.dcVoltage:
                    totalVoltageSupply += dcVoltage.voltage
                #All resistors are here
                if(len(data.resistors) > 0 and len(data.capacitors) == 0 and len(data.inductors) == 0):
                    totalResistance = 0
                    for resistor in data.resistors:
                        totalResistance += resistor.resistance
                    totalCurrent = totalVoltageSupply/totalResistance #Ohm's Law
                    for resistor in data.resistors:
                        (resistor.i0, resistor.i8) = (0.01*int(100*totalCurrent), 0.01*int(100*totalCurrent))
                        (resistor.v0, resistor.v8) = (0.01*int(100*totalCurrent*resistor.resistance),
                                                      0.01*int(100*totalCurrent*resistor.resistance))
                    for dcVoltage in data.dcVoltage:
                        (dcVoltage.i0, dcVoltage.i8) = (totalCurrent, totalCurrent)
                #All capacitors and resistors
                elif(len(data.resistors) > 0 and len(data.capacitors) > 0 and len(data.inductors)==0):
                    totalResistance = 0
                    (totalCapacitanceNumerator, totalCapacitanceDenomator) = (1, 0)
                    for resistor in data.resistors:
                        totalResistance += resistor.resistance
                    totalCurrent = totalVoltageSupply/totalResistance #Ohm's Law 
                    for capacitor in data.capacitors:
                        if(len(data.capacitors) == 1): totalCapacitance = capacitor.capacitance
                        else:
                            totalCapacitanceNumerator *= capacitor.capacitance
                            totalCapacitanceDenomator += capacitor.capacitance
                            totalCapacitance = totalCapacitanceNumerator/totalCapacitanceDenomator
                    totalCharge = totalVoltageSupply*totalCapacitance
                    for resistor in data.resistors:
                        (resistor.i0, resistor.i8) = (0.01*int(100*totalCurrent), 0.00)
                        (resistor.v0, resistor.v8) = (0.01*int(100*totalCurrent*resistor.resistance), 0.00)
                    for capacitor in data.capacitors:
                        (capacitor.i0, capacitor.i8) = (0.01*int(100*totalCurrent), 0.00)
                        (capacitor.v0, capacitor.v8) = (0.00, 0.01*int(100*totalCharge/capacitor.capacitance))
                    for dcVoltage in data.dcVoltage:
                        (dcVoltage.i0, dcVoltage.i8) = (totalCurrent, 0.00)
                #All resistors and inductors
                elif(len(data.resistors) > 0 and len(data.capacitors) == 0 and len(data.inductors) > 0):
                    totalResistance = 0
                    totalInductance = 0
                    for resistor in data.resistors:
                        totalResistance += resistor.resistance
                    totalCurrent = totalVoltageSupply/totalResistance #Ohm's Law
                    for inductor in data.inductors:
                        totalInductance += inductor.inductance
                    for resistor in data.resistors:
                        (resistor.i0, resistor.i8) = (0.00, 0.01*int(100*totalCurrent))
                        (resistor.v0, resistor.v8) = (0.00, 0.01*int(100*totalCurrent*resistor.resistance))
                    for inductor in data.inductors:
                        (inductor.i0, inductor.i8) = (0.00, 0.01*int(100*totalCurrent))
                        (inductor.v0, inductor.v8) = (0.01*int(100*totalVoltageSupply*inductor.inductance/totalInductance), 0.00)
                    for dcVoltage in data.dcVoltage:
                        (dcVoltage.i0, dcVoltage.i8) = (0.00, totalCurrent)
            elif(len(data.dcCurrent) > 0 and len(data.dcVoltage) == 0): 
                totalCurrent = 0
                for dcCurrent in data.dcCurrent:
                    totalCurrent += dcCurrent.current
                #All resistors are here
                if(len(data.resistors) > 0 and len(data.capacitors) == 0 and len(data.inductors) == 0):
                    totalResistance = 0
                    for resistor in data.resistors:
                        totalResistance += resistor.resistance
                    totalVoltage = totalCurrent*totalResistance #Ohm's Law
                    for resistor in data.resistors:
                        (resistor.i0, resistor.i8) = (0.01*int(100*totalCurrent), 0.01*int(100*totalCurrent))
                        (resistor.v0, resistor.v8) = (0.01*int(100*totalCurrent*resistor.resistance),
                                                      0.01*int(100*totalCurrent*resistor.resistance))
                    for dcCurrent in data.dcCurrent:
                        (dcCurrent.v0, dcCurrent.v8) = (-totalResistance*totalCurrent, -totalResistance*totalCurrent)
        else: data.isLegalCircuit = False

    getGroundCount(data)
    if(data.GroundCount == 2): determineVoltageandCurrentSeries(data)
