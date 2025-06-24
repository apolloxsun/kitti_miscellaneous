# KITTI Scan Visualization & Labeling Guide

## 📊 Visualization Steps

To generate your own visualizations:

1. **Install** one of the raw synced + rectified video sequences.
2. **Create** a custom KITTI folder:
   - Inside it, create a `sequences` directory.
   - Follow the **same folder structure** as required by the SemanticKITTI API.
3. **Run** the `visualize.py` script.

> ⚠️ This process only enables to visualize scans based on timestamps — it does **not** include labeling.

---


## 📁 Directory Structure

The following folder structure is used for this project:

/kitti/dataset/  
└── sequences/  
├── 00/  
│ ├── labels/  
│ │ ├── 000000.label   
│ │ └── 000001.label  
│ └── velodyne/  
│ │ ├── 000000.bin   
│ │ └── 000001.bin  

---

workspace directory  
/home/name/semantic_kitti/  
          └── semantic_kitti_api/  
          └── sequences/  
          └── fix_labels.py  
          

## 🏷️ Labeling Scans Using MATLAB Lidar Labeler

To evaluate the scans with labeling, this project currently uses **MATLAB’s Lidar Labeler Toolbox**.

Follow these steps:

1. **Install** MATLAB.
2. **Install** the **Lidar Labeler Toolbox** via MATLAB Add-Ons.
3. **Convert** the Velodyne `.bin` files to `.pcd` format using the provided script:
   ```bash
   python convert_kitti_to_pcd.py


