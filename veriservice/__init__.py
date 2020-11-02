import grpc
import time
import random
import urllib.request
import platform
import tempfile
import shutil
import os
import stat
import logging
import subprocess

from veriservice import veriservice_pb2 as pb
from veriservice import veriservice_pb2_grpc as pb_grpc

__version__ = "0.0.19"

logging.basicConfig(level=logging.DEBUG)

def get_url():
    platform_type = platform.system().lower()
    url_map = {
        "darwin": "https://github.com/bgokden/veri/releases/download/v0.0.22/veri-darwin-amd64",
        "windows": "https://github.com/bgokden/veri/releases/download/v0.0.22/veri-windows-amd64",
        "linux": "https://github.com/bgokden/veri/releases/download/v0.0.22/veri-linux-amd64",
    }
    return url_map.get(platform_type, url_map.get("linux"))


def init_service(service: str):
    host, port = service.split(":")
    if host == "localhost":
        pid_file_path = service + ".pid"
        logging.debug(f"Using pid file : {pid_file_path}")
        if os.path.isfile(pid_file_path):
            logging.debug(f"Service already exists, if not remove: {pid_file_path}")
        else:
            dirpath = tempfile.mkdtemp()
            source_url = get_url()
            download_path = os.path.join(dirpath, 'veri')
            urllib.request.urlretrieve(source_url, download_path)
            st = os.stat(download_path)
            os.chmod(download_path, st.st_mode | stat.S_IEXEC)
            args = [str(download_path), "serve", "-p", str(port)]
            logging.debug(f"Running with args: {args}")
            FNULL = open(os.devnull, 'w')
            popen_output = subprocess.Popen(args, stdout=FNULL, stderr=subprocess.STDOUT)
            pid = popen_output.pid
            with open(pid_file_path, 'w') as f:
                f.write(str(pid))
    else:
        logging.debug("Service is not localhost")



class GrpcClientWrapper:
    def __init__(self, service, client):
        self.service = service
        self.client = client

    def get_service(self):
        return self.service

    def get_client(self):
        return self.client


