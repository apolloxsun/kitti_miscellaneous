import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

point_path = "/home/ece/kitti/2011_09_30/2011_09_30_drive_0018_sync/velodyne_points/data"
point_files = sorted([f for f in os.listdir(point_path) if f.endswith('.bin')])  # Sort to maintain sequence

#max x 77.692, y 78.311, z 2.902
#min x -79.178, y -46.387, z -5.26
#len 126956

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.view_init(elev=90, azim=270)

def update(frame):
    ax.clear()
    point_cloud = np.fromfile(os.path.join(point_path, point_files[frame]), dtype=np.float32).reshape(-1, 4)
    x, y, z = point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2]
    ax.scatter(x,y,z, s=0.5)

ani = FuncAnimation(fig=fig, func=update, frames=len(point_files), interval=100)

plt.show()

#ground root, map point cloud