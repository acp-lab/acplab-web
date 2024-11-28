---
title: 'PCMPC: Perception-Constrained Model Predictive Control for Quadrotors with
  Suspended Loads using a Single Camera and IMU'
authors:
- Guanrui Li
- Alex Tunchez
- Giuseppe Loianno
author_notes:
- "Equal contribution"
- "Equal contribution"
date: '2021-01-01'
show_date: false
publishDate: '2024-11-18T23:48:37.379717Z'
publication_types:
- paper-conference
publication: '*IEEE International Conference on Robotics and Automation (ICRA)*'
summary: '*IEEE International Conference on Robotics and Automation (ICRA)*, 2021'

links:

url_pdf: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9561449
#url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_dataset: '#'
#url_poster: '#'
#url_project: ''
#url_slides: ''
#url_source: '#'
url_video: https://www.youtube.com/watch?v=BBWt1xG7Rrw

# links:
# - name: ""
#   url: ""

image:
  caption: ''
  focal_point: ""
  preview_only: false
---
Abstract: 

In this paper, we address the Perception--Constrained Model Predictive Control (PCMPC) and state estimation problems for quadrotors with cable suspended payloads using a single camera and Inertial Measurement Unit (IMU). We design a receding--horizon control strategy for cable suspended payloads directly formulated on the system manifold configuration space SE(3)xS^2. The approach considers the system dynamics, actuator limits and the camera's Field Of View (FOV) constraint to guarantee the payload's visibility during motion. The monocular camera, IMU, and vehicle's motor speeds are combined to provide estimation of the vehicle's states in 3D space, the payload's states, the cable's direction and velocity. The proposed control and state estimation solution runs in real-time at 500 Hz on a small quadrotor equipped with a limited computational unit. The approach is validated through experimental results considering a cable suspended payload trajectory tracking problem at different speeds.