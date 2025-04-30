import os
import numpy as np
from tqdm import tqdm

# Set your base path
sequence_path = "/home/ece/semantic_kitti/sequences/00"
velodyne_path = os.path.join(sequence_path, "velodyne")
labels_path = os.path.join(sequence_path, "labels")

# Make sure labels directory exists
os.makedirs(labels_path, exist_ok=True)

# List of all .bin files
bin_files = sorted(f for f in os.listdir(velodyne_path) if f.endswith(".bin"))

for bin_file in tqdm(bin_files, desc="Fixing label files"):
    bin_path = os.path.join(velodyne_path, bin_file)
    label_path = os.path.join(labels_path, bin_file.replace(".bin", ".label"))

    # Load point cloud
    points = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
    num_points = points.shape[0]

    # Check existing label file
    if os.path.exists(label_path):
        labels = np.fromfile(label_path, dtype=np.uint32)
        if labels.shape[0] == num_points:
            continue  # Skip if already correct

    # Generate dummy label file (class 0 = unlabeled)
    dummy_labels = np.zeros(num_points, dtype=np.uint32)
    dummy_labels.tofile(label_path)
