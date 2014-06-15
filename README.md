Installation
------------
Install Python, Numpy, and OpenCV. I have had best results using Python(x,y) on Windows, but you need to select OpenCV on the install for it to load the proper DLL's. Another distribution, Anaconda, supposedly works on all platforms, but I haven't tried it yet. Let me know what you find and I'll add it to this README.

The most recent version of Python(x,y) should work fine, as the bug detailed here (https://code.google.com/p/pythonxy/issues/detail?id=727) has been fixed according to the instructions. 

Operation
---------
Run main.py with either a webcam attached or a path to a pre-recorded video file. The best video is *ncompressed* recorded in a brightly-lit environment (daylight is great) with minimal motion from the subject and passersby and minimal automatic-adjustment from the camera. An example video is at https://www.dropbox.com/s/p0cfc0kjo7n2tth/face.avi and https://www.dropbox.com/s/d2ph5n7jjoaulig/face.mp4. 

**To change the webcam from default**
Change videoSrc in main.py from 0 (internal/default webcam) to 1 or 2 ... n

**To record a video**
Run Video.py and it will output 15 seconds of video into a file (default is webcam.avi). Then, change the videoFile variable in main.py from None to the name of your video file.

Additional Notes
----------------
* Very helpful OpenCV example code is at: https://github.com/Itseez/opencv/tree/master/samples
* I tried to organize the code so that it is easily understood and reusable in your own projects. Feel free to add it to your own libraries without attribution.

To Do
-----
* Finish explanation if demand warrants it.
* Camera global Gain/White Balance Correction algorithm for removing annoying camera auto-corrections from the computed results. It probably needs to consider the image as a whole.