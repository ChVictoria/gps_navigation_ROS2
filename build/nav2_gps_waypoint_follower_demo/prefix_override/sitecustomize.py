import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vik/navigation2_tutorials/nav2_gps_waypoint_follower_demo/install/nav2_gps_waypoint_follower_demo'
