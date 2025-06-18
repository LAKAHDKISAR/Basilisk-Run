# Basilisk Run

Basilisk Run is a simple yet engaging snake game written in Python. The game features smooth movement, dynamic difficulty, and immersive sound effects to enhance the classic snake gameplay experience. You can control the snake with arrow keys, eat the goals to score points, and avoid hitting the walls. The game speed increases as you score more points.

## Overview

- [Introduction](#Introduction)  
- [Features](#Features)  
- [Future Goals](#Future_Goals)
- [About Graphics](#About_Graphics)
- [How to Run](#How_to_run)  
- [Requirements](#Requirements) 
- [License](#license)  
- [Acknowledgements](#Acknowledgements) 

---

## Introduction

Basilisk Run is a modern take on the classic snake game built using Python. In this game, you control a snake navigating a confined space, aiming to eat targets that appear randomly on the screen. Each successful meal increases your score and gradually speeds up the game, making it more challenging as you progress. Avoid running into the walls to keep the game going. The game features smooth controls with the arrow keys, immersive background music, and sound effects that bring the gameplay to life.

---

## Features

- Smooth and responsive controls using arrow keys  
- Increasing speed as you score points  
- Background music with sound effects for eating and game over  
- Score display  
- Start and restart the game easily with the Enter key  

---

## Future_Goals

- Implement snake growth when eating  
- Add self-collision detection  
- Enhance graphics and animations  
- Introduce obstacles and power-ups  
- Improve sound design and UI elements  

---

## About_Graphics

The graphics.py file used in this project is not a standard Python graphics library, but a adaptation of the graphics library used in Stanford’s Code in Place course. It is built using Tkinter and PIL (Pillow) to handle shapes, images, and basic user interactions. This approach was chosen mainly for personal convenience and to keep graphics handling lightweight.

---

## How_to_Run

1. Clone the Repository
2. Set Up a Virtual Environment
3. Install Required Packages:
  - pip install pygame
  - pip install pillow
4. Run the Game
  - python main.py

---

## Requirements
1. Python 3.7+
2. pygame
3. pillow
4. Note:
  - tkinter is used internally by the graphics module which is included in most python installations but if it is not available you may need to install tkinter seperately.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

The graphics.py library is inspired by the Code in Place project.
Sound effects were sourced from Freesound.org under appropriate licenses — thank you to the creators for making these available.

