import os
import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController


def generate_launch_description():
    PKG_PATH    = get_package_share_directory('tereka_launcher')
    ROBOT_URDF  = os.path.join(PKG_PATH, 'resource', 'truck.urdf')
    WORLD_WBT   = os.path.join(PKG_PATH, 'worlds', 'plain_board.wbt')
    webots      = WebotsLauncher(world=WORLD_WBT)

    truck_driver = WebotsController(
        robot_name  = 'truck',
        parameters  = [
            {'robot_description': ROBOT_URDF},
        ]
    )
    
    serial_node = Node(
        package     = 'tereka_serial',
        executable  = 'main',
        name        = 'SerialNode'
    )

    return LaunchDescription([
        webots,
        truck_driver,
        serial_node,
        launch.actions.RegisterEventHandler(
            event_handler = launch.event_handlers.OnProcessExit(
                target_action   = webots,
                on_exit         = [launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])