class VeriClient:
    def __init__(self, services, data_name):
        self.services = services.split(",") # eg.: 'localhost:50051, localhost2:50051'
        self.clients = {}
        self.data_name = data_name

    def __get_client(self):
        service = random.choice(self.services)
        if service in self.clients:
            return self.clients[service]
        channel = grpc.insecure_channel(service)
        self.clients[service] = GrpcClientWrapper(service, pb_grpc.VeriServiceStub(channel))
        return self.clients[service]

    def __refresh_client(self, service):
        channel = grpc.insecure_channel(service)
        self.clients[service] = GrpcClientWrapper(service, pb_grpc.VeriServiceStub(channel))
        time.sleep(5)




    def create_data_if_not_exists(self, data_config={}, retry=5):
        request = pb.DataConfig(
            name=self.data_name,
            version=data_config.get("version", "v0"),
            TargetN=data_config.get("target_n", 10000),
            TargetUtilization=data_config.get("target_utilization", 0.9),
            NoTarget=False,
        )
        response = None
        while retry >= 0:
            client_wrapper = None
            try:
                client_wrapper = self.__get_client()
                response = client_wrapper.get_client().CreateDataIfNotExists(request)
                if response != None:
                    return response
            except grpc.RpcError as e:  # there should be connection problem
                if client_wrapper is not None:
                    self.__refresh_client(client_wrapper.get_service())
            except Exception as e:
                logging.debug(f"Error during insert: {e}")
                time.sleep(0.200)
            retry -= 1
        return response


    def insert_vector(self,
                      vector,
                      label,
                      groupLabel=None,
                      ttl=None,
                      retry=5,
                      ):
        request = pb.InsertionRequest(
            config=pb.InsertConfig(
                tTL=ttl
            ),
            datum=pb.Datum(
                key=pb.DatumKey(
                    feature=vector,
                    groupLabel=groupLabel,
                    size1=1,
                    size2=0,
                    dim1=len(vector),
                    dim2=0,
                ),
                value=pb.DatumValue(
                    version=None,
                    label=label,
                ),
            ),
            dataName=self.data_name,
        )
        response = None
        while retry >= 0:
            client_wrapper = None
            try:
                client_wrapper = self.__get_client()
                response = client_wrapper.get_client().Insert(request)
                if response.code == 0:
                    return response
            except grpc.RpcError as e:  # there should be connection problem
                if client_wrapper is not None:
                    self.__refresh_client(client_wrapper.get_service())
            except Exception as e:
                logging.debug(f"Error during insert: {e}")
                time.sleep(0.200)
            retry -= 1
        return response

    def insert(self,
                feature,
                label,
                grouplabel = '',
                timestamp = 0,
                sequencelengthone = 0,
                sequencelengthtwo = 0,
                sequencedimone = 0,
                sequencedimtwo = 0,
                retry = 5):
        request = pb.InsertionRequest(timestamp = timestamp,
                                        label = label,
                                        grouplabel = grouplabel,
                                        feature = feature,
                                        sequencelengthone = sequencelengthone,
                                        sequencelengthtwo= sequencelengthtwo,
                                        sequencedimone = sequencedimone,
                                        sequencedimtwo = sequencedimtwo)
        response = None
        while retry >= 0:
            client_wrapper = None
            try:
                client_wrapper = self.__get_client()
                response = client_wrapper.get_client().Insert(request)
                if response.code == 0:
                    return response
            except grpc.RpcError as e: # there should be connection problem
                if client_wrapper is not None:
                    self.__refresh_client(client_wrapper.get_service())
            except Exception as e:
                print(e)
                time.sleep(0.200)
            retry -= 1
        return response

    def getKnn(self, feature, k=10, id='', timestamp=0, timeout=1000, retry = 5):
        request = pb.KnnRequest(id=id, timestamp=timestamp, timeout=timeout, k=k, feature=feature)
        response = None
        while retry >= 0:
            client_wrapper = None
            try:
                client_wrapper = self.__get_client()
                response = client_wrapper.get_client().GetKnn(request)
                return response
            except grpc.RpcError as e: # there should be connection problem
                if client_wrapper is not None:
                    self.__refresh_client(client_wrapper.get_service())
            except Exception as e:
                print(e)
                time.sleep(5)
            retry -= 1
        return response

    def getKnnStream(self, feature, k=10, id='', timestamp=0, timeout=1000, retry = 5):
        request = pb.KnnRequest(id=id, timestamp=timestamp, timeout=timeout, k=k, feature=feature)
        response = None
        while retry >= 0:
            client_wrapper = None
            try:
                client_wrapper = self.__get_client()
                response = client_wrapper.get_client().GetKnnStream(request)
                return response
            except grpc.RpcError as e: # there should be connection problem
                if client_wrapper is not None:
                    self.__refresh_client(client_wrapper.get_service())
            except Exception as e:
                print(e)
                time.sleep(5)
            retry -= 1
        return response

    def getLocalData(self, retry = 5):
        request = pb.GetLocalDataRequest()
        response = None
        while retry >= 0:
            client_wrapper = None
            try:
                client_wrapper = self.__get_client()
                response = client_wrapper.get_client().GetLocalData(request)
                return response
            except grpc.RpcError as e: # there should be connection problem
                if client_wrapper is not None:
                    self.__refresh_client(client_wrapper.get_service())
            except Exception as e:
                print(e)
                time.sleep(5)
            retry -= 1
        return response

class DemoVeriClientWithData:
    def __init__(self, service):
        self.client = VeriClient(service) # eg.: 'localhost:50051'
        self.data = [
            {
                'label': 'a',
                'feature': [0.5, 0.1, 0.2]
            },
            {
                'label': 'b',
                'feature': [0.5, 0.1, 0.3]
            },
            {
                'label': 'c',
                'feature': [0.5, 0.1, 1.4]
            },
             ]

    def runExample(self):
        print('inserting data')
        for d in self.data:
            self.client.insert(d['feature'], d['label'], d['label'], 0)
        print('do a knn search')
        print(self.client.getKnn([0.1, 0.1, 0.1]))
