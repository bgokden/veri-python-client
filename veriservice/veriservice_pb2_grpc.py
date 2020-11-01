# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from veriservice import veriservice_pb2 as veriservice_dot_veriservice__pb2


class VeriServiceStub(object):
    """protoc -I veriservice/ veriservice/veriservice.proto --go_out=plugins=grpc:veriservice
    The Veri service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/veriservice.VeriService/Search',
                request_serializer=veriservice_dot_veriservice__pb2.SearchRequest.SerializeToString,
                response_deserializer=veriservice_dot_veriservice__pb2.SearchResponse.FromString,
                )
        self.Insert = channel.unary_unary(
                '/veriservice.VeriService/Insert',
                request_serializer=veriservice_dot_veriservice__pb2.InsertionRequest.SerializeToString,
                response_deserializer=veriservice_dot_veriservice__pb2.InsertionResponse.FromString,
                )
        self.Join = channel.unary_unary(
                '/veriservice.VeriService/Join',
                request_serializer=veriservice_dot_veriservice__pb2.JoinRequest.SerializeToString,
                response_deserializer=veriservice_dot_veriservice__pb2.JoinResponse.FromString,
                )
        self.DataStream = channel.unary_stream(
                '/veriservice.VeriService/DataStream',
                request_serializer=veriservice_dot_veriservice__pb2.GetDataRequest.SerializeToString,
                response_deserializer=veriservice_dot_veriservice__pb2.Datum.FromString,
                )
        self.CreateDataIfNotExists = channel.unary_unary(
                '/veriservice.VeriService/CreateDataIfNotExists',
                request_serializer=veriservice_dot_veriservice__pb2.DataConfig.SerializeToString,
                response_deserializer=veriservice_dot_veriservice__pb2.DataInfo.FromString,
                )
        self.GetDataInfo = channel.unary_unary(
                '/veriservice.VeriService/GetDataInfo',
                request_serializer=veriservice_dot_veriservice__pb2.GetDataRequest.SerializeToString,
                response_deserializer=veriservice_dot_veriservice__pb2.DataInfo.FromString,
                )
        self.SearchStream = channel.unary_stream(
                '/veriservice.VeriService/SearchStream',
                request_serializer=veriservice_dot_veriservice__pb2.SearchRequest.SerializeToString,
                response_deserializer=veriservice_dot_veriservice__pb2.ScoredDatum.FromString,
                )


class VeriServiceServicer(object):
    """protoc -I veriservice/ veriservice/veriservice.proto --go_out=plugins=grpc:veriservice
    The Veri service definition.
    """

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Join(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DataStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDataIfNotExists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VeriServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=veriservice_dot_veriservice__pb2.SearchRequest.FromString,
                    response_serializer=veriservice_dot_veriservice__pb2.SearchResponse.SerializeToString,
            ),
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=veriservice_dot_veriservice__pb2.InsertionRequest.FromString,
                    response_serializer=veriservice_dot_veriservice__pb2.InsertionResponse.SerializeToString,
            ),
            'Join': grpc.unary_unary_rpc_method_handler(
                    servicer.Join,
                    request_deserializer=veriservice_dot_veriservice__pb2.JoinRequest.FromString,
                    response_serializer=veriservice_dot_veriservice__pb2.JoinResponse.SerializeToString,
            ),
            'DataStream': grpc.unary_stream_rpc_method_handler(
                    servicer.DataStream,
                    request_deserializer=veriservice_dot_veriservice__pb2.GetDataRequest.FromString,
                    response_serializer=veriservice_dot_veriservice__pb2.Datum.SerializeToString,
            ),
            'CreateDataIfNotExists': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDataIfNotExists,
                    request_deserializer=veriservice_dot_veriservice__pb2.DataConfig.FromString,
                    response_serializer=veriservice_dot_veriservice__pb2.DataInfo.SerializeToString,
            ),
            'GetDataInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDataInfo,
                    request_deserializer=veriservice_dot_veriservice__pb2.GetDataRequest.FromString,
                    response_serializer=veriservice_dot_veriservice__pb2.DataInfo.SerializeToString,
            ),
            'SearchStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchStream,
                    request_deserializer=veriservice_dot_veriservice__pb2.SearchRequest.FromString,
                    response_serializer=veriservice_dot_veriservice__pb2.ScoredDatum.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'veriservice.VeriService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VeriService(object):
    """protoc -I veriservice/ veriservice/veriservice.proto --go_out=plugins=grpc:veriservice
    The Veri service definition.
    """

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/veriservice.VeriService/Search',
            veriservice_dot_veriservice__pb2.SearchRequest.SerializeToString,
            veriservice_dot_veriservice__pb2.SearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/veriservice.VeriService/Insert',
            veriservice_dot_veriservice__pb2.InsertionRequest.SerializeToString,
            veriservice_dot_veriservice__pb2.InsertionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Join(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/veriservice.VeriService/Join',
            veriservice_dot_veriservice__pb2.JoinRequest.SerializeToString,
            veriservice_dot_veriservice__pb2.JoinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DataStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/veriservice.VeriService/DataStream',
            veriservice_dot_veriservice__pb2.GetDataRequest.SerializeToString,
            veriservice_dot_veriservice__pb2.Datum.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDataIfNotExists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/veriservice.VeriService/CreateDataIfNotExists',
            veriservice_dot_veriservice__pb2.DataConfig.SerializeToString,
            veriservice_dot_veriservice__pb2.DataInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDataInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/veriservice.VeriService/GetDataInfo',
            veriservice_dot_veriservice__pb2.GetDataRequest.SerializeToString,
            veriservice_dot_veriservice__pb2.DataInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/veriservice.VeriService/SearchStream',
            veriservice_dot_veriservice__pb2.SearchRequest.SerializeToString,
            veriservice_dot_veriservice__pb2.ScoredDatum.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)