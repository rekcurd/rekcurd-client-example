#!/usr/bin/python
# -*- coding: utf-8 -*-


from rekcurd_client import RekcurdWorkerClient


host = 'localhost'
port = 5000
application_name = "sample"
service_level = "development"
rekcurd_grpc_version = "v2"

client = RekcurdWorkerClient(
    host=host, port=port,
    application_name=application_name, service_level=service_level, rekcurd_grpc_version=rekcurd_grpc_version)

idata = [0,0,0,1,11,0,0,0,0,0,
         0,7,8,0,0,0,0,0,1,13,
         6,2,2,0,0,0,7,15,0,9,
         8,0,0,5,16,10,0,16,6,0,
         0,4,15,16,13,16,1,0,0,0,
         0,3,15,10,0,0,0,0,0,2,
         16,4,0,0]
response = client.run_predict_arrint_string(idata)
print(response)
