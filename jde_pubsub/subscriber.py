import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'jde_topic',
            self.listener_callback,
            10)
        self.subscription 
        self.get_logger().info("Subscriber node has been started.")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: '{msg.data}'")

def main(args=None):
    rclpy.init(args=args)
    subscriber_node = Subscriber()
    rclpy.spin(subscriber_node)

    # Destroy the node explicitly
    subscriber_node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()