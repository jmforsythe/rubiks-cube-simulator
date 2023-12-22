# Rubik's Cube Simulator

## Installation
* Create virtual environment with `python -m venv .` and install required modules with `pip install -r requirements.txt`

## Running
* `python launch_gui.py`

## Usage
* Perform moves with the face buttons in the top right
* Paint the cube with the colours in the bottom right
* After painting, check that the cube is in a valid (reachable from solved with the allowed moves) state
* Enter an algorithm in the top left in standard notation
* Can either execute this algorithm, or calculate the degree (how many times this algorithm can be performed before ending up in the original state)
* Results appear in the bottom left eg "Degree of algorithm `RU2R'F` is 12"

