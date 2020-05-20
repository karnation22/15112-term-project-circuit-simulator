# mousePressed, mouseMoved, mouseReleased
# with left or right button
# and with ctrl and shift
from __future__ import print_function, division
from Tkinter import *
from classes import *
from drawFunctions import *
import math
import copy
import numpy as np
import matplotlib.pyplot as plt 

def eventInfo(eventName, x, y, ctrl, shift):
    msg = ""
    if ctrl:  msg += "ctrl-"
    if shift: msg += "shift-"
    msg += eventName
    msg += " at " + str((x,y))
    return msg
def mouseMotion(event, data):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    canvas.data["info"] = eventInfo("mouseMotion", event.x, event.y, ctrl, shift)
    canvas.data["motionPosn"] = (event.x, event.y)

    for resistor in data.resistors:
        (topx, topy, bottomx, bottomy) = resistor.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): resistor.rotaterdeleter = True
        else: resistor.rotaterdeleter = False
    for capacitor in data.capacitors:
        (topx, topy, bottomx, bottomy) = capacitor.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): capacitor.rotaterdeleter = True
        else: capacitor.rotaterdeleter = False

    for inductor in data.inductors:
        (topx, topy, bottomx, bottomy) = inductor.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): inductor.rotaterdeleter = True
        else: inductor.rotaterdeleter = False

    for acVoltage in data.acVoltage:
        (topx, topy, bottomx, bottomy) = acVoltage.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): acVoltage.rotaterdeleter = True
        else: acVoltage.rotaterdeleter = False

    for acCurrent in data.acCurrent:
        (topx, topy, bottomx, bottomy) = acCurrent.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): acCurrent.rotaterdeleter = True
        else: acCurrent.rotaterdeleter = False

    for dcCurrent in data.dcCurrent:
        (topx, topy, bottomx, bottomy) = dcCurrent.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): dcCurrent.rotaterdeleter = True
        else: dcCurrent.rotaterdeleter = False

    for dcVoltage in data.dcVoltage:
        (topx, topy, bottomx, bottomy) = dcVoltage.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): dcVoltage.rotaterdeleter = True
        else: dcVoltage.rotaterdeleter = False

    for wire in data.wires:
        (topx, topy, bottomx, bottomy) = wire.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): wire.rotaterdeleter = True
        else: wire.rotaterdeleter = False

    for cornerwire in data.cornerWires:
        (topx, topy, bottomx, bottomy) = cornerwire.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): cornerwire.rotaterdeleter = True
        else: cornerwire.rotaterdeleter = False

    for ground in data.ground:
        (topx, topy, bottomx, bottomy) = ground.getCorners() #will inherit from element class
        if(topx < event.x < bottomx and topy < event.y < bottomy): ground.rotaterdeleter = True
        else: ground.rotaterdeleter = False

    redrawAll(canvas, data)
