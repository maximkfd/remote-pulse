
Explanation
-----------
The color change in your skin due to your pulse is very tiny. Normally, we can't see it, but because of the randomness of light particles ("shot noise"), we can extract the color change by averaging in time and space over a large number of pixels. It's a similar idea to [Dithering](http://en.wikipedia.org/wiki/Dither), although we're looking at a *movie* instead of just an image.

Installation
------------
Install Python, Numpy, and OpenCV. I have had best results using [Python(x,y)](http://code.google.com/p/pythonxy/) on Windows, but you need to select OpenCV on the install for it to load the proper DLL's. Let me know what you find for other distributions and I'll add it to this README.

Additionally, you need to download my repository of common scripts, located [here](https://github.com/nolanhergert/lib), and add it to the PYTHONPATH environmental variable.

Operation
---------
Run [main.py](https://github.com/nolanhergert/remote-pulse/blob/master/main.py) with either a webcam attached or a path to a pre-recorded video file. The best video is recorded in a lit environment (daylight is great) with minimal motion from the subject and passersby and minimal automatic adjustment and compression from the camera. An example video is included and runs by default. 

**Command line options**
`python main.py` runs default video.
`python main.py 0` runs off your default webcam.
`python main.py file.avi` runs `file.avi`

**To record a video**

Run [Video.py](https://github.com/nolanhergert/lib/blob/master/python/lib/cv/Video.py) and it will output 15 seconds of uncompressed video into a file (default is webcam.avi).

Additional Notes
----------------
* Very helpful OpenCV example code is at: https://github.com/Itseez/opencv/tree/master/samples
* I tried to organize the code so that it is easily understood and reusable in your own projects. Feel free to add it to your own libraries without attribution.
* Demo videos are at http://nhergert.homenet.org/doku.php?id=projects:remoteppg

To Do
-----
* Finish explanation if demand warrants it.
* Camera global Gain/White Balance Correction algorithm for removing annoying camera auto-corrections from the computed results. It probably needs to consider the image as a whole.
