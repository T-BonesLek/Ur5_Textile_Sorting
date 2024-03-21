import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point  # Import the Point message type

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher_ = self.create_publisher(Point, 'my_robot_topic', 10)

    def publish_message(self, x, y, z):
        msg = Point()
        msg.x = x
        msg.y = y
        msg.z = z
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "x: %s, y: %s", z: %s"' % (msg.x, msg.y, msg.z))

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    while rclpy.ok():
        x = float(input("Enter the first float to publish (or 'quit' to exit): "))
        if str(x).lower() == 'quit':
            break
        y = float(input("Enter the second float to publish (or 'quit' to exit): "))
        if str(y).lower() == 'quit':
            break
        z = float(input("Enter the third float to publish (or 'quit' to exit): "))
        if str(z).lower() == 'quit':
            break
        
        node.publish_message(x, y, z)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()