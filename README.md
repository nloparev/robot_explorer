## robot-exploration
- Turtlebot Rapidly Explorting Random Tree and target detection using SIFT

## Setup
- to bringup Turtlebot and perform mapping and path planning with visualizer run: ```roslaunch robot_explorer setup.launch```

## Laser Scanner
- check for usb connectivity by running:```ls -l /dev/ttyACM0```
- to publish to the scan topic using live hokuyo sensor data run: ```rosrun urg_node urg_node```



## Teleoperation
- Controller config can be evaluated by running: ```jstest /dev/input/js0```
- Create ```my_ps3_teleop.launch``` to reflect controller config
- To test using controller teleop run: ```roslaunch turtlebot_teleop my_ps3_teleop.launch```

