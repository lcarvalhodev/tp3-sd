import grpc
from concurrent import futures
import air_pb2_grpc as pb2_grpc
import air_pb2 as pb2

class AirServicer(pb2_grpc.AirServicer):

    def __init__(self, *args, **kwargs):
        pass

    def turnOn(self,request,context):
        response = pb2.AirTemperature()
        print(response)
        response.temperature = request.temperature
        return response

    def turnOff(self,request,context):
        response = pb2.AirTemperature()
        print(response)
        response.temperature = -1
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    pb2_grpc.add_AirServicer_to_server(AirServicer(), server)
    print('Server is running on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
