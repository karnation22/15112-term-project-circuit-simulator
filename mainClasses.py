import math
class Element(object):
    def __init__(self): pass
    def getCorners(self): return (self.topx, self.topy, self.topx + self.squareSide, self.topy + self.squareSide)
    def getxy(self): return (self.topy, self.topx)
    def getvi(self): return(self.i0, self.i8, self.v0, self.v8)
class Resistor(Element):
    def __init__(self, topx, topy, rotaterdeleter, isVertical):
        self.squareSide = 60
        self.resistance = 10
        self.topx = topx
        self.topy = topy
        self.boxmargin = 5
        self.small = 10
        self.large = 20
        self.rotaterdeleter = rotaterdeleter
        self.isVertical = isVertical
        self.inParralel = True
        (self.v0, self.v8, self.i0, self.i8) = (None, None, None, None)

    def drawResistorOnBoard(self, canvas):
        #print the actual resistance
        canvas.create_text(self.topx, self.topy, text = "%s ohms" % str(self.resistance),
            font="Arial 10 bold", fill = "black", anchor = "nw")
        #create the tails of the resistor
        canvas.create_line(self.topx, self.topy + self.squareSide//2, 
            self.topx + 2*self.boxmargin, self.topy + self.squareSide//2, width = 2)
        canvas.create_line(self.topx + self.squareSide, self.topy + self.squareSide//2,
            self.topx + self.squareSide - 2*self.boxmargin, self.topy + self.squareSide//2, width=2)
        #create the middle crooked part
        canvas.create_line(self.topx + 2*self.boxmargin, self.topy + self.squareSide//2, self.topx + 
            2*self.boxmargin + self.small*math.sin(math.pi/6), self.topy + self.squareSide//2 + 
            self.small*math.cos(math.pi/6), width=2)
        canvas.create_line(self.topx + 2*self.boxmargin + self.small*math.sin(math.pi/6), 
             self.topy + self.squareSide//2 + self.small*math.cos(math.pi/6), 
             self.topx + 2*self.boxmargin + self.small*math.sin(math.pi/6) + self.large*math.sin(math.pi/6),
             self.topy + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6), width=2)
        canvas.create_line(self.topx + 2*self.boxmargin + self.small*math.sin(math.pi/6) + self.large*math.sin(math.pi/6),
             self.topy + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6),
             self.topx + 2*self.boxmargin + self.small*math.sin(math.pi/6) + 2*self.large*math.sin(math.pi/6),
             self.topy + self.squareSide//2 + self.small*math.cos(math.pi/6), width=2)
        canvas.create_line(self.topx + 2*self.boxmargin + self.small*math.sin(math.pi/6) + 2*self.large*math.sin(math.pi/6),
             self.topy + self.squareSide//2 + self.small*math.cos(math.pi/6),
             self.topx + 2*self.boxmargin + self.small*math.sin(math.pi/6) + 3*self.large*math.sin(math.pi/6),
             self.topy + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6), width=2)
        canvas.create_line(self.topx + 2*self.boxmargin + self.small*math.sin(math.pi/6) + 3*self.large*math.sin(math.pi/6),
             self.topy + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6),
              self.topx + self.squareSide - 2*self.boxmargin, self.topy + self.squareSide//2, width = 2)

    def drawResistorVertical(self, canvas): 
        #Print the actual resistance
        canvas.create_text(self.topx + (3*self.squareSide)//4, self.topy + self.squareSide//2,
            text = "%s ohms" % str(self.resistance), font="Arial 10 bold", fill = "black", anchor = "w")
        #Create the tails of the resistors
        canvas.create_line(self.topx + self.squareSide//2, self.topy, 
            self.topx + self.squareSide//2, self.topy + 2*self.boxmargin, width = 2)
        canvas.create_line(self.topx + self.squareSide//2, self.topy + self.squareSide - 2*self.boxmargin,
            self.topx + self.squareSide//2, self.topy + self.squareSide, width=2)
        #create the middle crooked part
        canvas.create_line(self.topx + self.squareSide//2 , self.topy + 2*self.boxmargin, 
            self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6), 
            self.topy + 2*self.boxmargin + self.small*math.sin(math.pi/6), width=2)
        canvas.create_line(self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6) , 
            self.topy + 2*self.boxmargin + self.small*math.sin(math.pi/6), 
            self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6), 
            self.topy + 2*self.boxmargin + self.small*math.sin(math.pi/6) + self.large*math.sin(math.pi/6), width=2)
        canvas.create_line(self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6),
         self.topy + 2*self.boxmargin + self.small*math.sin(math.pi/6) + self.large*math.sin(math.pi/6), 
         self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6), self.topy+ 
         2*self.boxmargin + self.small*math.sin(math.pi/6) + 2*self.large*math.sin(math.pi/6), width=2)
        canvas.create_line(self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6), self.topy + 
            2*self.boxmargin + self.small*math.sin(math.pi/6) + 2*self.large*math.sin(math.pi/6), 
            self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6), 
            self.topy + 2*self.boxmargin + self.small*math.sin(math.pi/6) + 3*self.large*math.sin(math.pi/6), width=2)
        canvas.create_line(self.topx + self.squareSide//2 + self.small*math.cos(math.pi/6) - self.large*math.cos(math.pi/6), 
            self.topy + 2*self.boxmargin + self.small*math.sin(math.pi/6) + 3*self.large*math.sin(math.pi/6), 
            self.topx + self.squareSide//2, self.topy + self.squareSide - 2*self.boxmargin, width=2)
class Capacitor(Element):
    def __init__(self, topx, topy, rotaterdeleter, isVertical):
        self.squareSide = 60
        self.capacitance = 5
        self.topx = topx
        self.topy = topy
        self.boxmargin = 0
        self.verlength = 20
        self.horlength = 16
        self.hor2length = 12
        self.rotaterdeleter = rotaterdeleter
        self.isVertical = isVertical
        (self.v0, self.v8, self.i0, self.i8) = (None, None, None, None)

    def drawCapacitorOnBoard(self, canvas):
        #Create the text label
        canvas.create_text(self.topx + self.squareSide, self.topy + 0.75*self.squareSide, 
            text="%s F"% str(self.capacitance), font = "Arial 10 bold", anchor = "ne")
        #create vertical lines
        canvas.create_line(self.topx + self.squareSide//2, self.topy + self.boxmargin, 
            self.topx + self.squareSide//2, self.topy + self.boxmargin + self.verlength, width=2)
        canvas.create_line(self.topx + self.squareSide//2, self.topy + self.squareSide - self.boxmargin,
            self.topx + self.squareSide//2, self.topy + self.squareSide - self.boxmargin - self.verlength, width=2)

        #create horizontal lines
        canvas.create_line(self.topx + self.squareSide//2 - self.horlength, self.topy + self.boxmargin + self.verlength, 
            self.topx + self.squareSide//2 + self.horlength, self.topy + self.boxmargin + self.verlength, width=2)

        canvas.create_line(self.topx + self.squareSide//2 - self.hor2length, self.topy + 2*self.verlength, 
            self.topx + self.squareSide//2 + self.hor2length, self.topy + 2*self.verlength, width=2)

    def drawCapacitorVertical(self, canvas):
        #Create the text label
        canvas.create_text(self.topx + self.squareSide, self.topy + 0.75*self.squareSide, 
            text="%s F"% str(self.capacitance), font = "Arial 10 bold", anchor = "ne")
        #Create the tail lines
        canvas.create_line(self.topx + self.boxmargin, self.topy + self.squareSide//2, self.topx + 
            self.boxmargin + self.verlength, self.topy + self.squareSide//2, width=2)
        canvas.create_line(self.topx + self.squareSide - self.boxmargin, self.topy + + self.squareSide//2,
            self.topx + self.squareSide - self.boxmargin - self.verlength, self.topy + self.squareSide//2, width=2)
        #create horizonal lines
        canvas.create_line(self.topx + self.boxmargin + self.verlength, self.topy + self.squareSide//2 - self.horlength,
            self.topx + self.boxmargin + self.verlength, self.topy + self.squareSide//2 + self.horlength, width=2)
        canvas.create_line(self.topx + 2*self.verlength, self.topy + self.squareSide//2 - self.hor2length,
            self.topx + 2*self.verlength, self.topy + self.squareSide//2 + self.hor2length, width=2)
class Inductor(Element):
    def __init__(self, topx, topy, rotaterdeleter, isVertical): 
        self.squareSide = 60
        self.inductance = 5
        self.topx = topx
        self.topy = topy
        self.boxmargin = 5
        self.verlength = 10
        self.verlength2 = 15
        self.lrad = 5
        self.rotaterdeleter = rotaterdeleter
        self.isVertical = isVertical
        (self.i0, self.i8, self.v0, self.v8) = (None, None, None, None)

    def drawInductorOnBoard(self, canvas):
        #Create the text label
        canvas.create_text(self.topx + self.squareSide, self.topy + 0.75*self.squareSide, 
            text="%s H"% str(self.inductance), font = "Arial 10 bold", anchor = "ne")
        #Inductor Lines
        canvas.create_line(self.topx + self.squareSide//2, self.topy, self.topx + 
            self.squareSide//2, self.topy + self.verlength2, width=2)

        canvas.create_line(self.topx + self.squareSide//2, self.topy + self.squareSide,
            self.topx + self.squareSide//2, self.topy + self.squareSide - self.verlength2 , width=2)
    
        #Inductor arcs (each with a diameter of 10)
        canvas.create_arc(self.topx + self.squareSide//2 - 2*self.lrad, self.topy + 
            self.boxmargin + self.verlength, self.topx + self.squareSide/2 + 2*self.lrad,
            self.topy + self.boxmargin + self.verlength + 2*self.lrad, start = 90, extent=180, width=2)

        canvas.create_arc(self.topx + self.squareSide//2 - 2*self.lrad, self.topy + 
            self.boxmargin + self.verlength + 2*self.lrad, self.topx + self.squareSide/2 + 2*self.lrad,
            self.topy + self.boxmargin + self.verlength + 4*self.lrad, start = 90, extent=180, width=2)

        canvas.create_arc(self.topx + self.squareSide//2 - 2*self.lrad, self.topy + 
            self.boxmargin + self.verlength + 4*self.lrad, self.topx + self.squareSide/2 + 2*self.lrad,
            self.topy + self.boxmargin + self.verlength + 6*self.lrad, start = 90, extent=180, width=2)

    def drawInductorVertical(self, canvas):
        #Create the text label
        canvas.create_text(self.topx + self.squareSide, self.topy + 0.75*self.squareSide, 
            text="%s H"% str(self.inductance), font = "Arial 10 bold", anchor = "ne")
        #Create the tail lines
        canvas.create_line(self.topx, self.topy + self.squareSide//2, self.topx + self.verlength2,
            self.topy + self.squareSide//2, width=2)
        canvas.create_line(self.topx + self.squareSide, self.topy + self.squareSide//2, 
            self.topx + self.squareSide - self.verlength2, self.topy + self.squareSide//2, width=2)
        #draw up the inductor arcs (lets hope it works!)
        canvas.create_arc(self.topx + self.boxmargin + self.verlength, self.topy + self.squareSide//2 - 2*self.lrad,
            self.topx + self.boxmargin + self.verlength + 2*self.lrad, self.topy + self.squareSide/2 + 2*self.lrad, 
            start = 0, extent = 180, width=2)
        canvas.create_arc(self.topx + self.boxmargin + self.verlength + 2*self.lrad, self.topy +
            self.squareSide//2 - 2*self.lrad, self.topx + self.boxmargin + self.verlength + 4*self.lrad,
            self.topy + self.squareSide/2 + 2*self.lrad, start = 0, extent = 180, width=2)
        canvas.create_arc(self.topx + self.boxmargin + self.verlength + 4*self.lrad, self.topy +
            self.squareSide//2 - 2*self.lrad, self.topx + self.boxmargin + self.verlength + 6*self.lrad,
            self.topy + self.squareSide/2 + 2*self.lrad, start = 0, extent = 180, width=2)
class VoltageSource(Element): 
    def __init__(self): 
        pass
class ACVoltageSource(VoltageSource):
    def __init__(self, topx, topy, rotaterdeleter):
        self.topx = topx
        self.topy = topy
        self.squareSide = 60
        self.circRad = 15
        self.signsize = 5
        self.signadjust = 6
        self.sinesize = 3
        self.rotaterdeleter = rotaterdeleter

    def drawACVoltageOnBoard(self, canvas):
        (centerx, centery) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_oval(centerx - self.circRad, centery - self.circRad, centerx + self.circRad, 
            centery + self.circRad, width=2)
        #create the lines
        canvas.create_line(centerx, centery + self.circRad, centerx, centery + self.squareSide//2, width=2)
        canvas.create_line(centerx, centery - self.circRad, centerx, centery - self.squareSide//2, width=2)
        
        #Plus sign
        canvas.create_line(centerx - self.signsize, centery - self.signadjust, centerx + self.signsize,
            centery - self.signadjust, width=2)
        canvas.create_line(centerx, centery - self.signadjust - self.signsize, centerx, 
            centery - self.signadjust + self.signsize, width = 2)

        #Minus sign
        canvas.create_line(centerx - self.signsize, centery + self.signadjust, centerx + self.signsize,
            centery + self.signadjust, width=2)

        #sine-wave thingy
        canvas.create_line(centerx - self.sinesize, centery - self.sinesize, centerx + self.sinesize,
            centery + self.sinesize, width=2)
        canvas.create_line(centerx + self.sinesize, centery + self.sinesize, centerx + 3*self.sinesize, 
            centery - self.sinesize , width=2)
        canvas.create_line(centerx - self.sinesize, centery - self.sinesize, centerx - 3*self.sinesize,
            centery + self.sinesize, width=2)
class DCVoltageSource(VoltageSource):
    def __init__ (self, topx, topy, rotaterdeleter):
        self.voltage = 10
        self.topx = topx
        self.topy = topy
        self.circRad = 15
        self.signsize = 5
        self.signadjust = 6
        self.squareSide = 60
        self.rotaterdeleter = rotaterdeleter
        (self.v0, self.v8) = (-self.voltage, -self.voltage)
        (self.i0, self.i8) = (None, None)

    def drawDCVoltageOnBoard(self, canvas): 
        (centerx, centery) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_oval(centerx - self.circRad, centery - self.circRad, centerx + self.circRad, 
            centery + self.circRad, width=2)
        #create the lines
        canvas.create_line(centerx, centery + self.circRad, centerx, centery + self.squareSide//2, width=2)
        canvas.create_line(centerx, centery - self.circRad, centerx, centery - self.squareSide//2, width=2)
        #Plus sign
        canvas.create_line(centerx - self.signsize, centery - self.signadjust, centerx + self.signsize,
            centery - self.signadjust, width=2)
        canvas.create_line(centerx, centery - self.signadjust - self.signsize, centerx, 
            centery - self.signadjust + self.signsize, width = 2)
        #Minus sign
        canvas.create_line(centerx - self.signsize, centery + self.signadjust, centerx + self.signsize,
            centery + self.signadjust, width=2)
        canvas.create_text(self.topx , self.topy , 
            text="%s V"% str(self.voltage), font = "Arial 10 bold", fill = "black", anchor = "nw")
class CurrentSource(Element):
    def __init__(self): 
        pass
class ACCurrentSource(CurrentSource):
    def __init__(self, topx, topy, rotaterdeleter):
        self.topx = topx
        self.topy = topy
        self.linelen = 10
        self.wingsize = 6
        self.squareSide = 60
        self.circRad = 15
        self.sinesize = 3
        self.rotaterdeleter = rotaterdeleter

    def drawACCurrentOnBoard(self, canvas): 
        (centerx, centery) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_oval(centerx - self.circRad, centery - self.circRad, centerx + self.circRad, 
            centery + self.circRad, width=2)
        canvas.create_line(centerx, centery - self.linelen, centerx, centery + self.linelen, width=2)

        #create the lines
        canvas.create_line(centerx, centery + self.circRad, centerx, centery + self.squareSide//2, width=2)
        canvas.create_line(centerx, centery - self.circRad, centerx, centery - self.squareSide//2, width=2)

        canvas.create_line(centerx - self.wingsize, centery + self.linelen - self.wingsize,
            centerx, centery + self.linelen, width=2)
        canvas.create_line(centerx + self.wingsize, centery + self.linelen - self.wingsize,
            centerx, centery + self.linelen, width=2)

        #sine-wave thingy
        canvas.create_line(centerx - self.sinesize, centery - self.sinesize, centerx + self.sinesize,
            centery + self.sinesize, width=2)
        canvas.create_line(centerx + self.sinesize, centery + self.sinesize, centerx + 3*self.sinesize, 
            centery - self.sinesize , width=2)
        canvas.create_line(centerx - self.sinesize, centery - self.sinesize, centerx - 3*self.sinesize,
            centery + self.sinesize, width=2)
class DCCurrentSource(CurrentSource):
    def __init__(self, topx, topy, rotaterdeleter):
        self.topx = topx
        self.topy = topy
        self.linelen = 10
        self.wingsize = 6
        self.squareSide = 60
        self.circRad = 15
        self.sinesize = 3
        self.rotaterdeleter = rotaterdeleter
        self.current = 1
        (self.i0, self.i8, self.v0, self.v8) = (self.current, self.current, None, None)

    def drawDCCurrentOnBoard(self, canvas):
        (centerx, centery) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_oval(centerx - self.circRad, centery - self.circRad, centerx + self.circRad, 
            centery + self.circRad, width=2)
        canvas.create_line(centerx, centery - self.linelen, centerx, centery + self.linelen, width=2)
        #create the lines
        canvas.create_line(centerx, centery + self.circRad, centerx, centery + self.squareSide//2, width=2)
        canvas.create_line(centerx, centery - self.circRad, centerx, centery - self.squareSide//2, width=2)

        canvas.create_line(centerx - self.wingsize, centery - self.linelen + self.wingsize,
            centerx, centery - self.linelen, width=2)
        canvas.create_line(centerx + self.wingsize, centery - self.linelen + self.wingsize,
            centerx, centery - self.linelen, width=2)
        canvas.create_text(self.topx , self.topy , 
            text="%s A"% str(self.current), font = "Arial 10 bold", fill = "black", anchor = "nw")

class Wire(Element):
    def __init__(self, topx, topy, rotaterdeleter, isVertical):
        self.squareSide = 60
        self.topx = topx
        self.topy = topy
        self.rotaterdeleter = rotaterdeleter
        self.isVertical = isVertical

    def drawWireOnBoard(self, canvas):
        canvas.create_line(self.topx, self.topy + self.squareSide//2, 
            self.topx + self.squareSide, self.topy + self.squareSide//2, width=2)

    def drawWireVertical(self, canvas):
        canvas.create_line(self.topx + self.squareSide//2, self.topy,
            self.topx + self.squareSide//2, self.topy + self.squareSide, width=2)

class CornerWire(Wire):
    def __init__(self, topx, topy, rotaterdeleter, top, left):
        self.squareSide = 60
        self.topx = topx
        self.topy = topy
        self.rotaterdeleter = rotaterdeleter
        self.top = top
        self.left = left
        self.hasPartner = False

    def drawCornerWireBottomRight(self, canvas):
        (cx, cy) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_line(cx, cy, cx + self.squareSide//2, cy, width=2)
        canvas.create_line(cx, cy, cx, cy + self.squareSide//2, width=2)

    def drawCornerBottomLeft(self, canvas): 
        (cx, cy) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_line(self.topx, cy, cx, cy, width=2)
        canvas.create_line(cx, cy, cx, self.topy + self.squareSide, width=2)

    def drawCornerTopLeft(self, canvas): 
        (cx, cy) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_line(cx, cy, cx - self.squareSide//2, cy, width=2)
        canvas.create_line(cx, cy, cx, cy - self.squareSide//2, width=2)

    def drawCornerTopRight(self, canvas): 
        (cx, cy) = (self.topx + self.squareSide//2, self.topy + self.squareSide//2)
        canvas.create_line(cx, cy, cx + self.squareSide//2, cy, width=2)
        canvas.create_line(cx, cy, cx, cy - self.squareSide//2, width=2)

class Ground(Element):
    def __init__(self, topx, topy, rotaterdeleter): 
        self.squareSide = 60
        self.topx = topx
        self.topy = topy
        self.linelen = 7.5
        self.linewidth = 5
        self.linecount = 3
        self.rotaterdeleter = rotaterdeleter
    
    def drawGroundOnBoard(self, canvas): 
        canvas.create_line(self.topx + self.squareSide//2, self.topy + self.squareSide//2, 
            self.topx + self.squareSide//2, self.topy, width=2)

        for line in range(self.linecount, 0, -1): 
            canvas.create_line(self.topx - line*(self.linelen) + self.squareSide//2, self.topy + self.squareSide//2 + 
                (3-line)*(self.linewidth), self.topx + line*(self.linelen) + self.squareSide//2, self.topy + 
                self.squareSide//2 + (3-line)*(self.linewidth), width=2)
