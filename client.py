import grpc
import customer_pb2
import customer_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = customer_pb2_grpc.CustomerServiceStub(channel)
        response = stub.GetCustomer(customer_pb2.CustomerRequest(customerName="Kanishk Verma"))
        print("Customer details received: ", response)

if __name__ == '__main__':
    run()
