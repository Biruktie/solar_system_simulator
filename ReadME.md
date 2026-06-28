# 3D Solar System Simulator

## Project Overview

This project is a real-time 3D solar system simulation built using **Python + OpenGL (PyOpenGL + Glut)**.
It demonstrates core computer graphics concepts such as hierarchical modeling, affine transformations, and interactive animation.

The system simulates the Sun, planets, and Moon with orbital motion controlled entirely through mathematical transformations.

---

## Features

### Solar System Simulation
- Sun at the center of the system
- 8 planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
- Each planet has:
  - Orbit around the Sun
  - Self-rotation
  - Unique size and color

### Earth-Moon System
- Moon orbits Earth using hierarchical transformations
- Independent orbital speed from planets

### Saturn Ring
- Procedurally generated ring using OpenGl primitives

---

## Interactive Controls

| Key   | Action                         |
|-------|--------------------------------|
| `+`   | Increase simulation speed      |
| `-`   | Decrease simulation speed      |
| `R`   | Reverse time direction         |
| `P`   | Pause/ Resume simulation       |
| `1-8` | Select Planet                  |
| `[`   | Decrease selected planet scale |
| `]`   | Increase selected planet scale |

---

## Core Graphics Concepts Used

### 1. Hierarchical Modeling
- Moon inherits Earth's transformation
- Planets inherit Sun-centered transformations

### 2. Affline Transformations
- `glRotatef()` → orbital motion
- `glTranslatef()` → orbital radius positioning
- `glScalef()` → planet scaling

### 3. Matrix Stack
- `glPushMatrix()` / `glPopMatrix()` used to isolate transformations

### 4. Real-Time Animation
- Central light source at the Sun position
- Ambient + diffuse lighting for realism

---

## How to Run

### 1. Install dependencies 
```bash
pip install PyOpenGL PyOpenGL_accelerate
```
### 2. Run the project
```bash
python main.py
```






