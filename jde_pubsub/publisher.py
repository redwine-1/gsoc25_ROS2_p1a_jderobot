import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'jde_topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Publisher node has been started.")

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello! ROS2 is fun.'
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: '{msg.data}'")

def main(args=None):
    rclpy.init(args=args)
    publisher_node = Publisher()
    rclpy.spin(publisher_node)

    # Destroy the node explicitly
    publisher_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()