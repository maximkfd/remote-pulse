import cv2

from Video import VideoCapture


# Use a fast algorithm? Definitely.
use_ransac = True
red = (0,0,255)
green = (0,255,0)

feature_params = dict( maxCorners = 1000, 
                       qualityLevel = 0.01,
                       minDistance = 8,
                       blockSize = 19 )

lk_params = dict( winSize  = (19, 19), 
                  maxLevel = 2, 
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))   


class LKHomography():
    """
    Lucas-Kanade Tracker and warps using the randomized-consensus algorithm (RANSAC) warper
    mostly from opencv/samples/python2/lk_homography.py
    """
    def __init__(self, image, rect = None):
        """
        Define the region that we will track within image.
        
        Parameters
        ----------
        image : cv2 image
        
        rect : rectangle: 
             A list of 4 coordinates [x1,y1,x2,y2]. If rect is None, 
             use the entire size of the image.
            
        """

        if (rect == None):
            self.rect = [0,0,image.shape[1],image.shape[0]]
        else:
            #Extract coordinates from the bounding box
            self.rect = rect
        
        self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        x1,y1,x2,y2 = self.rect
        croppedGray = self.gray[y1:y2,x1:x2]
            
        #Find goodFeatures on the cropped gray image
        self.pointsOrig = cv2.goodFeaturesToTrack(croppedGray, **feature_params)
        for p in self.pointsOrig:
            p[0,0] = int(p[0,0] + x1)
            p[0,1] = int(p[0,1] + y1)
        
        #Assume we're using the points detected on the first image and don't need 
        #to show potential points to track
        output = image
        vis = output.copy()
        if self.pointsOrig is not None:
            for x, y in self.pointsOrig[:,0]:
                cv2.circle(vis, (x, y), 2, (0,255,0), -1)
            #draw_str(image, (20, 20), 'feature count: %d' % len(p))
        
        self.points = self.pointsOrig
        
        self.grayPrev       = None

    def TrackWarpCrop(self, image):
        
        self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if self.grayPrev != None:
            # Given the previous image and the next image, determine whether
            # all of self.points are still there in the current image. 
            # status is True/False for every point in pts
            pts, status = self.FindPointsAndReject(self.grayPrev, self.gray, self.points)
            #If we lost any points due to bad tracking, get rid of them
            self.points     = pts[status].copy()
            self.pointsOrig = self.pointsOrig[status].copy()
        
        # If we have a significant number of points left
        if (len(self.pointsOrig) > 12):
            
            #Find the linear mapping/warping from points back to pointsOrig 
            H, status = cv2.findHomography(self.pointsOrig, self.points, (0,cv2.RANSAC)[use_ransac], 10.0)
            
            h, w = image.shape[:2]
            #Warp the original image so that the tracker points match as close as possible the original points
            #This one is fun to look at
            output = cv2.warpPerspective(image, H, (w, h), flags=cv2.WARP_INVERSE_MAP+cv2.INTER_LINEAR)
            
            vis = output.copy()
            for (x0, y0), (x1, y1), good in zip(self.pointsOrig[:,0], self.points[:,0], status[:,0]):
                if good:
                    cv2.line(vis, (x0, y0), (x1, y1), (0, 128, 0))
                cv2.circle(vis, (x1, y1), 2, (red, green)[good], -1)
                
        
        else:
            raise Exception('Lost tracker points, re-initialize')

        self.grayPrev = self.gray
        
        cv2.imshow('LKHomography', vis)
        x1,y1,x2,y2 = self.rect
        return output[y1:y2,x1:x2,:]
        
        
    def FindPointsAndReject(self, img0, img1, p0, back_threshold = 1.0):
        '''
        Finds the tracker points p0 in img1 and returns them as p1. Also
        determines whether it lost points in p0 and returns True/False for
        whether the tracker found them
        '''
        
        p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
        p0r, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
        d = abs(p0-p0r).reshape(-1, 2).max(-1)
        status = d < back_threshold
        return p1, status
    
    
if __name__ == '__main__':
    for i, image in enumerate(VideoCapture()):
        if i == 0:
            lk = LKHomography(image)
        image2 = lk.TrackWarpCrop(image)
        #OpenCV gets a little fast going through the loop...
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break
        
    
