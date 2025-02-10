import open3d as o3d
import numpy as np

# Step 1: Generate a Random 3D Point Cloud
num_points = 1000  # Adjust for more/less points
points = np.random.rand(num_points, 3)  # Random points in 3D space

# Step 2: Create Open3D PointCloud Object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Step 3: Visualize the Point Cloud
o3d.visualization.draw_geometries([pcd], window_name="3D Point Cloud")
