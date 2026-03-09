# SkyPaw — Quadruped Dog Robot with Glider Wings

> University group project | Raspberry Pi Pico | SG90 Servos | 3D Printed

## Overview

SkyPaw is a quadruped walking robot inspired by a dog, built as part of a university group project. What makes it unique is the addition of two mandatory glider-like wings, allowing the robot to combine ground locomotion with passive gliding capability.

The robot is fully 3D printed and controlled via a Raspberry Pi Pico with a dedicated servo controller board managing all leg and wing movements.

## Features

- 4-legged quadruped walking gait
- 2 glider-like deployable wings (mandatory design requirement)
- 3D printed chassis and limbs
- Compact servo-driven joints (SG90 motors)
- Raspberry Pi Pico microcontroller brain

## Hardware

| Component | Details |
|---|---|
| Microcontroller | Raspberry Pi Pico |
| Servo Controller | PCA9685 or equivalent |
| Servos | SG90 (x8 minimum) |
| Wings | Custom 3D printed glider-style |
| Chassis | Fully 3D printed (PLA/PETG) |
| Power | LiPo battery pack |

## Software

- MicroPython on Raspberry Pi Pico
- Servo PWM control via servo controller library
- Gait sequences for walking motion
- Wing deploy/retract control

## Getting Started

### Requirements
- Raspberry Pi Pico with MicroPython firmware
- Servo controller library (e.g. pca9685.py)
- All hardware assembled and wired

### Upload & Run
1. Flash MicroPython onto the Pico
2. Upload the project files using Thonny or rshell
3. Run main.py to start the walking sequence

## Project Status

Active development - university group project in progress.

## Team

University group project. Contributors listed in commit history.
