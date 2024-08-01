
from concurrent import futures
import grpc
import customer_pb2
import customer_pb2_grpc

class CustomerService(customer_pb2_grpc.CustomerServiceServicer):
    def GetCustomer(self, request, context):
        # Mock data
        if request.customerName == "Kanishk Verma":
            return customer_pb2.Customer(
                customerName="Kanishk Verma",
                address="Banglore Some Place, India"
            )
        else:
            context.set_details("Customer not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return customer_pb2.Customer()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_pb2_grpc.add_CustomerServiceServicer_to_server(CustomerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()