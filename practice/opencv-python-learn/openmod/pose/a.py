import mediapipe as mp
import inspect

# Get the Pose class from mediapipe
Pose = mp.solutions.pose.Pose

# Method 1: Using inspect module
pose_class_file_path = inspect.getfile(Pose)
print(f"The Pose class is defined in: {pose_class_file_path}")

# Method 2: Using __file__ attribute
pose_module_file_path = mp.solutions.pose.__file__
print(f"The pose module is located at: {pose_module_file_path}")
