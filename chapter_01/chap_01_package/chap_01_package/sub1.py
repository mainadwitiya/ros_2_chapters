import rclpy
from std_msgs.msg import String

def callback(msg):
    print('Received: ' + msg.data)

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('sub_node')

    sub = node.create_subscription(String, 'topic', callback, 10)

    while rclpy.ok():
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
