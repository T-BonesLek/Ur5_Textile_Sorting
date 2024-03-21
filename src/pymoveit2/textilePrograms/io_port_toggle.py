import rclpy
from rclpy.node import Node
from ur_msgs.srv import SetIO

class IOToggleClient(Node):
    def __init__(self):
        super().__init__('io_toggle_client')
        self.client = self.create_client(SetIO, '/io_and_status_controller/set_io')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetIO.Request()

    def send_request(self, pin_state_pairs):
        for pin, state in pin_state_pairs:
            self.req.fun = 1  # 1 is for digital output
            self.req.pin = pin
            self.req.state = state
            self.future = self.client.call_async(self.req)
            try:
                # Wait for the future to complete and get the result
                response = self.future.result()
                self.get_logger().info('Service call succeeded')
            except Exception as e:
                self.get_logger().info('Service call failed %r' % (e,))


# simulation = False  # Set this variable as per your requirement

def toggle_gripper(trigger, simulation):
    if simulation:
        print("Simulation mode is on. The script will not run.")
        return
    
    # rclpy.init(args=args)
    io_toggle_client = IOToggleClient()
    if trigger == 0:
        io_toggle_client.send_request([(0, 1.0), (1, 0.0)]) #Close gripper
    elif trigger == 1:
        io_toggle_client.send_request([(0, 0.0), (1, 1.0)]) #Open gripper
    io_toggle_client.destroy_node()
    # rclpy.shutdown()

if __name__ == '__main__':
    toggle_gripper(1,simulation=True)  # Call toggle_gripper with trigger = 0 to close the gripper