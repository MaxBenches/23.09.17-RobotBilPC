import socket

"""Socket binding"""
# Makes an internet (AF_INET) UDP (SOCK_DGRAM) socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# This function sends a message to a specified ip address / port
def msg_send(message,ip_address, port):
    message_str = str(message)
    message_encoded = message_str.encode("utf-8")
    sock.sendto(message_encoded, (ip_address, port))