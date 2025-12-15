# Dino Game – Webcam Controlled (Python)

## Overview
This project is a Python-based recreation of the classic Dino Runner game, enhanced with **webcam-based motion control**.  
Instead of using keyboard input, the player jumps by moving their hand upward in front of the webcam, using basic computer vision techniques.

The project combines **game development** with **real-time image processing**, making it an experimental interactive prototype.

---

## Features
- Real-time Dino Runner gameplay
- Webcam-based jump detection using hand motion
- Obstacle generation and collision detection
- Score tracking
- Simple, clean 2D graphics using Pygame

---

## How It Works
- The game uses **OpenCV** to capture webcam frames.
- A **Region of Interest (ROI)** is monitored for motion.
- Frame differencing and thresholding are used to detect significant upward movement.
- When motion exceeds a set threshold, the Dino jumps.
- Game physics (gravity, velocity) are handled using Pygame.

---

## Controls
- **Jump:** Move your hand upward in front of the webcam (inside the highlighted box)
- **Exit:** Close the game window

---

## Tech Stack
- Python 3.12
- Pygame
- OpenCV (cv2)
- NumPy

---

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dino-webcam-game

---

  ## Install dependencies:

pip install pygame opencv-python numpy


---

  ## Run the game:

python main.py


---

TEAM MEMBERS:
1. ANUSHKA BHATNAGAR
2. TANUJ VATSA
3. LAVANYA SHARMA
4. JENITH SHARMA