def keyPressed(event, data): 
    #Now I can press keys as well (rotate and delete keys)
    #If we are within range, we are good
    if(event.keysym == "q"): data.restart = True
    if(event.keysym == "r"): 
        for resistor in data.resistors: 
            if(resistor.rotaterdeleter): resistor.isVertical = not resistor.isVertical
        for capacitor in data.capacitors: 
            if(capacitor.rotaterdeleter): capacitor.isVertical = not capacitor.isVertical
        for inductor in data.inductors:
            if(inductor.rotaterdeleter): inductor.isVertical = not inductor.isVertical
        for cornerWire in data.cornerWires:
            if(cornerWire.rotaterdeleter):
                if(not cornerWire.top and not cornerWire.left): cornerWire.top = True
                elif(cornerWire.top and not cornerWire.left): (cornerWire.top , cornerWire.left) = (False, True)
                elif(not cornerWire.top and cornerWire.left): cornerWire.top = True
                else: (cornerWire.top, cornerWire.left) = (False, False)
        for wire in data.wires:
            if(wire.rotaterdeleter): wire.isVertical = not wire.isVertical
    if(event.keysym == "d"): 
        #if we are true here
        topx = ((event.x + 15)//30 - 1)*30
        topy = ((event.y + 15)//30 - 1)*30
        for resistor in data.resistors: 
            if(resistor.rotaterdeleter): 
                data.resistors.remove(resistor)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for capacitor in data.capacitors: 
            if(capacitor.rotaterdeleter): 
                data.capacitors.remove(capacitor)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False 
        for inductor in data.inductors: 
            if(inductor.rotaterdeleter): 
                data.inductors.remove(inductor)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for acVoltage in data.acVoltage: 
            if(acVoltage.rotaterdeleter): 
                data.acVoltage.remove(acVoltage)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for acCurrent in data.acCurrent: 
            if(acCurrent.rotaterdeleter): 
                data.acCurrent.remove(acCurrent)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for dcVoltage in data.dcVoltage: 
            if(dcVoltage.rotaterdeleter): 
                data.dcVoltage.remove(dcVoltage)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for dcCurrent in data.dcCurrent: 
            if(dcCurrent.rotaterdeleter): 
                data.dcCurrent.remove(dcCurrent)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for wire in data.wires: 
            if(wire.rotaterdeleter): 
                data.wires.remove(wire)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for cornerwire in data.cornerWires: 
            if(cornerwire.rotaterdeleter): 
                data.cornerWires.remove(cornerwire)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
        for ground in data.ground: 
            if(ground.rotaterdeleter): 
                data.ground.remove(ground)
                data.elementGrid[topy//60][topx//60] = 0
                data.booleanGrid[topy//60][topx//60] = False
    if(event.keysym == "s"):
        for dcVoltage in data.dcVoltage:
            if(dcVoltage.rotaterdeleter):
                (i0,i8,v0,v8) = dcVoltage.getvi()
                finTuple = ((0,i0),(1,i8),(2,v0), (3,v8))
                for (key,value) in finTuple:
                    data.displayValues[key] = value
        for dcCurrent in data.dcCurrent:
            if(dcCurrent.rotaterdeleter):
                (i0,i8,v0,v8) = dcCurrent.getvi()
                finTuple = ((0,i0),(1,i8),(2,v0), (3,v8))
                for (key,value) in finTuple:
                    data.displayValues[key] = value
        for resistor in data.resistors:
            if(resistor.rotaterdeleter): 
                (i0,i8,v0,v8) = resistor.getvi()
                finTuple = ((0,i0),(1,i8),(2,v0), (3,v8))
                for (key,value) in finTuple:
                    data.displayValues[key] = value
        for capacitor in data.capacitors: 
            if(capacitor.rotaterdeleter): 
                (i0,i8,v0,v8) = capacitor.getvi()
                finTuple = ((0,i0),(1,i8),(2,v0),(3,v8))
                for (key, value) in finTuple:
                    data.displayValues[key] = value
        for inductor in data.inductors:
            if(inductor.rotaterdeleter):
                (i0,i8,v0,v8) = inductor.getvi()
                finTuple = ((0,i0),(1,i8),(2,v0), (3,v8))
                for (key, value) in finTuple:
                    data.displayValues[key] = value
    if(event.keysym == "t"):
        elementlist = [data.resistors, data.inductors, data.capacitors]
        if(data.transientAnalysis and data.isLegalCircuit):
            for elementtype in elementlist:
                for element in elementtype:
                    if(element.rotaterdeleter == True):
                        performTransientAnalysis(element, data)
    if(event.keysym == "i"): data.helpScreen = not data.helpScreen
def rightMousePressed(event, data):
 #Normal Mouse Press (but darn, it is right click)
    #RLC Elements
    if(60 < event.y < 120):
        if(30 < event.x < 90):
            data.resistorSelect = True
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = False

        elif(90 < event.x < 150):
            data.resistorSelect = False
            data.capacitorSelect = True
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = False

        elif(150 < event.x < 210):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = True
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = False
       
        #AC Elements
    elif(150 < event.y < 210):
        if(30 < event.x < 90):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = True
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = False

        elif(90 < event.x < 150):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = True
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = False

        #DC Elements
    elif(240 < event.y < 300):
        if(30 < event.x < 90):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = True
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = False

        elif(90 < event.x < 150):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = True
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = False

        #Ground n Wire n corner wire
    elif (330 < event.y < 390):
        if(30 < event.x < 90):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = True
            data.cornerWireSelect = False
            data.groundSelect = False

        elif(90 < event.x < 150):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = False
            data.groundSelect = True

        elif(150 < event.x < 210):
            data.resistorSelect = False
            data.capacitorSelect = False
            data.inductorSelect = False
            data.acVoltageSelect = False
            data.acCurrentSelect = False
            data.dcVoltageSelect = False
            data.dcCurrentSelect = False
            data.wireSelect = False
            data.cornerWireSelect = True
            data.groundSelect = False
def leftMousePressed(event, data): 
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    canvas.data["info"] = eventInfo("leftMousePressed", event.x, event.y, ctrl, shift)
    canvas.data["leftPosn"] = (event.x, event.y)
    #Checks to see if our leftMousePressed was on a red-selected box
    topx = ((event.x + 15)//30 - 1)*30
    topy = ((event.y + 15)//30 - 1)*30
    datax = topx//60
    datay = topy//60
    if(topx//30 % 2 == 0 and topy//30 % 2 == 0 and event.x > 240 
        and (data.elementGrid[datay][datax] == 0 or (data.cornerWireSelect and 
        type(data.elementGrid[datay][datax]) == CornerWire))):
        if(data.resistorSelect): data.resistors.append(Resistor(topx, topy, False, False))
        elif(data.capacitorSelect): data.capacitors.append(Capacitor(topx, topy, False, False)) 
        elif(data.inductorSelect): data.inductors.append(Inductor(topx, topy, False, False))
        elif(data.acVoltageSelect): data.acVoltage.append(ACVoltageSource(topx, topy, False))
        elif(data.acCurrentSelect): data.acCurrent.append(ACCurrentSource(topx, topy, False))
        elif(data.dcVoltageSelect): data.dcVoltage.append(DCVoltageSource(topx, topy, False))
        elif(data.dcCurrentSelect): data.dcCurrent.append(DCCurrentSource(topx, topy, False))
        elif(data.wireSelect): data.wires.append(Wire(topx, topy, False, False))
        elif(data.cornerWireSelect): data.cornerWires.append(CornerWire(topx, topy, False, False, False))
        elif(data.groundSelect): data.ground.append(Ground(topx, topy, False))

    elif(60 < event.x < 180 and 420 < event.y < 480):
        solveCircuit(data)
        data.flashSimulate = True
    elif(60 < event.x < 180 and 510 < event.y < 540):
        data.transientAnalysis = True
def solveCircuit(data):##THIS IS THE MEAT####### 
    def getGroundCount(data):
        #Check to see for one ground - determine ground starting point
        for row in range(len(data.elementGrid)):
            for col in range(len(data.elementGrid[0])):
                if type(data.elementGrid[row][col]) == Ground: 
                    data.GroundCount.append((row,col))
        return data.GroundCount
    def getVoltageLocation(data):
        for row in range(len(data.elementGrid)):
            for col in range(len(data.elementGrid[0])):
                if(type(data.elementGrid[row][col]) == DCVoltageSource or 
                   type(data.elementGrid[row][col]) == DCCurrentSource): 
                    data.voltageLocation.append((row, col))
        return data.voltageLocation
    def getClosestGround(data):
        groundCount = getGroundCount(data)
        VoltageLocation = getVoltageLocation(data)
        minGround  = None
        minValue = None
        for ground in groundCount:
            currentValue = (abs(ground[0] - VoltageLocation[0][0]) + abs(ground[1] - VoltageLocation[0][1]) )
            currentGround = ground
            if(minValue == None or currentValue < minValue): 
                minValue = currentValue
                minGround = ground
        (data.startRow, data.startCol) = minGround #sert startRow, startCol to the minGround
    def getNodeCount(data, startRow, startCol):
        (NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,-1), (1,0), (0,1))
        count = 0
        for (drow, dcol) in (NORTH, WEST, SOUTH, EAST):
            if(data.elementGrid[startRow+drow][startCol+dcol] != 0): count +=1
        return count
    def AllNonZero(data):
        count = 0
        for row in range(len(data.elementGrid)):
            for col in range(len(data.elementGrid[0])):
                if(data.elementGrid[row][col] !=0): count +=1
        return count
    def buildRecursiveDictionaryWrapper(data):
        return buildRecursiveDictionary(data.dictionary, data.elementGrid, 
            data.booleanGrid, data.startRow, data.startCol)
    def buildRecursiveDictionary(dictionary, elementGrid, booleanGrid, startRow, startCol, layer=0):
        if(layer > 0 and type(elementGrid[startRow][startCol]) == Ground): 
            return elementGrid[startRow][startCol]
        else: 
            (NORTH, EAST, SOUTH, WEST) = ((-1,0), (0,-1), (1,0), (0,1))
            for (drow, dcol) in (NORTH, WEST, SOUTH, EAST):
                if(elementGrid[startRow+drow][startCol+dcol] != 0 and booleanGrid[startRow+drow][startCol+dcol]):
                    booleanGrid[startRow][startCol] = False
                    nodeCount = getNodeCount(data, startRow, startCol)
                    curElem = elementGrid[startRow][startCol]
                    if(nodeCount > 2): #goes into a "Y" direction
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
    def isLegalCircuitBasic(data):
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
    def isLegalCircuitAdvanced(data): 
        for voltage in data.voltageLocation:
            print(voltage, data.startCol)
            if voltage[1] != data.startCol: return False
        return True
    def determineVoltageandCurrentBasic(data):
        if(isLegalCircuitBasic(data) and len(data.acVoltage) == 0 and len(data.acCurrent) == 0):
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
                        (dcVoltage.i0, dcVoltage.i8) = (0.01*int(100*totalCurrent), 0.01*int(100*totalCurrent))
                #All capacitors and resistors
                elif(len(data.resistors) > 0 and len(data.capacitors) > 0 and len(data.inductors)==0):
                    totalResistance = 0
                    (totalCapacitanceNumerator, totalCapacitanceDenomator) = (1, 0)
                    for resistor in data.resistors:
                        totalResistance += resistor.resistance
                    totalCurrent = totalVoltageSupply/totalResistance #Ohm's Law 
                    for capacitor in data.capacitors:
                        totalCapacitanceNumerator *= capacitor.capacitance
                        totalCapacitanceDenomator += capacitor.capacitance
                    if(len(data.capacitors) > 1): totalCapacitance = totalCapacitanceNumerator/totalCapacitanceDenomator
                    else: totalCapacitance = totalCapacitanceDenomator
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
                        (inductor.v0, inductor.v8) = (0.01*int(100*totalVoltageSupply*
                            inductor.inductance/totalInductance), 0.00)
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
        else: data.isLegalCircuit = False ###THIS IS THE MEAT OF THE MEAT###
    def getParallelResistanceAdvancedNumerator(newResistorList, parallelResistance=1): 
        for resistor in newResistorList:
            parallelResistance *= resistor.resistance
        return parallelResistance
    def getParallelResistanceAdvancedDenominator(powerSetNewResistorList, newResistorList, parallelResistance=0):
        for List in powerSetNewResistorList:
            if(len(List) == len(newResistorList)-1): # we got a good set
                blockSet = 1
                for element in List: #we go through each resistor
                    blockSet *= element.resistance
                parallelResistance += blockSet
        return parallelResistance
    def flattenList(resistorList, newResistorList=[]):
        if(resistorList == []): return newResistorList
        elif(type(resistorList[0])== list):
            return flattenList(resistorList[0], newResistorList)
        else: #we have a resistor itself
            newResistorList.append(resistorList[0])
            return flattenList(resistorList[1:], newResistorList)
    def powerset(a): #CITE(THIS IS 15-112 code)
        if (len(a) == 0): return [[]]
        else:
            allSubsets = [ ]
            for subset in powerset(a[1:]):
                allSubsets += [subset]
                allSubsets += [[a[0]] + subset]
            return allSubsets
    def carveOutResistor(subdictionary):
        if(type(subdictionary) == list): return [carveOutResistor(subdictionary[0]), carveOutResistor(subdictionary[1])]
        else:
            for element in subdictionary: #there better fucking be a resistor in there
                if(type(element) == Resistor): return element
                else: 
                    return carveOutResistor(subdictionary[element])
    def determineVoltageandResistanceAdvancedWrapper(data):
        dictionary = buildRecursiveDictionaryWrapper(data)
        if(len(data.acVoltage)==0 and len(data.acCurrent)==0 and len(data.dcVoltage) !=0 and 
            isLegalCircuitAdvanced(data)): 
            data.isLegalCircuit = True
            return determineVoltageandResistanceAdvanced(dictionary)
        else: data.isLegalCircuit = False
    def determineVoltageandResistanceAdvanced(dictionary, totalVoltageSupply=0, 
        totalResistanceNumerator=1, totalResistanceDenominator=0, totalResistance=0):
        for element in dictionary:
            if(type(element)==DCVoltageSource): #pop in the voltage supply
                totalVoltageSupply += element.voltage
                determineVoltageandResistanceAdvanced(dictionary[element], totalVoltageSupply, 
                        totalResistanceNumerator, totalResistanceDenominator, totalResistance)
            elif(type(element)== Resistor): #If we have a resistor in series with the Voltage Source
                    totalResistance += element.resistance
                    element.inParralel = False
                    determineVoltageandResistanceAdvanced(dictionary[element], totalVoltageSupply, 
                        totalResistanceNumerator, totalResistanceDenominator, totalResistance)
            elif(type(dictionary)==list): #ok, now we are in the parallel section
                resistorList = [ ]
                for subdictionary in dictionary: #we are iterating through each dictionary in the list
                    resistor = carveOutResistor(subdictionary)
                    resistorList.append(resistor)
                newResistorList = flattenList(resistorList)
                equivalentResistanceNumerator = getParallelResistanceAdvancedNumerator(newResistorList)
                powerSetNewResistorList = powerset(newResistorList)
                equivalentResistanceDenominator = getParallelResistanceAdvancedDenominator(powerSetNewResistorList, 
                    newResistorList)
                totalResistance += (equivalentResistanceNumerator/equivalentResistanceDenominator)
                solveVoltageAndResistanceAdvanced(totalVoltageSupply, totalResistance)
                break #after we do it once, we can break
            elif(type(element) == CornerWire or type(element) == Wire or type(element)==Ground): #proceed
                determineVoltageandResistanceAdvanced(dictionary[element], totalVoltageSupply, 
                    totalResistanceNumerator, totalResistanceDenominator, totalResistance) ###MEAT OF THE MEAT###
    def solveVoltageAndResistanceAdvanced(totalVoltageSupply, totalResistance):
        totalCurrent = totalVoltageSupply/totalResistance
        currentVoltageSupply = totalVoltageSupply
        for resistor in data.resistors:
            if(not resistor.inParralel): 
                currentVoltageSupply -= (resistor.resistance*totalCurrent)
                (resistor.i0, resistor.i8) = (0.01*int(100*totalCurrent), 0.01*int(100*totalCurrent))
                (resistor.v0, resistor.v8) = (0.01*int(100*resistor.resistance*totalCurrent), 
                    0.01*int(100*resistor.resistance*totalCurrent))
        for resistor in data.resistors:
            if(resistor.inParralel):    
                (resistor.v0, resistor.v8) = (0.01*int(100*currentVoltageSupply), 0.01*int(100*currentVoltageSupply))
                (resistor.i0, resistor.i8) = (0.01*int(100*currentVoltageSupply/resistor.resistance), 
                    0.01*int(100*currentVoltageSupply/resistor.resistance))
        for dcVoltage in data.dcVoltage:
            (dcVoltage.v0, dcVoltage.v8) = (-dcVoltage.voltage, -dcVoltage.voltage)
            (dcVoltage.i0, dcVoltage.i8) = (0.01*int(100*totalCurrent), 0.01*int(100*totalCurrent))

    getGroundCount(data)
    if(len(data.GroundCount) < 2): data.isLegalCircuit = False #Can't have a circuit like this now can we
    elif(len(data.GroundCount) == 2 and (len(data.dcVoltage) != 0 or len(data.dcCurrent) != 0 )): 
        getClosestGround(data)
        determineVoltageandCurrentBasic(data)
    else:
        if len(data.acVoltage) > 0 or len(data.acCurrent) > 0: data.isLegalCircuit = False
        elif (len(data.GroundCount) > 2 and (len(data.dcVoltage) > 0 or len(data.dcCurrent) > 0)
            and len(data.capacitors) == 0 and len(data.inductors) == 0): 
            getClosestGround(data)
            determineVoltageandResistanceAdvancedWrapper(data)
        else: data.isLegalCircuit = False
def calculateTao(data): #Assume we have at least one resistor and no LC circuit
    totalResistance = 0
    if(len(data.capacitors) > 0):
        totalCapacitance = 0
        for resistor in data.resistors:
            totalResistance += resistor.resistance
        for capacitor in data.capacitors:
            totalCapacitance += capacitor.capacitance
        return (totalResistance*totalCapacitance)
    elif(len(data.inductors) > 0):
        totalInductance = 0
        for resistor in data.resistors:
            totalResistance += resistor.resistance
        for inductor in data.inductors:
            totalInductance += inductor.inductance
        return (totalInductance/totalResistance)
def performTransientAnalysis(element, data): #Need to have a resistor
    tao = calculateTao(data)
    vInfinity = element.v8
    vZero = element.v0
    iInfinity = element.i8
    iZero = element.i0
    start = 0
    stop = 6*tao
    step = 0.01*tao
    if(vInfinity > vZero and iZero > iInfinity): 
        x1 = np.arange(start, stop, step)
        y1 = vInfinity*(1-math.e **((-x1)/tao)) 
        plt.plot(x1, y1)
        plt.xlabel("Time(s)")
        plt.ylabel("Voltage(V)/Current(A)")
        y2 = iZero*(math.e**((-x1)/tao))
        plt.plot(x1, y2)
        plt.show()
    elif(vZero > vInfinity and iZero < iInfinity): 
        x1 = np.arange(start, stop, step)
        y1 = vZero*(math.e **(-(x1)/tao) )
        plt.plot(x1, y1)
        plt.xlabel("Time(s)")
        plt.ylabel("Voltage(V)/Current(A)")
        y2 = iInfinity*(1-math.e**(-(x1)/tao))
        plt.plot(x1, y2)
        plt.show()
    elif(iZero > iInfinity and vZero > vInfinity): 
        x1 = np.arange(start, stop, step)
        y1 = iZero*(math.e **(-(x1)/tao)) 
        plt.plot(x1, y1)
        plt.xlabel("Time(s)")
        plt.ylabel("Voltage(V)/Current(A)")
        y2 = vZero*(math.e**(-(x1)/tao))
        plt.plot(x1, y2)
        plt.show()
    elif(iInfinity > iZero and vInfinity > vZero):
        x1 = np.arange(start, stop, step)
        y1 = iInfinity*(1-math.e **(-(x1)/tao)) 
        plt.plot(x1, y1)
        plt.xlabel("Time(s)")
        plt.ylabel("Voltage(V)/Current(A)")
        y2 = vInfinity*(1-math.e**(-(x1)/tao))
        plt.plot(x1, y2)
        plt.show()
    else:
        x1 = np.arange(start, stop, step)
        y1 = iInfinity
        plt.plot(x1, y1)
        plt.xlabel("Time(s)")
        plt.ylabel("Voltage(V)/Current(A)")
        y2 = vInfinity
        plt.plot(x1, y2)
        plt.show()
def redrawAll(canvas, data):
    (width, height) = (900, 600)
    if(data.helpScreen): 
        if(data.restart): init(canvas, data)
        canvas.create_rectangle(0, 0, width, height, fill = "white")
        drawInstructionsMenu(canvas, data)
    elif(not data.helpScreen):
        if(data.restart): init(canvas, data)
        #Create horizontal lines
        for row in range(int(height/30)): 
            if(row %2 == 0): canvas.create_line(-5, row*30,  width+5, row*30, width = 1.0, fill = "black")
            else: canvas.create_line(-5, row*30,  905, row*30, width = 0.5, fill = "light gray")
        for col in range(int(width/30)):
            if(col % 2 == 0): canvas.create_line(col*30, -5, col*30, height + 5, width = 1.0, fill = "black")
            else: canvas.create_line(col*30, -5, col*30, height + 5, width = 0.5, fill = "light gray")
        drawSidePanel(canvas, data)
        drawtopRightBox(canvas, data)
        for resistor in data.resistors:
            if(resistor.isVertical): 
                resistor.drawResistorVertical(canvas)
            else: 
                (x,y) = resistor.getxy()
                resistor.drawResistorOnBoard(canvas)
                data.elementGrid[x//60][y//60] = resistor
                data.booleanGrid[x//60][y//60] = True
        for capacitor in data.capacitors: 
            if(capacitor.isVertical): capacitor.drawCapacitorVertical(canvas)
            else: 
                (x,y) = capacitor.getxy()
                data.elementGrid[x//60][y//60] = capacitor
                data.booleanGrid[x//60][y//60] = True
                capacitor.drawCapacitorOnBoard(canvas)
        for inductor in data.inductors: 
            if(inductor.isVertical): inductor.drawInductorVertical(canvas)
            else: 
                (x,y) = inductor.getxy()
                inductor.drawInductorOnBoard(canvas)
                data.elementGrid[x//60][y//60] = inductor
                data.booleanGrid[x//60][y//60] = True
        for acVoltage in data.acVoltage: 
            (x,y) = acVoltage.getxy()
            acVoltage.drawACVoltageOnBoard(canvas)
            data.elementGrid[x//60][y//60] = acVoltage
            data.booleanGrid[x//60][y//60] = True
        for acCurrent in data.acCurrent: 
            acCurrent.drawACCurrentOnBoard(canvas)
            (x,y) = acCurrent.getxy()
            data.elementGrid[x//60][y//60] = acCurrent
            data.booleanGrid[x//60][y//60] = True
        for dcCurrent in data.dcCurrent: 
            (x,y) = dcCurrent.getxy()
            dcCurrent.drawDCCurrentOnBoard(canvas)
            data.elementGrid[x//60][y//60] = dcCurrent
            data.booleanGrid[x//60][y//60] = True
        for dcVoltage in data.dcVoltage: 
            (x,y) = dcVoltage.getxy()
            dcVoltage.drawDCVoltageOnBoard(canvas)
            data.elementGrid[x//60][y//60] = dcVoltage
            data.booleanGrid[x//60][y//60] = True
        for wire in data.wires: 
            if(wire.isVertical): wire.drawWireVertical(canvas)
            else: 
                (x,y) = wire.getxy()
                wire.drawWireOnBoard(canvas)
                data.elementGrid[x//60][y//60] = wire
                data.booleanGrid[x//60][y//60] = True
        for cornerwire in data.cornerWires: 
            if(not cornerwire.top and not cornerwire.left): 
                (x,y) = cornerwire.getxy()
                cornerwire.drawCornerWireBottomRight(canvas)
                data.elementGrid[x//60][y//60] = cornerwire
                data.booleanGrid[x//60][y//60] = True
            elif(cornerwire.top and not cornerwire.left): cornerwire.drawCornerTopRight(canvas)
            elif(not cornerwire.top and cornerwire.left): cornerwire.drawCornerBottomLeft(canvas)
            else: cornerwire.drawCornerTopLeft(canvas)
        for ground in data.ground: 
            (x,y) = ground.getxy()
            ground.drawGroundOnBoard(canvas)
            data.elementGrid[x//60][y//60] = ground
            data.booleanGrid[x//60][y//60] = True

    font = "Arial 16 bold"
    (cx, cy) = canvas.data["motionPosn"]
    canvas.create_text(cx, cy, text="M", font=font)
def init(canvas, data):
    canvas.data["motionPosn"] = (300,300)
    #RLC Elements
    data.resistorSelect = False
    data.resistors = [ ]
    data.resistorvertical = True
    data.capacitorSelect = False
    data.capacitors = [ ]
    data.inductorSelect = False
    data.inductors = [ ]

    #AC Elements
    data.acVoltageSelect = False
    data.acVoltage = [ ]
    data.acCurrentSelect = False
    data.acCurrent = [ ]

    #DC Elements
    data.dcVoltageSelect = False
    data.dcVoltage = [ ]
    data.dcCurrentSelect = False
    data.dcCurrent = [ ]

    #Wire n ground
    data.wireSelect = False
    data.wires = [ ]
    data.cornerWireSelect = False
    data.cornerWires = [ ]
    data.groundSelect = False
    data.ground = [ ]

    data.elementdropper = False
    data.rotaterdeleter = False
    data.elementGrid = [[0]*15 for i in range(10)]
    data.booleanGrid = [[False]*15 for i in range(10)]
    data.displayValues = [0,0,0,0]
    data.restart = False

    data.flashSimulate = False
    data.isLegalCircuit = None
    data.transientAnalysis = False
    data.voltageLocation = []
    data.dictionary = dict()
    data.GroundCount = [ ]
    data.startRow = 0
    data.startCol = 0
    data.helpScreen = False

    redrawAll(canvas, data)
def run():
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()  

    def mouseMotionWrapper(event, canvas, data):
        mouseMotion(event, data)
        redrawAllWrapper(canvas, data)  

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def rightMousePressedWrapper(event, canvas, data):
        rightMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def leftMousePressedWrapper(event, canvas, data):
        leftMousePressed(event, data)
        redrawAllWrapper(canvas, data)


    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=900, height=600)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }

    #create a usable data
    #Main is the class - data can be used
    class Main(object): pass
    data = Main()
    init(canvas, data)

    # set up events
    #KeyPressed, mouseMotion and mousePressed(right click grr)
    root.bind("<Key>", lambda event:
             keyPressedWrapper(event, canvas, data))
    root.bind("<Button-3>", lambda event:
             rightMousePressedWrapper(event, canvas, data))
    canvas.bind("<Motion>", lambda event:
                mouseMotionWrapper(event, canvas, data))
    #left click is drag, snap n drop with data instance
    root.bind("<Button-1>", lambda event:
                leftMousePressedWrapper(event, canvas, data))

    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
