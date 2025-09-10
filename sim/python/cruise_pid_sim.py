import numpy as np
import matplotlib.pyplot as plt

# Simple Cruise Control with PID (skeleton)

# Vehicle parameters
mass = 1000.0       # kg
dt = 0.1            # time step
time = np.arange(0, 50, dt)

# Target speed
set_speed = 20.0    # m/s (~72 km/h)

# PID parameters
Kp = 500
Ki = 1
Kd = 10

# State variables
speed = 0.0
integral = 0.0
prev_error = 0.0

speed_log = []

for t in time:
    error = set_speed - speed
    integral += error * dt
    derivative = (error - prev_error) / dt

    throttle = Kp*error + Ki*integral + Kd*derivative  # control force
    accel = throttle / mass
    speed += accel * dt

    prev_error = error
    speed_log.append(speed)

plt.plot(time, speed_log, label="Vehicle Speed")
plt.axhline(set_speed, color='r', linestyle='--', label="Set Speed")
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Cruise Control PID Simulation")
plt.legend()
plt.grid(True)
plt.show()