#!/usr/bin/env python
###################

from __future__ import print_function

roslib.load_manifest('cv2ros2')

import roslib
import rospy
import sys
import cv2

from std_msgs.msg import String #for indigo up
from sensor_msgs.msg import Image #sensor read
from cv_bridge import CvBridge, CvBridgeError #CvBridge

###################class cv2ros#####################
class cv2ros:

  def __init__(self):
    self.image_pub = rospy.Publisher("top2",Image)
	self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("top1",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "rgb8")#red-green-blue
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255) #circle around PoI

    cv2.imshow("cv2ros", cv_image)
    cv2.waitKey(2)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "rgb8"))#red-green-blue
    except CvBridgeError as e:
      print(e)

#####################main############################
def main(args): 
  ic = cv2ros()
  rospy.init_node('cv2ros', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("close")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)