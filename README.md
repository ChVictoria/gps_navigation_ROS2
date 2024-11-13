```
source /opt/ros/jazzy/setup.bash
```
```
colcon build
```
```
source ~/ros_sw/install/setup.bash
```
- Install packages
```
sudo apt install ros-jazzy-robot-localization
sudo apt install ros-jazzy-mapviz
sudo apt install ros-jazzy-mapviz-plugins
sudo apt install ros-jazzy-tile-map
```
```
- Set path to robot model
```
export GZ_SIM_RESOURCE_PATH="~/nav2_gps_waypoint_follower_demo/models"
```
- Run gazebo simulation
```
ros2 launch nav2_gps_waypoint_follower_demo gazebo_gps_world.launch.py
```
- Run localization nodes
```
ros2 launch nav2_gps_waypoint_follower_demo dual_ekf_navsat.launch.py
```
- Run mapviz
```
ros2 launch nav2_gps_waypoint_follower_demo mapviz.launch.py
```
