import rclpy
from std_msgs.msg import String
import time
def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('pub_node')

    pub = node.create_publisher(String, 'topic', 10)

    msg = String()
    msg.data = 'Hello, ROS2'

    while rclpy.ok():
        pub.publish(msg)
        time.sleep(1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
