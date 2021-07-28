#!/usr/bin/env python3
import rospy
import pandas as pd
import numpy as np
from velodyne_msgs.msg import VelodyneScan

def callback(data):
    pub = rospy.Publisher("/velodyne_packets", VelodyneScan, queue_size=10)
    pub.publish(data)

    
def listener():
    rospy.init_node('listener', anonymous=True)

    #rospy.Subscriber("/velodyne_packets", VelodyneScan, callback)
    rospy.Subscriber("/driving/velodyne/raw_packets", VelodyneScan, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
