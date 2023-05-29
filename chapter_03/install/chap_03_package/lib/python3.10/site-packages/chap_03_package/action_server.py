import rclpy
from example_interfaces.action import Fibonacci

class FibonacciServer:
    def __init__(self):
        self.node = rclpy.create_node('fibonacci_server')
        self.server = self.node.create_action_server(Fibonacci, 'fibonacci', self.execute_callback)
        self.feedback = Fibonacci.Feedback()
        self.result = Fibonacci.Result()

    def execute_callback(self, goal_handle):
        self.node.get_logger().info('Executing action...')

        # Extract the goal value from the received request
        target = goal_handle.request.order

        # Initialize Fibonacci sequence with first two numbers
        sequence = [0, 1]

        # Calculate Fibonacci sequence until target is reached
        while len(sequence) <= target:
            # Update feedback with the latest value
            self.feedback.sequence = sequence
            goal_handle.publish_feedback(self.feedback)

            # Calculate next Fibonacci number and add it to the sequence
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)

        # Set the final result
        self.result.sequence = sequence
        goal_handle.succeed(self.result)

        self.node.get_logger().info('Action completed')

def main(args=None):
    rclpy.init(args=args)
    fibonacci_server = FibonacciServer()
    rclpy.spin(fibonacci_server.node)
    fibonacci_server.node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
