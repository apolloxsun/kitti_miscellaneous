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
