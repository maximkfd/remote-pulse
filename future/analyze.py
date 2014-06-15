import numpy
from future import common
import matplotlib.pyplot as pyplot


hrMin = 30;   # Heart rate min in BPM
hrMax = 180;  # Heart rate max in BPM
hrvMax = 10;   # Expected Heart Rate Variability over trial in BPM
psrThreshold = 8;

plotFFT = True



# Select green channel only for analysis. Also, select after filter rise time
# The array green is (pixel,time)
green = numpy.transpose(numpy.reshape(amplifiedRegion[baselineFilterHistory:, :, :, 1], (-1, finalHeight * finalWidth)))

# Mean over all of the ROI's
greenOverallMean = numpy.mean(green, axis = 0, dtype = numpy.double)
numSamples = greenOverallMean.shape[0]
# Compute FFT and its absolute value
fftAbs = numpy.abs(numpy.fft.rfft(greenOverallMean))
x = numpy.linspace(0, framesPerSecond / 2, num = numSamples / 2 + 1)


#### Compute Peak-to-Sidelobe Ratio ####
# Find the heart rate fundamental by finding the max of fft in valid HR region
# Convert to Hz
hrMinIndex = int((float(hrMin) / 60) / (framesPerSecond / 2) * (numSamples / 2))
hrMaxIndex = int((float(hrMax) / 60) / (framesPerSecond / 2) * (numSamples / 2))
hrvMaxIndex = int((float(hrvMax) / 60) / (framesPerSecond / 2) * (numSamples / 2))
hrIndex = hrMinIndex + numpy.argmax(fftAbs[hrMinIndex:hrMaxIndex])

# Sidelobe is peak + hrv to next hr harmonic - hrv
sidelobe = fftAbs[hrIndex + hrvMaxIndex:hrIndex * 2 - hrvMaxIndex]

psr = (fftAbs[hrIndex] - numpy.mean(sidelobe)) / numpy.std(sidelobe)
hr = (float(hrIndex) / (numSamples / 2)) * (framesPerSecond / 2) * 60

    


if (plotFFT == True):
    pyplot.figure(figsize = (4, 3))
    pyplot.plot(x, fftAbs)
    pyplot.plot(x[hrIndex], fftAbs[hrIndex], 'ro')
    x1, x2, y1, y2 = pyplot.axis()
    pyplot.axis((x1, x2, 0, fftAbs[hrIndex] + 50))
    pyplot.xlabel('Frequency (Hz)')
    pyplot.ylabel('Magnitude')
    pyplot.show(block = False)



if (psr > psrThreshold):
    print 'HR: ' + str(hr) + ' BPM'
    print 'PSR: ' + str(psr) + ' ---> Alive'
    future.common.draw_str(alignedRegion, (0, regionHeight / 2), 'Alive')
    out = 1
else:
    print 'PSR: ' + str(psr) + ' ---> Dead'
    future.common.draw_str(alignedRegion, (0, regionHeight / 2), 'Dead')
    out = 0
    
    
pyplot.close()