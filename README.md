## Robot operating system(ROS)
esse repositorio é a dedicado ao aprendizado e desenvolvimento de tecnologias com ROS
[Ros2 tutorials](https://docs.ros.org/en/humble/Tutorials.html)


### ROS2 comandos
Atualizar o ambiente
```bash
source /opt/ros/humble/setup.bash
```


### spwan robot in the gazebo
one by one step
```bash
 ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro my_robot.urdf.xacro)"

ros2 launch ros_gz_sim gz_sim.launch.py gz_args:="empty.sdf -r"

ros2 run ros_gz_sim create -topic robot_description
```
