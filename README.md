# Part 1: Introduction to ROS2 -> a. ‘Hello! ROS2 is fun.’
This repository contains solution to Part 1.a of the JdeRobot ROS2 challenge for GSoC 2025. The goal of this challenge is to  Create ROS2 publisher-subscriber nodes and publish the message ‘Hello! ROS2 is fun.’

## Instruction
- create working directory
  ```
  mkdir -p ~/ros2_jderobot_ws/src
  cd ~/ros2_jderobot_ws/src
  ```
- clone repository
  ```
  git clone https://github.com/redwine-1/gsoc25_ROS2_p1a_jderobot.git
  ```
- build project
  ```
  cd ..
  colcon build
  ```
- source installation and run publisher
  ```
  source  install/setup.bash
  ros2 run jde_pubsub publisher 
  ```
- open another termianl, source intstalltion and run subscriber
  ```
  source  install/setup.bash
  ros2 run jde_pubsub subscriber 
  ```
