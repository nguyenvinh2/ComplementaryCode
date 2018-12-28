import numpy
import scipy
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import os

numpy.set_printoptions(threshold=numpy.inf, linewidth=numpy.inf)

setpathA = '../assets/comp8a.sc'
setpathB = '../assets/comp8b.sc'

dir = os.path.dirname(__file__)

fileA = os.path.join(dir, setpathA)
fileB = os.path.join(dir, setpathB)

dataA = numpy.fromfile(fileA, dtype='int16')
dataB = numpy.fromfile(fileB, dtype='int16')

complexA = 1.0*dataA[::2]+1.0j*dataA[1::2]
complexB = 1.0*dataB[::2]+1.0j*dataB[1::2]

compFilterA = numpy.repeat(numpy.array([1,1,1,-1,1,1,-1,1]),10)
compFilterB = numpy.repeat(numpy.array([1,1,1,-1,-1,-1,1,-1]),10)

autoCorrA = numpy.correlate(compFilterA, compFilterA, mode='full')
autoCorrB = numpy.correlate(compFilterB, compFilterB, mode='full')

compTotal = autoCorrA + autoCorrB

compTime = numpy.linspace(0,8,80)

plt.subplot(2,1,1)
plt.plot(compTime, compFilterA)
plt.title('Complementary Signal A')
plt.ylabel('Amplitude')
plt.subplot(2,1,2)
plt.plot(compTime, compFilterB)
plt.title('Complementary Signal B')
plt.xlabel('time (in micro-seconds)')
plt.ylabel('Amplitude')
plt.show()

autoCorrTime = numpy.linspace(-8,8,num=159)
combine = plt.plot(autoCorrTime, compTotal, 'r', label='Combined Signal')
lineA, = plt.plot(autoCorrTime, autoCorrA, 'b', label='Signal A')
lineB, = plt.plot(autoCorrTime, autoCorrB, 'g', label='Signal B')
plt.legend(handler_map={lineA: HandlerLine2D(numpoints=4)})
plt.title('Autocorrelation of Complementary Codes')
plt.xlabel('time (in micro-seconds)')
plt.ylabel('Signal Strength')
plt.show()

plt.subplot(2,1,1)
plt.plot(abs(complexA)**2)
plt.title('Unfiltered Signal Return A')
plt.ylabel('Signal Strength')
plt.subplot(2,1,2)
plt.plot(abs(complexB)**2)
plt.title(' Unfiltered Signal Return B')
plt.xlabel('Range')
plt.ylabel('Signal Strength')
plt.show()

signalcorrelationA = numpy.correlate(complexA, numpy.array([1,1,1,-1,1,1,-1,1]), mode='full')
signalcorrelationB = numpy.correlate(complexB, numpy.array([1,1,1,-1,-1,-1,1,-1]), mode='full')

plt.subplot(2,1,1)
plt.plot(abs(signalcorrelationA[8:])**2)
plt.title('Signal Return A Correlated')
plt.ylabel('Signal Strength')
plt.subplot(2,1,2)
plt.plot(abs(signalcorrelationB[8:])**2)
plt.title('Signal Return B Correlated')
plt.xlabel('Range')
plt.ylabel('Signal Strength')
plt.show()





combine = plt.plot(abs(signalcorrelationA[8:]+signalcorrelationB[8:])**2, 'r', label='Combined Return')
plt.title('Combined Return Signal Using Complementary Codes')
plt.xlabel('Range')
plt.ylabel('Signal Strength')
plt.show()