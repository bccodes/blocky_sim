#!/usr/bin/env python3

# Simple talker, publishes alternating values as Float64s at fixed rate

import rospy
from std_msgs.msg import Float64

destination_topic = '/blocky/controllers/position/joint1/command' #the topic to publish to
rate_hz = 2 #the rate at which to publish
cmd1_data = 1 #the first command
cmd2_data = 0 #the second command

def talker():
    pub = rospy.Publisher(destination_topic, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    ros_rate = rospy.Rate(rate_hz)
    while not rospy.is_shutdown():
        rospy.loginfo("publishing %f to %s", cmd1_data, destination_topic)
        pub.publish(cmd1_data)
        ros_rate.sleep()
        rospy.loginfo("publishing %f to %s", cmd2_data, destination_topic)
        pub.publish(cmd2_data)
        ros_rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
