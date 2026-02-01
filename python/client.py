from __future__ import print_function


import argparse

import grpc
import todo_pb2
import todo_pb2_grpc



def write(ip, port, todo_text):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with grpc.insecure_channel(f"{ip}:{port}") as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        response = stub.CreateTodo(todo_pb2.TodoItem(text=todo_text))
        print(f"Response -> \n{response}")
     


def read(ip, port):
    with grpc.insecure_channel(f"{ip}:{port}") as channel:
        stub = todo_pb2_grpc.TodoStub(channel)
        response = stub.ReadTodos(todo_pb2.TodoRequestNoParam())
        print(f"Response -> \n{response}")
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Args and flags for grpc client")
    parser.add_argument("--operation",  help="Create / Read gRPC operation", default="read")
    parser.add_argument("-o", "--todo_text", help="Todo text")

    parser.add_argument("--port",  help="gRPC PORT", default="67452")
    parser.add_argument("--ip",  help="gRPC ip", default="localhost")
    

    args = parser.parse_args()

   

    print(args)

    if args.operation == "read":
        read(ip=args.ip, port=args.port)

    if args.operation == "create":
        write(ip=args.ip, port=args.port, todo_text=args.todo_text)

    # run()