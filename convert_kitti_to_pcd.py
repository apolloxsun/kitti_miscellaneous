import numpy as np
import open3d as o3d
import os

def convert_bin_to_pcd(bin_file_path, pcd_output_path):
    """
    Converts a KITTI Velodyne .bin file to a .pcd file.

    Args:
        bin_file_path (str): Path to the input .bin file.
        pcd_output_path (str): Path to save the output .pcd file.
    """
    try:
        # Load the binary data
        # Each point is x, y, z, intensity (4 floats)
        lidar_points = np.fromfile(bin_file_path, dtype=np.float32).reshape(-1, 4)

        # Create an Open3D PointCloud object
        # We only need x, y, z for the geometry
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(lidar_points[:, :3])

        # Optionally, you can store intensity as a scalar_field or color if your tool supports it
        # For simplicity, we'll just save X,Y,Z. If you need intensity,
        # you might need to save as PCD with custom fields or XYZI.
        # Open3D's default save_point_cloud might not directly store intensity
        # as a named field without more explicit header manipulation.
        # For MATLAB's labeler, XYZ is usually sufficient for geometry.

        # Save the PointCloud object to a .pcd file
        o3d.io.write_point_cloud(pcd_output_path, pcd)
        print(f"Converted '{os.path.basename(bin_file_path)}' to '{os.path.basename(pcd_output_path)}'")

    except Exception as e:
        print(f"Error converting {bin_file_path}: {e}")

def batch_convert_kitti_velodyne(input_bin_dir, output_pcd_dir):
    """
    Batch converts all .bin files in a directory to .pcd files.

    Args:
        input_bin_dir (str): Path to the directory containing input .bin files.
        output_pcd_dir (str): Path to the directory where output .pcd files will be saved.
    """
    if not os.path.exists(output_pcd_dir):
        os.makedirs(output_pcd_dir)
        print(f"Created output directory: {output_pcd_dir}")

    bin_files = sorted([f for f in os.listdir(input_bin_dir) if f.endswith('.bin')])

    print(f"Found {len(bin_files)} .bin files in '{input_bin_dir}'")

    for bin_file_name in bin_files:
        bin_file_path = os.path.join(input_bin_dir, bin_file_name)
        # Ensure output .pcd file has the same name but .pcd extension
        pcd_file_name = bin_file_name.replace('.bin', '.pcd')
        pcd_output_path = os.path.join(output_pcd_dir, pcd_file_name)
        
        convert_bin_to_pcd(bin_file_path, pcd_output_path)

    print("Batch conversion complete.")

if __name__ == "__main__":
    # Define your input and output directories
    # This should be your 'velodyne_points/data/' folder
    input_bin_directory = '/path/to/your/custom_kitti_data/sequences/05/velodyne' #for our case we used the provided 05th sequence 
    # This will be your new folder for PCDs, which you'll point MATLAB to
    output_pcd_directory = '/path/to/new/pcd/folder/' 

    # Run the batch conversion
    batch_convert_kitti_velodyne(input_bin_directory, output_pcd_directory)
