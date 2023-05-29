import rclpy
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('service_client')

    client = node.create_client(AddTwoInts, 'add_two_ints')

    while not client.wait_for_service(timeout_sec=1.0):
        print('Service not available. Waiting...')

    a = int(input('Enter first integer'))
    b = int(input('Enter second integer'))
    request = AddTwoInts.Request()
    request.a = a
    request.b = b

    future = client.call_async(request)

    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        response = future.result()
        print(f"Result: {response.sum}")
    else:
        print("Service call failed!")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
