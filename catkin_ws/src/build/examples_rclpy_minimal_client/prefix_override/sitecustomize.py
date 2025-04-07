import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/marco/projects/ros/catkin_ws/src/install/examples_rclpy_minimal_client'
