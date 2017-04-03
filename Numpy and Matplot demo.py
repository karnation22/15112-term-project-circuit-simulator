bimport numpy as np 
import matplotlib.pyplot as plt 
#THIS IS A NUMP AND MATPLOTLIB DEMO!!
#Sine wave
def sinWave():
	frequency = 2
	offset = 10
	amplitude = 10
	start = 0
	stop = 2*np.pi
	step = .01
	x = np.arange(start, stop, step)
	y = amplitude*np.cos(frequency*x)+offset
	plt.plot(x,y)
	plt.ylabel = ("Voltage(V)")
	plt.xlabel = ("Time(s)")
	plt.show()

def squareWave():
	offset = 10
	amplitude = 10
	start = 0
	stop = 10
	step = 0.01
	x2 = np.arange(start,stop,step)
	y2 = np.ceil(x2) % 2
	plt.plot(x2,y2)
	plt.y2label = ("Voltage(V)")
	plt.x2label = ("Time(s)")
	plt.show()

def sawtoothWave():
	offset = 10
	amplitude = 10
	start = 0
	stop = 10
	step = 0.01
	x3 = np.arange(start, stop, step)
	y3 = x3%2
	plt.plot(x3,y3)
	plt.y3label = ("Voltage(V)")
	plt.x3label = ("Time(s)")
	plt.show()


squareWave()
sinWave()
sawtoothWave()
