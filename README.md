# Autonomous Navigation on Rough Terrain

A ROS 2 Jazzy and Gazebo Sim project exploring
autonomous rover navigation over rough terrain.

## Current Progress

- Rubicon terrain world loaded in Gazebo.
- Basic four-wheel rover model created.
- Rover added to the terrain world.

## Requirements

- Ubuntu / compatible Linux environment
- ROS 2 Jazzy
- Gazebo Sim compatible with the installed ROS 2 setup

## Build

Source ROS 2 Jazzy:

    source /opt/ros/jazzy/setup.bash

Build the workspace:

    cd ~/ros2_ws
    colcon build
    source install/setup.bash

## Terrain World

The current terrain world is:

    src/rough_terrain_sim/worlds/Rubicon World/rubicon.sdf

The world references the Rubicon model hosted on Gazebo Fuel.

## Rover Model

The rover model is located in:

    src/rough_terrain_rover/models/rover/

## Development Roadmap

1. Verify rover placement and physics.
2. Add wheel control.
3. Add LiDAR and verify point-cloud data.
4. Develop terrain mapping and traversability analysis.
5. Implement path planning.
6. Implement autonomous goal-to-goal navigation.