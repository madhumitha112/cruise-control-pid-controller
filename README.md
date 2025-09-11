# cruise-control-pid-controller
Simulation and implementation of a longitudinal Cruise Control system using PID controller for automotive applications.

# Cruise Control PID Controller

This repo contains a simple simulation of a vehicle’s cruise control system using a PID controller.


## How it works
- Vehicle mass: 1000 kg
- Target speed: 20 m/s (≈72 km/h)
- PID controller updates throttle at each timestep.

## How to run

```bash
venv\Scripts\activate.bat
pip install -r sim/python/requirements.txt   # first time only
python sim/python/cruise_pid_sim.py
