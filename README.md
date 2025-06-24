direcory format we are using 
/kitti/dataset/
          └── sequences/
                  ├── 00/
                  │   ├── labels/
                  │   │     ├ 000000.label
                  │   │     └ 000001.label
                  │   └── velodyne/
                  │         ├ 000000.bin
                  │         └ 000001.bin

run 
./visualize.py --sequence 00 --dataset /path/to/sequences (~/filecontainingsequences or /home (if sequences directly in home) may work directly)
in the semantic-kitti-api directory

workspace directory
/home/name/semantic_kitti/
          └── semantic_kitti_api/
          └── sequences/
          └── fix_labels.py
# Visualization and Labeling Instructions

## Visualization Steps

To generate your own visualizations:

1. **Install** one of the raw synced + rectified video sequences.
2. **Create** a custom KITTI folder:
   - Inside it, create a `sequences` directory.
   - Follow the **same folder structure** as required by the SemanticKITTI API.
3. **Run** the `visualize.py` script.

> ⚠️ This process only visualizes scans based on timestamps — it does not include labeling.

---

## Labeling with MATLAB Lidar Labeler

To evaluate and label scans using MATLAB:

1. **Install** MATLAB and the **Lidar Labeler Toolbox**.
2. **Convert** `.bin` files from the `velodyne` folder to `.pcd` using:
   ```bash
   python convert_kitti_to_pcd.py



