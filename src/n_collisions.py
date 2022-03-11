#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt64
from turtlesim.msg import Pose

counter = 0
collided = False

def callback(data):
    
    global counter, collided, pub

    pos_x = data.x
    pos_y = data.y

    if ( not ((0 < pos_x < 11.0) and (0 < pos_y < 11.0))):
        if (not collided):
            collided = True
            counter += 1
            rospy.loginfo("Amounts of collisions with wall =  %i" % (counter))
            pub.publish(counter)
    else:
        collided = False

    # rospy.loginfo("[x] = %f and [y] =  %f" % (pos_x, pos_y))
    

def listener():
    global pub
    pub = rospy.Publisher('/turtle1/collisions', UInt64, queue_size=1, latch=True)
    rospy.init_node('n_collisions_node', anonymous=True)
    pub.publish(counter)
    rospy.Subscriber("/turtle1/pose", Pose, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

