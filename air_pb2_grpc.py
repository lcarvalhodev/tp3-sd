# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import air_pb2 as air__pb2


class AirStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.turnOn = channel.unary_unary(
                '/Air/turnOn',
                request_serializer=air__pb2.AirTemperature.SerializeToString,
                response_deserializer=air__pb2.AirTemperature.FromString,
                )
        self.turnOff = channel.unary_unary(
                '/Air/turnOff',
                request_serializer=air__pb2.AirTemperature.SerializeToString,
                response_deserializer=air__pb2.AirTemperature.FromString,
                )


class AirServicer(object):
    """Missing associated documentation comment in .proto file."""

    def turnOn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def turnOff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AirServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'turnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOn,
                    request_deserializer=air__pb2.AirTemperature.FromString,
                    response_serializer=air__pb2.AirTemperature.SerializeToString,
            ),
            'turnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOff,
                    request_deserializer=air__pb2.AirTemperature.FromString,
                    response_serializer=air__pb2.AirTemperature.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Air', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Air(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def turnOn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Air/turnOn',
            air__pb2.AirTemperature.SerializeToString,
            air__pb2.AirTemperature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def turnOff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Air/turnOff',
            air__pb2.AirTemperature.SerializeToString,
            air__pb2.AirTemperature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
