import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

point_path = "/home/ece/kitti/2011_09_30/2011_09_30_drive_0018_sync/velodyne_points/data"
point_files = sorted([f for f in os.listdir(point_path) if f.endswith('.bin')])  # Sort to maintain sequence

ground_threshold = -1.5

fig = plt.figure()
ax = fig.add_subplot()

def update(frame):
    ax.clear()
    ax.set_xlim(-80, 80)  
    ax.set_ylim(-80, 80)  
    point_cloud = np.fromfile(os.path.join(point_path, point_files[frame]), dtype=np.float32).reshape(-1, 4)
    ground = point_cloud[point_cloud[:, 2] < ground_threshold]
    x, y = ground[:, 1], ground[:, 0]
    ax.scatter(x,y, s=0.1)

ani = FuncAnimation(fig=fig, func=update, frames=len(point_files), interval=100)

plt.show()
