import grpc
import greeter_pb2
import greeter_pb2_grpc
from concurrent import futures

class GreeterService(greeter_pb2_grpc.GreeterServiceServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message='Hello, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServiceServicer_to_server(GreeterService(), server)
    server.add_insecure_port('[::]:50051')
    print("Starting gRPC Server...")
    server.start()
    server.wait_for_termination()

serve()
