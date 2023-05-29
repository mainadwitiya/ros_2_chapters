import rclpy
from example_interfaces.srv import AddTwoInts

def handle_add_two_ints(request, response):
    result = request.a + request.b
    response.sum = result
    print(f"Received request: {request.a} + {request.b}")
    print(f"Sending response: {result}")
    return response

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('service_server')

    srv = node.create_service(AddTwoInts, 'add_two_ints', handle_add_two_ints)

    print('Service server ready')

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
