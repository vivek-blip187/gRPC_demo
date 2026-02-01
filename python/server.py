import grpc
import logging
from concurrent import futures
import argparse

import todo_pb2_grpc
import todo_pb2

todos = todo_pb2.TodoItems()

class TodoService(todo_pb2_grpc.TodoServicer):
    def ReadTodos(self, request, context):
        return todos
    

    def CreateTodo(self, request, context):
        id = len(todos.items) + 1
        todo_item = todo_pb2.TodoItem(id=id, text=request.text)
        todos.items.append(todo_item)
        return todo_item
        



# def parse_args():
#      # 1. Create the parser and add a description
#     parser = argparse.ArgumentParser(description="Args and flags for grpc server")
    
#     # 2. Add a required positional argument
#     # parser.add_argument("name", type=str, help="Your name (a required positional argument)")
    
#     parser.add_argument("-f","--logfile", help="Specify an log file path", default='grpc-server.log')

#     # 3. Add an optional argument that takes a value (an 'option')
#     # Use -o for short form, --output for long form
#     # parser.add_argument("-o", "--output", help="Specify an outut file path")
    
#     # 4. Add an optional on/off flag (boolean flag)
#     # Use -v for short form, --verbose for long form, action="store_true" makes it a boolean flag
#     parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output (a boolean flag)")
    
#     # 5. Parse the arguments from the command line
#     args = parser.parse_args()

#     print(args)

#     return args
  


def serve(grpc_port):
    port = grpc_port
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    logging.info("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    
    # args = parse_args()
    parser = argparse.ArgumentParser(description="Args and flags for grpc server")
    parser.add_argument("-f","--logfile", help="Specify an log file path", default='grpc-server.log')
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output (a boolean flag)")
    parser.add_argument("--port",  help="gRPC PORT", default="67452")
    
    args = parser.parse_args()

    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(filename=args.logfile, level=log_level)
    serve(grpc_port=args.port)