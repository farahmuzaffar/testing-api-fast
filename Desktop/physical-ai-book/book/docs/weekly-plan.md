# Weekly Plan: 13-Week Roadmap

This section outlines the 13-week roadmap for the Physical AI & Humanoid Robotics capstone course. Each week combines theoretical concepts with hands-on lab exercises, culminating in a comprehensive capstone project.

## Course Progression Overview

```text
Week | Module Focus                  | Key Activities
-----|-------------------------------|----------------------------------
 1   | Foundations & Setup           | Env Setup, ROS 2 Basics
 2-3 | ROS 2 Fundamentals            | Nodes, Topics, Services, URDF
 4-6 | Gazebo/Unity Simulation       | Env, Sensors, Control, ROS 2 Sim
 7-9 | NVIDIA Isaac Sim              | Advanced Perception, Nav2, Manipulation
10-11| Vision-Language-Action (VLA)  | LLMs, Voice-to-Action, Planning
12   | Capstone Project Prep         | Integration, Sim-to-Real Planning
13   | Capstone Project Demos        | Final Presentations
```

## Week 1: Introduction to Physical AI & Robotics Foundations

*   **Topic**: Course overview, introduction to embodied intelligence, history of robotics, AI in robotics.
*   **Lab**: Setup development environment (Ubuntu, Docker, VS Code). Basic Linux commands and ROS 2 installation verification.
*   **Readings**: Foundational papers on embodied AI; ROS 2 Foxy/Humble documentation.

## Week 2: Robot Operating System 2 (ROS 2) Fundamentals

*   **Topic**: ROS 2 architecture (nodes, topics, services, actions), client libraries (`rclpy`), message types.
*   **Lab**: Create first ROS 2 package. Implement publisher/subscriber nodes. Use `ros2 topic` and `ros2 node` commands.
*   **Readings**: ROS 2 official tutorials (core concepts).

## Week 3: ROS 2 Advanced Concepts & Robot Modeling

*   **Topic**: Parameters, launch files, TF (Transformations), quality of service (QoS), Unified Robot Description Format (URDF).
*   **Lab**: Create URDF for a simple robot. Use `rviz2` to visualize the robot model. Implement basic TF broadcaster/listener.
*   **Readings**: ROS 2 URDF tutorials; advanced ROS 2 communication patterns.

## Week 4: Gazebo Simulation - Environment Setup

*   **Topic**: Introduction to Gazebo, creating simulation worlds, integrating URDF models into Gazebo.
*   **Lab**: Launch a simple robot in an empty Gazebo world. Create a custom Gazebo world with static objects.
*   **Readings**: Gazebo official tutorials (getting started, world building).

## Week 5: Gazebo Simulation - Sensors & Control

*   **Topic**: Simulating common robotics sensors (LiDAR, IMU, cameras), integrating ROS 2 control with Gazebo.
*   **Lab**: Add sensors to the simulated robot in Gazebo. Publish sensor data to ROS 2 topics. Implement teleoperation for the simulated robot.
*   **Readings**: Gazebo sensor plugins documentation; ROS 2 control interfaces.

## Week 6: Unity Robotics Simulation

*   **Topic**: Introduction to Unity for robotics simulation, Unity Robotics Hub, advantages over Gazebo for certain applications.
*   **Lab**: Set up a Unity environment for a robot. Integrate a robot model and connect to ROS 2.
*   **Readings**: Unity Robotics Hub documentation; comparisons of Unity and Gazebo for robotics.

## Week 7: NVIDIA Isaac Sim - Fundamentals

*   **Topic**: Introduction to NVIDIA Isaac Sim, Omniverse, USD (Universal Scene Description), high-fidelity simulation.
*   **Lab**: Launch Isaac Sim, import a basic robot model. Explore rendering and physics.
*   **Readings**: NVIDIA Isaac Sim documentation; Omniverse USD tutorials.

## Week 8: NVIDIA Isaac Sim - Perception Pipeline

*   **Topic**: Advanced sensor simulation in Isaac Sim, building perception pipelines (object detection, segmentation), ROS 2 integration.
*   **Lab**: Simulate a camera in Isaac Sim. Use ROS 2 bridge to get image data. Implement a simple object detection algorithm on simulated data.
*   **Readings**: Isaac Sim sensor API; AI perception in robotics.

## Week 9: NVIDIA Isaac Sim - Navigation & Manipulation

*   **Topic**: Autonomous navigation with Nav2 in Isaac Sim, robot manipulation (inverse kinematics, grasping).
*   **Lab**: Implement a basic Nav2 stack for a robot in Isaac Sim. Perform simple pick-and-place tasks with a simulated arm.
*   **Readings**: ROS 2 Nav2 documentation; robot manipulation algorithms.

## Week 10: Vision-Language-Action (VLA) Models - Foundations

*   **Topic**: Introduction to VLA models, multimodal AI, integration of LLMs with robotic systems.
*   **Lab**: Explore pre-trained VLA models. Understand how language instructions can be parsed for robot tasks.
*   **Readings**: Survey papers on VLA models in robotics; LLM applications in control.

## Week 11: VLA Models - Voice-to-Action & Planning

*   **Topic**: Speech-to-text (e.g., Whisper) integration, LLM-based task planning, grounding language in robot actions.
*   **Lab**: Implement a voice command interface using Whisper. Map simple natural language commands to ROS 2 actions.
*   **Readings**: Whisper documentation; research on LLM-based robot planning.

## Week 12: Capstone Project Preparation & Integration

*   **Topic**: Project scope definition, team formation, integration strategies for all modules. Simulation-to-real transfer planning.
*   **Lab**: Teams define capstone project proposals. Initial setup of a combined simulation environment for the capstone.
*   **Readings**: Project management for robotics; case studies of complex robotic systems.

## Week 13: Capstone Project Presentation & Demos

*   **Topic**: Final project presentations, demonstrations of autonomous humanoid capabilities, discussion of project challenges and future work.
*   **Lab**: Teams demonstrate their capstone projects (preferably simulation-to-real or advanced simulation).
*   **Readings**: Final project reports; peer feedback and evaluation.
