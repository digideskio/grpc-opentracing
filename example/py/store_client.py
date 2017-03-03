# A OpenTraced client for a Python service that implements the store interface.
from __future__ import print_function

import grpc
import sys

import store_pb2
from grpcext import intercept_channel
from otgrpc import open_tracing_client_interceptor
import lightstep
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--access_token', help='LightStep Access Token')
    args = parser.parse_args()
    if not args.access_token:
        print('You must specify access_token')
        sys.exit(-1)

    tracer = lightstep.Tracer(component_name='python.store-client',
                              access_token=args.access_token)
    tracer_interceptor = open_tracing_client_interceptor(tracer)
    channel = grpc.insecure_channel('localhost:50051')
    channel = intercept_channel(channel, tracer_interceptor)
    stub = store_pb2.StoreStub(channel)
    response = stub.GetQuantity(store_pb2.QuantityRequest(item_id=51))
    print('Quantity: ' + str(response.quantity))

    tracer.flush()


if __name__ == '__main__':
    run()
