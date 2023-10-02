project(blocky_sim)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs message_runtime sensor_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/talker.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)