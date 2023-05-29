import rclpy
from example_interfaces.action import Fibonacci

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('fibonacci_client')

    client = node.create_client(Fibonacci, 'fibonacci')

    while not client.wait_for_service(timeout_sec=1.0):
        print('Action server not available. Waiting...')

    # Create a goal with the desired Fibonacci order
    goal = Fibonacci.Goal()
    goal.order = 10  # Target Fibonacci order

    # Send the goal to the action server
    future = client.send_goal_async(goal)

    # Wait for the result
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        result = future.result().result
        print("Fibonacci sequence:", result.sequence)
    else:
        print("Action failed!")

    node.destroy_node()
    rcl
