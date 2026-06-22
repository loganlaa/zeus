import socket

def get_system_info():

    return {
        "hostname": socket.gethostname(),
        "app": "zeus",
        "version": "1.0.0"
    }
