import math
def drawSidePanel(canvas, data):
    (margin, panelWidth, panelHeight) = (30,180,540)
    canvas.create_rectangle(margin, margin, margin+panelWidth, margin+panelHeight,
        fill = "dark gray", width = 5)
    drawTransientAnalysis(canvas, data, margin)
    drawLabels(canvas, margin, panelWidth)
    drawSimulateButton(canvas, data)
    drawVoltageSource(canvas, margin, data)
    drawCurrentSource(canvas, margin, data)
    drawResistor(canvas, margin, data)
    drawCapacitor(canvas, margin, data)
    drawInductor(canvas, margin, data)
    drawWires(canvas, margin, data)
    drawCornerWire(canvas, margin, data)
    drawGround(canvas, margin, data)
    drawStartMenu(canvas, margin, data)
def drawStartMenu(canvas, margin, data):
    canvas.create_rectangle(2*margin, 0, 6*margin, margin-3, fill = "gray")
    canvas.create_text(4*margin, 0.5*margin, text = "Press i for instructions")
def drawInstructionsMenu(canvas, data): 
    (xcorner, ycorner, ystep, xstep) = (20,20,25, 300)
    canvas.create_text(xcorner, ycorner, text="Key Buttons:", font = "Arial 16 bold", anchor = "nw")
    canvas.create_text(xcorner, ycorner + ystep, text = "Press q to restart everything.", font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 2*ystep, text = "Press r to rotate circuit elements.", 
        font = "Arial 10",anchor = "nw")
    canvas.create_text(xcorner, ycorner + 3*ystep, text = "Press d to delete circuit elements.", 
        font = "Arial 10",anchor = "nw")
    canvas.create_text(xcorner, ycorner + 4*ystep, text = "Press s to solve voltages and currents after pressing simulate.",
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 5*ystep, 
        text = "Press t to perform transient analysis after pressing transient analysis.", font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 6*ystep, text = "Press i to switch from help screen to build mode.", 
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 7*ystep, text = "Mouse Motion:", font = "Arial 16 bold", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 8*ystep, text = "Hover over a circuit element before pressing s or t.",
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 9*ystep, text = "Mouse Click:", font = "Arial 16 bold", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 10*ystep, text = "Right-Click side panel to select an element.",
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 11*ystep, text = """Once an element has been selected, left click to snap element on board.""", 
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 12*ystep, text = "Operating Instructions for Build Mode:", 
        font = "Arial 16 bold", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 13*ystep, text = "Use only resistors for parallel connections.",
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 14*ystep, text = """Use RLC for series circuits but use only resistor for dcCurrent Sources.""", 
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 15*ystep, text = """Use ground to ground connections. Don't create a loop!""",
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 16*ystep, text = "Simulate and Transient Analysis:", font = "Arial 16 bold",
        anchor = "nw")
    canvas.create_text(xcorner, ycorner + 17*ystep, text = "Simulate button will turn green if you have a legalCircuit.",
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 18*ystep, text = """Same rule applies for Transient Analysis button; only use transient analysis button for series circuits and dcVoltage sources.""", 
        font = "Arial 10", anchor = "nw")
    canvas.create_text(xcorner, ycorner + 19*ystep, text = """Only press transient analysis button after pressing the simulate button.""", 
        font = "Arial 10", anchor = "nw")

