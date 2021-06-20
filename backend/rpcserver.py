from xmlrpc.server import SimpleXMLRPCServer
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer(('localhost', 9000), logRequests=False)

# Expose a function
def list_contents(dir_name):
    logging.debug('list_contents(%s)', dir_name)
    return os.listdir(dir_name)
server.register_function(list_contents)

def helloWorld():
    print("Hello World")
server.register_function(helloWorld)

try:
    print("Use Control-C to exit")
    server.serve_forever()
except KeyboardInterrupt:
    print("Exiting")