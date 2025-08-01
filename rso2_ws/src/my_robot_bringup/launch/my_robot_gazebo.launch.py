# my_robot_launch.py

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Argumentos
    urdf_path = LaunchConfiguration('urdf_path')
    rviz_config_path = LaunchConfiguration('rviz_config_path')
    gazebo_config_path = LaunchConfiguration('gazebo_config_path')

    return LaunchDescription([
        # Declaração de argumentos
        DeclareLaunchArgument(
            'urdf_path',
            default_value=PathJoinSubstitution([
                FindPackageShare('my_robot_description'),
                'urdf',
                'my_robot.urdf.xacro'
            ])
        ),
        DeclareLaunchArgument(
            'rviz_config_path',
            default_value=PathJoinSubstitution([
                FindPackageShare('my_robot_description'),
                'rviz',
                'urdf_config.rviz'
            ])
        ),
        DeclareLaunchArgument(
            'gazebo_config_path',
            default_value=PathJoinSubstitution([
                FindPackageShare('my_robot_bringup'),
                'config',
                'gazebo_bridge.yaml'
            ])
        ),

        # Publicar robot_description via xacro e robot_state_publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': Command([
                    'xacro ', urdf_path
                ])
            }]
        ),

        # Gazebo (ros_gz_sim)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('ros_gz_sim'),
                    'launch',
                    'gz_sim.launch.py'
                ])
            ),
            launch_arguments={'gz_args': 'empty.sdf -r'}.items()
        ),

        # Publicar modelo no Gazebo via ros_gz_sim create
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_sim', 'create', '-topic', 'robot_description'],
            output='screen'
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen'
        ),

        # Ponte de parâmetros do Gazebo
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            parameters=[{
                'config_file': gazebo_config_path
            }]
        ),
    ])
