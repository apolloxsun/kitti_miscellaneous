import numpy as np

# Load Velodyne point cloud data (binary format)
velodyne_path = "/home/ece/kitti/2011_09_30/2011_09_30_drive_0018_sync/velodyne_points/data/0000000000.bin"
lidar_points = np.fromfile(velodyne_path, dtype=np.float32).reshape(-1, 4)

# Extract XYZ coordinates
x, y, z = lidar_points[:, 0], lidar_points[:, 1], lidar_points[:, 2]

import pandas as pd

gps_data = pd.read_csv("oxts_data.txt", delim_whitespace=True, header=None)

# Extract Longitude, Latitude, Altitude, and Yaw
lon, lat, alt = gps_data.iloc[0, 0], gps_data.iloc[0, 1], gps_data.iloc[0, 2]
yaw = gps_data.iloc[0, 5]  # Vehicle heading

# Load transformation matrix (from calibration file)
velo_to_imu = np.loadtxt("calib_velo_to_imu.txt")  # 4x4 transformation matrix

# Convert LiDAR points to homogeneous coordinates
ones = np.ones((x.shape[0], 1))
lidar_homogeneous = np.hstack((x.reshape(-1, 1), y.reshape(-1, 1), z.reshape(-1, 1), ones))

# Transform to IMU/vehicle frame
lidar_vehicle = lidar_homogeneous @ velo_to_imu.T

from pyproj import Proj, Transformer

# Convert GPS (lat, lon) to UTM
proj_utm = Proj(proj="utm", zone=32, ellps="WGS84", preserve_units=False)
utm_x, utm_y = proj_utm(lon, lat)

# Transform LiDAR points to UTM coordinates
lidar_gps_x = lidar_vehicle[:, 0] + utm_x
lidar_gps_y = lidar_vehicle[:, 1] + utm_y
lidar_gps_z = lidar_vehicle[:, 2] + alt  # Add altitude

# Convert back to (Lat, Lon)
proj_latlon = Proj(proj="latlong", datum="WGS84")
transformer = Transformer.from_proj(proj_utm, proj_latlon)
gps_lon, gps_lat = transformer.transform(lidar_gps_x, lidar_gps_y)

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.scatter(gps_lon, gps_lat, s=0.5, c=lidar_gps_z, cmap="jet")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar(label="Altitude (m)")
plt.title("Velodyne LiDAR Mapped to GPS Coordinates")
plt.grid()
plt.show()
