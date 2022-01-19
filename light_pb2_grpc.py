# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import light_pb2 as light__pb2


class LightStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.turnOn = channel.unary_unary(
                '/Light/turnOn',
                request_serializer=light__pb2.LightStatus.SerializeToString,
                response_deserializer=light__pb2.LightStatus.FromString,
                )
        self.turnOff = channel.unary_unary(
                '/Light/turnOff',
                request_serializer=light__pb2.LightStatus.SerializeToString,
                response_deserializer=light__pb2.LightStatus.FromString,
                )


class LightServicer(object):
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


def add_LightServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'turnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOn,
                    request_deserializer=light__pb2.LightStatus.FromString,
                    response_serializer=light__pb2.LightStatus.SerializeToString,
            ),
            'turnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.turnOff,
                    request_deserializer=light__pb2.LightStatus.FromString,
                    response_serializer=light__pb2.LightStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Light', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Light(object):
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
        return grpc.experimental.unary_unary(request, target, '/Light/turnOn',
            light__pb2.LightStatus.SerializeToString,
            light__pb2.LightStatus.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Light/turnOff',
            light__pb2.LightStatus.SerializeToString,
            light__pb2.LightStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
