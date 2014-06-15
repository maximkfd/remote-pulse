To get remote pulse detection working, you will need to install Python, Numpy and OpenCV.

Installation
------------
Anaconda should work for all platforms...?
Windows
-------
* Install a tool like Python(x,y) or Anaconda to get numpy and Python.
* Install OpenCV:
** If you use Python(x,y), you can click the appropriate check box in the install exe
to install OpenCV (which will install the FFMPEG dll as well).
*** However, it doesn't work quite yet: https://code.google.com/p/pythonxy/issues/detail?id=727
** If you want to install OpenCV manually, copy the appropriate cv2.pyd file (as of 2.8.4
inside of opencv\build\python\<platform>) to C:\Python27\Lib\site-packages


* Download OpenCV separately for great example code + FFMPEG dll's. 
** Alternatively, the github for the source code is: https://github.com/Itseez/opencv/tree/master/
** The SAMPLE CODE is at: https://github.com/Itseez/opencv/tree/master/samples


* Download OpenCV separately for great example code + FFMPEG dll's. 
** To enable FFMPEG (for more reasonable output file sizes using x264 codec), 
follow the instructions at: http://goo.gl/n8ipvY

Linux
-----
* You should be able to figure out what to do :) Something to do with 
sudo apt-get install *** on Ubuntu. I think you have to compile from source
and enable V4L for webcam drivers and FFMPEG if you want FFMPEG.


* Github formatting (markdown)

Operation
---------
Run main.py with either a webcam attached or a path to a pre-recorded video file. 
*Uncompressed* video recorded in a brightly-lit environment (daylight is great)
with minimal motion from the subject and passersby and minimal 
automatic-adjustment from the camera is best. 
An example video is at __________. 

**To change the webcam from default**
change videoSrc in main.py from 0 (internal/default webcam) to 1 or 2 ... n

**To record a backup video**
run Video.py and it will output 15 seconds of video into webcam.avi. Then, change the
videoFile variable in main.py from None to 'webcam.avi'.


To convert from avi to other formats using FFMPEG:
Settings for AVC1 or libx264
ffmpeg -i face.avi -c:v libx264 -crf 18 face_compressed.mp4



To Do
-----
* Finish explanation if demand warrants it
* Camera global Gain/White Balance Correction algorithm for removing annoying camera 
auto-corrections from the computed results. It probably needs to consider the image
as a whole.