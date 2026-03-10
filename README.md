# SkyPaw — Quadruped Robot with Decorative Wings

> University group project | Raspberry Pi Pico H | SG90 Servos | 3D Printed

## Overview

SkyPaw is a 4-legged quadruped walking robot built as part of a university group project. The robot features two decorative wings that were a mandatory task requirement — they serve as a visual display element only and open when a predator (fast-moving object) is detected.

The robot is fully 3D printed and controlled via a Raspberry Pi Pico H with a dedicated servo controller board managing all leg and wing movements.

## Tasks

- **Obstacle Avoidance** — Detects and navigates around obstacles autonomously
- **Random Walk** — Explores environment using a randomised walking pattern
- **Phototaxis** — Moves toward a light source
- **Predator Response** — Detects fast-moving objects and opens decorative wings as a display response

## Features

- 4-legged quadruped walking gait (tripod gait — 3 legs on ground at all times)
- 2 decorative wings (mandatory task requirement — visual display only, no lift)
- 3D printed chassis and limbs
- Compact servo-driven joints (SG90 motors x10)
- Raspberry Pi Pico H microcontroller

## Hardware

| Component | Details |
|---|---|
| Microcontroller | Raspberry Pi Pico H |
| Servo Controller | Dedicated servo controller board |
| Leg Servos | SG90 x8 (hip and knee joints) |
| Wing Servos | SG90 x2 (decorative display) |
| Wings | 3D printed decorative wings (task requirement) |
| Chassis | Fully 3D printed |
| Power | 4x AA alkaline batteries (6V) + 5V supply for Pico |

## Software

- CircuitPython on Raspberry Pi Pico H
- Servo PWM control via servo controller library
- Tripod gait sequences for walking motion
- Sensor integration for obstacle avoidance and phototaxis
- Predator detection logic for wing display response

## Getting Started

### Requirements

- Raspberry Pi Pico H with CircuitPython firmware
- Servo controller library
- All hardware assembled and wired

### Upload & Run

1. Flash CircuitPython onto the Pico H
2. Upload the project files
3. Run `main.py` to start the robot

## Repository Structure

```
skypaw/
├── Shekinah/
│   ├── Sprint1_Design_and_Mechanics/
│   ├── Sprint2_Electronics/
│   ├── Sprint3_Programming/
│   ├── Sprint4_Documentation/
│   └── Sprint5_Build_and_Testing/
├── Jasin/
│   ├── Sprint1_Design_and_Mechanics/
│   ├── Sprint2_Electronics/
│   ├── Sprint3_Programming/
│   ├── Sprint4_Documentation/
│   └── Sprint5_Build_and_Testing/
├── Ramon/
│   ├── Sprint1_Design_and_Mechanics/
│   ├── Sprint2_Electronics/
│   ├── Sprint3_Programming/
│   ├── Sprint4_Documentation/
│   └── Sprint5_Build_and_Testing/
└── Savio/
    ├── Sprint1_Design_and_Mechanics/
    ├── Sprint2_Electronics/
    ├── Sprint3_Programming/
    ├── Sprint4_Documentation/
    └── Sprint5_Build_and_Testing/
```

## Team

| Name | Role |
|---|---|
| Shekinah | Team Member |
| Jasin | Team Member |
| Ramon | Team Member |
| Savio | Team Member |

## Project Status

Active development — university group project in progress.