def drawLabels(canvas, margin, panelWidth):
    step = 3
    textLabels = ["RLC Elements", "AC Elements", "DC Elements", "Basic Blocks"]
    for num in range(0, 10, step):
        canvas.create_rectangle(margin, margin+num*margin, margin+panelWidth,
                                margin+(num+1)*margin, fill = "yellow")
        
        canvas.create_text(margin, margin+num*margin, text = textLabels[num//3],
                           font = "Arial 20", anchor = "nw") 
def drawTransientAnalysis(canvas, data, margin): #Assume series circuit
    (x0, x1, y0, y1) = (2*margin, 6*margin, 17*margin, 18*margin)
    font = "Arial 10 bold"
    if(not data.transientAnalysis): 
        canvas.create_rectangle(x0, y0, x1, y1, fill = "yellow")
        canvas.create_text(0.5*(x0+x1), 0.5*(y0+y1), text = "Transient Analysis", fill = "blue", font=font)
    elif(data.flashSimulate and data.isLegalCircuit and len(data.GroundCount) == 4 and data.transientAnalysis): 
        #It has to perform a ground of two twice(hence we need our total GroundCount to be forur)
        canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
        canvas.create_text(0.5*(x0+x1), 0.5*(y0+y1), text = "Transient Analysis", fill = "blue", font=font)
    elif(data.transientAnalysis):
        canvas.create_rectangle(x0, y0, x1, y1, fill = "red")
        canvas.create_text(0.5*(x0+x1), 0.5*(y0+y1), text = "Transient Analysis", fill = "blue", font=font)
def drawSimulateButton(canvas, data): 
    if(not data.flashSimulate):
        canvas.create_rectangle(60, 420, 180, 480, fill = "yellow")
        canvas.create_text(62.5, 440, text = "SIMULATE", font = "Arial 18", fill = "blue", anchor = "nw")
    elif(data.flashSimulate and data.isLegalCircuit): #We succeeded
        canvas.create_rectangle(60, 420, 180, 480, fill = "green")
        canvas.create_text(62.5, 440, text = "SIMULATE", font = "Arial 18", fill = "blue", anchor = "nw")
    elif(data.flashSimulate and not data.isLegalCircuit): #Nope, the simulation will fail now 
        canvas.create_rectangle(60, 420, 180, 480, fill = "red")
        canvas.create_text(62.5, 440, text = "SIMULATE", font = "Arial 18", fill = "blue", anchor = "nw")
def drawWires(canvas, margin, data):
    boxmargin = 5
    if(data.wireSelect): canvas.create_rectangle(margin, 11*margin, 3*margin, 13*margin, fill = "cyan")
    else: canvas.create_rectangle(margin, 11*margin, 3*margin, 13*margin, fill = "light gray")

    canvas.create_line(margin + boxmargin, 12*margin, 3*margin - boxmargin, 12*margin, 
        fill = "black", width=2)
def drawCornerWire(canvas, margin, data):
    boxmargin = 5
    if(data.cornerWireSelect): canvas.create_rectangle(5*margin, 11*margin, 7*margin, 13*margin, fill = "cyan")
    else: canvas.create_rectangle(5*margin, 11*margin, 7*margin, 13*margin, fill = "light gray")
    canvas.create_line(6*margin, 12*margin, 7*margin - boxmargin, 12*margin, width = 2)
    canvas.create_line(6*margin, 12*margin, 6*margin, 13*margin - boxmargin, width = 2)
def drawGround(canvas, margin, data): 
    verlength = 15
    line1 = 5
    linewidth = 4
    linecount = 3
    if(data.groundSelect): canvas.create_rectangle(3*margin, 11*margin, 5*margin, 13*margin, fill = "cyan")
    else: canvas.create_rectangle(3*margin, 11*margin, 5*margin, 13*margin, fill = "light gray")

    canvas.create_line(4*margin, 11*margin + margin//2, 4*margin, 11*margin + margin//2 + verlength, width=2)
    for i in range(linecount,0,-1):
        canvas.create_line(4*margin - line1*(i+1), 11*margin + margin//2 + verlength + 
            (linecount-i)*linewidth, 4*margin + line1*(i+1), 11*margin + margin//2 + 
            verlength + (linecount-i)*linewidth, width=2)
def drawVoltageSource(canvas, margin, data):
    signsize = 5
    sineWavesize = 3
    for num in range(4,8,3):
        if((num == 4 and data.acVoltageSelect) or (num == 7 and data.dcVoltageSelect)):
            canvas.create_rectangle(margin,(num+1)*margin, 3*margin, (num+3)*margin, fill = "cyan")
        else: canvas.create_rectangle(margin,(num+1)*margin, 3*margin, (num+3)*margin, fill = "light gray")

        canvas.create_oval(margin + 0.5*margin, margin*(num+1) + 0.5*margin,
                           3*margin - 0.5*margin, (num+3)*(margin) - 0.5*margin, width=2)
        canvas.create_line(2*margin - signsize, margin*(num+2.2), 2*margin + signsize,
                           margin*(num+2.2), width=2)
        canvas.create_line(2*margin - signsize, margin*(num+1.8), 2*margin + signsize,
                           margin*(num+1.8), width=2)
        canvas.create_line(2*margin, margin*(num+1.8)-signsize, 2*margin,
                           margin*(num+1.8)+signsize, width=2)

        #Create the sine shape thingy
        if(num == 4): 
            canvas.create_line(2*margin - sineWavesize, margin*(num+2) - sineWavesize, 
                2*margin + sineWavesize, margin*(num+2) + sineWavesize, width=2)
            canvas.create_line(2*margin + sineWavesize, margin*(num+2) + sineWavesize,
                2*margin + 3*sineWavesize, margin*(num+2) - sineWavesize, width=2)
            canvas.create_line(2*margin - sineWavesize, margin*(num+2) - sineWavesize,
                2*margin - 3* sineWavesize, margin*(num+2) + sineWavesize, width=2)  
def drawCurrentSource(canvas, margin, data):
    signsize = 10
    sineWavesize  = 3
    buffup = -3
    for num in range(4,8,3):
        if((num == 4 and data.acCurrentSelect) or (num == 7 and data.dcCurrentSelect)):
            canvas.create_rectangle(margin + 2*margin,(num+1)*margin, 
                3*margin + 2*margin, (num+3)*margin, fill = "cyan")
            
        else: canvas.create_rectangle(margin + 2*margin,(num+1)*margin,  
                3*margin + 2*margin, (num+3)*margin, fill = "light gray")

        canvas.create_oval(margin + 0.5*margin + 2*margin, margin*(num+1) + 0.5*margin,
                           3*margin - 0.5*margin + 2*margin, (num+3)*(margin) - 0.5*margin, width=2)
        canvas.create_line(2*margin + 2*margin, margin*(num+1.7), 2*margin + 2*margin,
                           margin*(num+2.3), width=2)
        #Left wing
        canvas.create_line(4*margin, margin*(num + 1.7), 4*margin - signsize*math.sin(math.pi/6),
                           margin*(num + 2.3) - signsize*math.cos(math.pi/6), width=2)
        #Right Wing
        canvas.create_line(4*margin, margin*(num + 1.7), 4*margin + signsize*math.sin(math.pi/6),
                           margin*(num + 2.3) - signsize*math.cos(math.pi/6), width=2)

        #create that sine shape thingy
        if(num == 4): 
            canvas.create_line(4*margin - sineWavesize, margin*(num+2) - sineWavesize - buffup, 
                4*margin + sineWavesize, margin*(num+2) + sineWavesize - buffup, width=2)
            canvas.create_line(4*margin + sineWavesize, margin*(num+2) + sineWavesize - buffup,
                4*margin + 3*sineWavesize, margin*(num+2) - sineWavesize - buffup, width=2)
            canvas.create_line(4*margin - sineWavesize, margin*(num+2) - sineWavesize - buffup,
                4*margin - 3* sineWavesize, margin*(num+2) + sineWavesize - buffup, width=2)           
def drawResistor(canvas, margin, data):
    boxmargin = 5
    small = 10
    large = 20

    if(data.resistorSelect): canvas.create_rectangle(margin, 2*margin, 3*margin, 4*margin, fill = "cyan")
    else: canvas.create_rectangle(margin, 2*margin, 3*margin, 4*margin, fill = "light gray")

    #create the tails of the resistor
    canvas.create_line(margin + boxmargin, 3*margin, margin +2*boxmargin, 3*margin)
    canvas.create_line(3*margin - boxmargin, 3*margin, 3*margin - 2*boxmargin, 3*margin)

    #create the middle crooked part
    canvas.create_line(margin + 2*boxmargin, 3*margin, margin + 2*boxmargin +
                       small*math.sin(math.pi/6), 3*margin + small*math.cos(math.pi/6), width=2)
    canvas.create_line(3*margin - 2*boxmargin, 3*margin, 3*margin - 2*boxmargin - small*math.sin(math.pi/6),
                       3*margin - small*math.cos(math.pi/6), width=2)
    canvas.create_line(margin + 2*boxmargin + small*math.sin(math.pi/6),
                       3*margin + small*math.cos(math.pi/6), margin + 2*boxmargin
                       + small*math.sin(math.pi/6) + large*math.sin(math.pi/6),
                       3*margin + small*math.cos(math.pi/6) - large*math.cos(math.pi/6), width=2)
    canvas.create_line(3*margin - 2*boxmargin - small*math.sin(math.pi/6),3*margin - small*math.cos(math.pi/6),
                       3*margin - 2*boxmargin - small*math.sin(math.pi/6) -large*math.sin(math.pi/6),
                       3*margin - small*math.cos(math.pi/6) + large*(math.cos(math.pi/6)), width=2)
    canvas.create_line(3*margin - 2*boxmargin - small*math.sin(math.pi/6) -large*math.sin(math.pi/6),
                       3*margin - small*math.cos(math.pi/6) + large*(math.cos(math.pi/6)),margin + 2*boxmargin
                       + small*math.sin(math.pi/6) + large*math.sin(math.pi/6),
                       3*margin + small*math.cos(math.pi/6) - large*math.cos(math.pi/6), width=2) 
def drawCapacitor(canvas, margin, data):
    boxmargin = 5
    verlength = 20
    horlength = 16
    hor2length = 12
    if(data.capacitorSelect): canvas.create_rectangle(3*margin, 2*margin, 5*margin, 4*margin, fill = "cyan")
    else: canvas.create_rectangle(3*margin, 2*margin, 5*margin, 4*margin, fill = "light gray")
    
    #Create vertical lines
    canvas.create_line(4*margin, 2*margin + boxmargin, 4*margin, 2*margin + boxmargin + verlength, width=2)
    canvas.create_line(4*margin, 4*margin - boxmargin, 4*margin, 4*margin - boxmargin - verlength, width=2)

    #create horizontal lines
    canvas.create_line(4*margin - horlength, 2*margin + boxmargin + verlength, 4*margin + horlength,
                        2*margin + boxmargin + verlength, width=2)
    canvas.create_line(4*margin - hor2length, 4*margin - boxmargin - verlength, 4*margin + hor2length,
                       4*margin - boxmargin - verlength, width=2)
def drawInductor(canvas, margin, data):
    boxmargin = 5
    verlength = 10
    lrad = 5
    if(data.inductorSelect): canvas.create_rectangle(5*margin, 2*margin, 7*margin, 4*margin, fill = "cyan")
    else: canvas.create_rectangle(5*margin, 2*margin, 7*margin, 4*margin, fill = "light gray")
    #Inductor Lines
    canvas.create_line(6*margin, 2*margin + boxmargin, 6*margin, 2*margin + boxmargin + verlength, width=2)
    canvas.create_line(6*margin, 4*margin - boxmargin, 6*margin, 4*margin - boxmargin - verlength, width=2)
    #Inductor arcs (each with a diameter of 10)
    canvas.create_arc(6*margin - 2*lrad, 2*margin + boxmargin + verlength, 6*margin + 2*lrad,
                      2*margin + boxmargin + verlength + 2*lrad, start = 90, extent=180, width=2)
    canvas.create_arc(6*margin - 2*lrad, 2*margin + boxmargin + verlength + 2*lrad, 6*margin + 2*lrad,
                      2*margin + boxmargin + verlength + 4*lrad, start = 90, extent=180, width=2)
    canvas.create_arc(6*margin - 2*lrad, 2*margin + boxmargin + verlength + 4*lrad, 6*margin + 2*lrad,
                      2*margin + boxmargin + verlength + 6*lrad, start = 90, extent=180, width=2)
def drawtopRightBox(canvas, data):
    #only if we have no ac sources in our circuit
    if(len(data.acCurrent) > 0 or len(data.acVoltage) > 0):
        canvas.create_rectangle(780, 0, 900, 120, fill = "black")

    else:
        canvas.create_rectangle(780, 0, 900, 120, fill = "light gray")

        canvas.create_text(790, 0, text = "I", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(820, 0, text = "=", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(800, 15, text = "0", fill = "orange", font = "Arial 10 bold", anchor = "nw")
        canvas.create_text(850, 6, text = "%s A" % str(data.displayValues[0]), fill = "orange", 
        font = "Arial 12", anchor = "nw")

        canvas.create_text(790, 30, text = "V", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(805, 45, text = "0", fill = "orange", font = "Arial 10 bold", anchor = "nw")
        canvas.create_text(820, 30, text = "=", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(850, 36, text = "%s V" % str(data.displayValues[2]), fill = "orange", 
        font = "Arial 12 ", anchor = "nw")

        canvas.create_text(790, 60, text = "I", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(820, 60, text = "=", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(790, 90, text = "V", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(850, 66, text = "%s A" % str(data.displayValues[1]), fill = "orange", 
        font = "Arial 12", anchor = "nw")

        canvas.create_text(820, 90, text = "=", fill = "orange", font = "Arial 20", anchor = "nw")
        canvas.create_text(800, 75, text = "oo", fill = "orange", font = "Arial 10 bold", anchor = "nw")
        canvas.create_text(805, 105, text = "oo", fill = "orange", font = "Arial 10 bold", anchor = "nw")
        canvas.create_text(850, 96, text = "%s V" % str(data.displayValues[3]), fill = "orange", 
        font = "Arial 12", anchor = "nw")