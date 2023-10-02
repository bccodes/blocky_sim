# blocky_sim


This is the repo for the blocky_sim ROS package (Noetic Ninjemys).

It is loosely based on the urdf_sim_tutorial package, but has been modified and simplified where possible.

Launching blocky.launch will start RViz and Gazebo, then running talker.py will send commands to the robot.

The included blocky URDF contains 2x links, 1x joint and 1x transmission.

This package can be expanded to model larger robots by modifying the URDF (.xacro), config (.yaml), and launch (.launch) files.

-Ben