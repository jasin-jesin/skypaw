# 🐾 SkyPaw — Quadruped Robot with Decorative Wings

> **University of Hertfordshire** · BEng Robotics & AI · Group Project 2025–2026

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi%20Pico%20H-c51a4a)
![Language](https://img.shields.io/badge/language-CircuitPython-3776ab)
![Servos](https://img.shields.io/badge/servos-10%20×%20SG90-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## Overview

**SkyPaw** is a 4-legged quadruped walking robot with two decorative wings, built from scratch as a university group project using the **Scrum methodology** across 6 sprints. The robot is fully **3D printed**, controlled via a **Raspberry Pi Pico H**, and features four autonomous behaviours driven by onboard sensors.

The wings serve as a predator-response display — they open automatically when fast movement is detected by the PIR sensor.

<p align="center">
  <img src="docs/system_architecture.png" alt="SkyPaw System Architecture" width="800"/>
</p>

---

## Hardware Specifications

| Component | Detail |
|---|---|
| **Microcontroller** | Raspberry Pi Pico H (RP2040) |
| **Servo controller** | PCA9685 — 16-channel PWM via I2C |
| **Leg servos** | 8 × SG90 (2 per leg: hip + knee) |
| **Wing servos** | 2 × SG90 (left wing + right wing) |
| **Servo channels** | Legs: CH0–CH7 · Wings: CH8–CH9 |
| **Ultrasonic sensors** | 2 × HC-SR04 (front left + front right) |
| **Light sensors** | LDR on ADC GP26 |
| **Power supply** | 4 × AA batteries (6V rail) |
| **Frame** | Fully 3D printed PLA |
| **PWM frequency** | 50Hz · Pulse width 1–2ms |

### Pin Mapping

| Pin | Function |
|---|---|
| GP4 (SDA) | I2C to PCA9685 |
| GP5 (SCL) | I2C to PCA9685 |
| GP0 | HC-SR04 Left — Trig |
| GP1 | HC-SR04 Left — Echo |
| GP2 | HC-SR04 Right — Trig |
| GP3 | HC-SR04 Right — Echo |
| GP26 | LDR — Analogue ADC |

---

## Autonomous Behaviours

| # | Behaviour | Sensor Used | Description |
|---|---|---|---|
| 1 | **Obstacle avoidance** | HC-SR04 (×2) | Detects and steers around obstacles in path |
| 2 | **Phototaxis** | LDR | Guides robot toward a light source |
| 3 | **Predator response** | PIR | Detects fast movement, opens wings as display |
| 4 | **Random walk** | — | Explores environment in randomised directions |

---

## System Architecture

The full hardware architecture diagram is located at [`docs/system_architecture.png`](docs/system_architecture.png).

```
4 × AA (6V)
     │
     ▼
Raspberry Pi Pico H  ──(I2C)──►  PCA9685 Servo Controller
     │                                    │
     │                         ┌──────────┼──────────┐
     │                         ▼          ▼          ▼
     │                    Leg servos  Leg servos  Wing servos
     │                    CH0–CH3     CH4–CH7     CH8–CH9
     │
     ├──(GPIO GP0–GP3)──►  HC-SR04 Left + Right
     └──(ADC  GP26)────►  LDR Light Sensor
```

---

## Repository Structure

```
SkyPaw/
│
├── Jasin/
│   ├── Sprint1_Design_and_Mechanics/
│   ├── Sprint2_Electronics/
│   ├── Sprint3_Programming/
│   ├── Sprint4_Documentation/
│   └── Sprint5_Build_and_Testing/
│
├── Shekinah/
│   └── (same sprint structure)
│
├── Ramon/
│   └── (same sprint structure)
│
├── Savio/
│   └── (same sprint structure)
│
├── Apikeshini/
│   └── (same sprint structure)
│
├── docs/
│   ├── system_architecture.png   ← Hardware architecture diagram
│   ├── circuit_diagram.png       ← Full circuit schematic
│   ├── program_flowchart.png     ← Behaviour logic flowchart
│   ├── gantt_chart.png           ← Project Gantt chart
│   └── burndown_charts.png       ← Sprint burndown charts
│
├── meeting_minutes/
│   └── meeting_minutes.docx      ← All 14 sessions Jan–Apr 2026
│
├── sprint_management/
│   ├── risk_register.xlsx
│   ├── bom.xlsx                  ← Bill of materials (~£93)
│   └── sprint_plans/
│
├── media/
│   ├── photos/
│   └── videos/
│
└── README.md
```

---

## Sprint Timeline

| Sprint | Focus | Dates | Key Outcome |
|---|---|---|---|
| Sprint 0 | Planning & Setup | Jan 27 – Feb 3 | Concept confirmed, roles assigned |
| Sprint 1 | 3D Design | Feb 3 – Feb 17 | CAD models complete |
| Sprint 2 | 3D Printing | Feb 17 – Mar 3 | Physical frame printed |
| Sprint 3 | Electronics | Feb 24 – Mar 10 | Wiring and circuit complete |
| Sprint 4 | Programming | Mar 10 – Apr 7 | All 4 behaviours coded |
| Sprint 5 | Assembly & Testing | Mar 12 – Apr 14 | Full robot tested and signed off |

### Key Milestones

- 📅 **Jan 30** — Extra alignment session, peer teaching, concept locked
- 📦 **Feb 17** — Components received; Apikeshini joined the team
- 🔧 **Feb 24** — Tutor communication issue identified and resolved
- 🚶 **Mar 24** — **FIRST WALK ACHIEVED**
- 🧪 **Apr 9** — Full behaviour testing on assembled robot
- ✅ **Apr 14** — Final tweaking, project signed off

---

## Getting Started

### Requirements

- Raspberry Pi Pico H
- CircuitPython firmware (latest stable)
- Libraries: `adafruit_pca9685`, `adafruit_motor`, `adafruit_hcsr04`

### Setup

1. Flash CircuitPython onto the Pico H
2. Copy the `lib/` folder to the Pico's `CIRCUITPY` drive
3. Copy `code.py` to the root of `CIRCUITPY`
4. Power the robot — it will start in **random walk** mode by default

### Switching Behaviours

Edit the `BEHAVIOUR` constant at the top of `code.py`:

```python
BEHAVIOUR = "obstacle_avoidance"  # or "phototaxis", "predator", "random_walk"
```

---

## Bill of Materials

| Component | Qty | Unit Cost | Total |
|---|---|---|---|
| Raspberry Pi Pico H | 1 | £5.00 | £5.00 |
| PCA9685 servo controller | 1 | £3.50 | £3.50 |
| SG90 servo | 10 | £2.00 | £20.00 |
| HC-SR04 ultrasonic | 2 | £1.50 | £3.00 |
| AA battery holder (×4) | 1 | £1.50 | £1.50 |
| PLA filament | — | ~£15.00 | £15.00 |
| Jumper wires, PCB, misc | — | ~£10.00 | £10.00 |
| **Total** | | | **~£58.50** |

> Full BOM with part numbers available in [`sprint_management/bom.xlsx`](sprint_management/bom.xlsx)

---

## Team

| Name | Role |
|---|---|
| **Jasin** | Team lead, electronics, documentation |
| **Shekinah** | 3D design, assembly |
| **Ramon** | Programming, testing |
| **Savio** | Electronics, wiring |
| **Apikeshini** | Programming, documentation (joined Sprint 2) |

---

## Project Management

This project followed **Scrum** methodology with weekly sprints, managed using:

- Sprint planning documents
- Weekly meeting minutes (14 sessions total)
- Risk register
- Burndown charts per sprint
- GitHub for version control and documentation

All sprint management documents are in the [`sprint_management/`](sprint_management/) folder.

---

## License

MIT License — see [`LICENSE`](LICENSE) for details.

---

*University of Hertfordshire · BEng Robotics & AI · Group Project 2025–2026*
