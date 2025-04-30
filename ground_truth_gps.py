import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

gps_path = "/home/ece/kitti/2011_09_30/2011_09_30_drive_0018_sync/oxts/data"
gps_files = sorted([f for f in os.listdir(gps_path) if f.endswith('.txt')])  # Sort to maintain sequence

frames = len(gps_files)
r = []
phi = []
theta = []

for i in range(frames):
    r.append(np.loadtxt(os.path.join(gps_path, gps_files[i]))[2])
    phi.append(np.loadtxt(os.path.join(gps_path, gps_files[i]))[1])
    theta.append(np.loadtxt(os.path.join(gps_path, gps_files[i]))[0])

plt.scatter(phi, theta, s = 0.1)
plt.show()