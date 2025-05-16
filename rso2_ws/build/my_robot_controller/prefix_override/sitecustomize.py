import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/marco/projects/robot_operating_system2/rso2_ws/install/my_robot_controller'
