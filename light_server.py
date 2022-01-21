import grpc
from concurrent import futures
import time
import light_pb2_grpc as pb2_grpc
import light_pb2 as pb2

class LightServicer(pb2_grpc.LightServicer):

    def __init__(self, *args, **kwargs):
        pass

    def turnOn(self,request,context):
        response = pb2.LightStatus()
        response.status = 1
        return response

    def turnOff(self,request,context):
        response = pb2.LightStatus()
        response.status = -1
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    pb2_grpc.add_LightServicer_to_server(LightServicer(), server)
    print('Server is running on port 50052.')
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
