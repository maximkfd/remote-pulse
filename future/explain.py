"""
Show what happens when we average data generated from a Gaussian noise source
plus an underlying signal that is below the sampling threshold.
"""  

# draggable rectangle with the animation blit techniques; see
# http://www.scipy.org/Cookbook/Matplotlib/Animations
from matplotlib import mlab
import numpy

import matplotlib.pyplot as pyplot
import numpy as np


class DraggableRectangle:
    lock = None  # only one can be animated at a time
    def __init__(self, rect):
        self.rect = rect
        self.press = None
        self.background = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return
        if DraggableRectangle.lock is not None: return
        contains, attrd = self.rect.contains(event)
        if not contains: return
        print 'event contains', self.rect.xy
        x0, y0 = self.rect.xy
        w = self.rect.width
        h = self.rect.height
        
        print '%d,%d' %(w,h)
        
        self.press = x0, y0, event.xdata, event.ydata
        DraggableRectangle.lock = self

        # draw everything but the selected rectangle and store the pixel buffer
        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        self.rect.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.rect.axes.bbox)

        # now redraw just the rectangle
        axes.draw_artist(self.rect)

        # and blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if DraggableRectangle.lock is not self:
            return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)
        self.rect.set_width()

        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        # restore the background region
        canvas.restore_region(self.background)

        # redraw just the current rectangle
        axes.draw_artist(self.rect)

        # blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_release(self, event):
        'on release we reset the press data'
        if DraggableRectangle.lock is not self:
            return

        self.press = None
        DraggableRectangle.lock = None

        # turn off the rect animation property and reset the background
        self.rect.set_animated(False)
        self.background = None

        # redraw the full figure
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


class ROI:
    """
    A region of pixels that we want to average over
    """
    def __init__(self, fig, widthInit=5,heightInit=5):
        """
        Parameters
        ----------
        fig : matplotlib figure handle
            
        """
        self.width  = widthInit
        self.height = heightInit
        self.fig    = fig
    
    def update(self, points):
        assert len(points) == len(self)
        
        # Plot the array of points
#         self.fig.

        
    def __len__(self):
        return self.width*self.height

class Generator():
    """
    Gaussian shot noise generator that is sampled in time and discretized
    """
    
    def __init__(self, ax, varianceInit=2, numBins=8):
        """
        """
        self.ax = ax
        # Take 50 steps to create a sin wave. Amplitude of 1 for now
        # It might be useful to let the user interact with the amplitude of the 
        # signal too. Kind of a depressing thing to see it not work, but it is 
        # good to know the edge cases.
        t = numpy.arange(50)
        self.waveform = 128 + numpy.sin(t*(2*numpy.pi)/50)
        self.idx = 0
        self.variance = varianceInit
        
        # Plot numbins intensity levels on the right bottom of the figure 
        self.ax.grid()

        # Plot a gaussian with mean of the signal[idx] and variance of 
        # self.variance
        self.x = numpy.linspace(128-numBins/2,128+numBins/2,100)
        self.ax.plot(self.x,mlab.normpdf(self.x,self.waveform[self.idx],numpy.sqrt(self.variance)))
    def update(self, n):
        # Update the gaussian
        self.ax.plot(self.x,n*mlab.normpdf(self.x,self.waveform[self.idx],numpy.sqrt(self.variance)))

        signal = self.waveform[self.idx] + numpy.random.randn(n)
        
        # Plot signal as vertical... red? lines on the gaussian (before
        # discretizing the signal)
        for value in signal:
            self.ax.plot([value,0],[value,1],'r-')
        
        # Discretize the signal 
        signal = numpy.floor(signal)
        
        # Plot the resulting histogram, pretty transparent,
        # maybe with a number of the count in the bin too
#         self.fig
        return signal
    
fig = pyplot.figure()
roi = ROI(fig.add_subplot(131))
generator = Generator(fig.add_subplot(132))

while True:
    # Pick another set of points based on the width of the ROI

    points = generator.update(len(roi))
    roi.update(points)
    print points
    fig.draw()