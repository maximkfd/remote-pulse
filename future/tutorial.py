'''
Explanatory animation going over the foundations of how we can extract
someone's pulse from a "non-existent" signal


1. Want to see how we can extract someone's pulse from video?

* First, we need to learn a little bit about noise. Let's take a look at the 
noise on a typical video of a static scene. 
<Do video of a checkerboard pattern?> <Zoom into a region of a normal video>

* You see how the values are jittering ever so slightly? It doesn't mean
that you have a bad camera, it's actually from the randomness in the number
of photons received by that pixel on the camera. Since we know that nothing
in our scene is changing, let's plot those pixel values over time...

* Again, we see that the baseline value does not change, but those jitters are 
always there, regardless of the light intensity. <Is there a difference in the 
size of the variation on light vs. dark pixels?>

* Now, let's look at a slightly different scene, a video of someone's hand/face.
<where is that video of hand on top of glass? Can you re-record it? Yes glass table in entryway>
Again, let's plot the values over time. <there probably won't be a change>
<Maybe do video of finger pressed against glass and you can see the actual
color change with reflective PPG>

* Even though we can't see the underlying signal, I can guarantee you that 
the color change from your pulse is buried in that noise. How are we going
to extract it?

* The answer lies in the digitizing operation done by the digital converter
in the camera sensor. It has to convert voltage from millions of photons 
into a value from 0 to 255. This loss of resolution is called ___discretization??_______, and
obscures the underlying signal. However, we can recover it back if we know a 
little bit of probability theory. 

* Let's simulate a really tiny signal that is digitized. <small signal that when 
digitized, rounds to the nearest integer> 

* If the signal's variation doesn't go over a rounding boundary, the signal is 
obscured completely. 

* We're going look at the same data another way. Let's plot a histogram of the
pixel values. Although it might not look like it, the underlying distribution
is actually a Gaussian, which is really use


We won't get into the details,
but this effect is way more noticeable when you have less light or less exposure
time, and close to goes away when you have a lot of light or a long exposure. 
effect isn't from your camera, it's actually from the discrete 
'''



#Great, we can 



'''
Do a scrollable webpage with html5? videos similar to bret victor. Much easier to 
handle and update than a YouTube video
'''






'''
Update the startup and new york guys when you are done. 
'''