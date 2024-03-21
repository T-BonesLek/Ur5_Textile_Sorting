import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Import the String message type
from pick_goal import move_to_pose
from place_cotton import move_to_place_cotton
from place_mix import move_to_place_mix
from place_wool import move_to_place_wool
import threading  # Import the threading module
from geometry_msgs.msg import Point  # Import the Point message type


class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription = self.create_subscription(
            Point,  # Specify the message type
            'my_robot_topic',  # Specify the topic
            self.listener_callback,  # Specify the callback
            10)  # Specify the queue size

    def listener_callback(self, msg):
        x = msg.x
        y = msg.y
        z = msg.z
        # self.get_logger().info('I heard: "x: %s, y: %s, z: %s"' % (msg.x, msg.y, msg.z))  # Log the received message
        print('Received message: "x: %s, y: %s, z: %s"' % (msg.x, msg.y, msg.z))  # Print the received message to the terminal

        if y == 1.0:
            print(x)  # Print the y value of the received message to the terminal
            if x <= -0.4 and x >= -0.6:
                try:
                    # Start a new thread to run the move_to_pose function with the received x and y values
                    threading.Thread(target=self.run_pick_cotton, args=(x, z)).start()
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid x value")


        if y == 2.0:
            print(x)
            if x <= -0.4 and x >= -0.6:
                try:
                    # Start a new thread to run the move_to_pose function with the received x and y values
                    threading.Thread(target=self.run_pick_wool, args=(x, z)).start()
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid x value")

        if y == 3.0:
            print(x)
            if x <= -0.4 and x >= -0.6:
                try:
                    # Start a new thread to run the move_to_pose function with the received x and y values
                    threading.Thread(target=self.run_pick_mix, args=(x, z)).start()
                except Exception as e:
                    print(f"An error occurred: {e}")    
            else:
                print("Invalid x value")


    def run_pick_cotton(self ,x, z):
        if z == 1.0:
            sim = True
        else:
            sim = False
        move_to_pose(x, False, sim)
        print("Pick finished")
        move_to_place_cotton(False, sim)
        print("Place finished")
    
    def run_pick_wool(self ,x, z):
        if z == 1.0:
            sim = True
        else:
            sim = False
        move_to_pose(x, False, sim)
        print("Pick finished")
        move_to_place_wool(False, sim)
        print("Place finished")

    def run_pick_mix(self ,x, z):
        if z == 1.0:
            sim = True
        else:
            sim = False
        move_to_pose(x, False, sim)
        print("Pick finished")
        move_to_place_mix(False, sim)
        print("Place finished")


def main(args=None):
    rclpy.init(args=args)  # Initialize the default context
    try:
        node = MySubscriber()
        rclpy.spin(node)  # Spin the node so it can process callbacks
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if rclpy.ok():  # Check if the context is still valid
            rclpy.shutdown()  # Shutdown the default context

if __name__ == '__main__':
    main()