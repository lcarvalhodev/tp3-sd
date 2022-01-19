import grpc
from concurrent import futures
import time
import smoke_pb2_grpc as pb2_grpc
import smoke_pb2 as pb2

class SmokeServicer(pb2_grpc.SmokeServicer):

    def __init__(self, *args, **kwargs):
        pass

    def turnOn(self,request,context):
        response = pb2.SmokeStatus()
        print(response)
        response.status = request.status
        return response

    def turnOff(self,request,context):
        response = pb2.SmokeStatus()
        print(response)
        response.status = -1
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SmokeServicer_to_server(SmokeServicer(), server)
    print('Server is running on port 50053.')
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
