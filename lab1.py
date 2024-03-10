"""
CPSC 5520, Seattle University
This is free and unencumbered software released into the public domain.
:Authors: Aditya Ganti
:Assignment: Lab 1
"""
import socket
import pickle
import sys


class GCDClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self, gcd_hostname, gcd_port):
        """
        This function is responsible for creating the sockets to communicate with
        the GCD Daemon and the subsequent members that it presents

        :param gcd_hostname: string that either contains the domain name or IP address
        :param gcd_port: integer value that specifies the port number to connect to
        """
        try:
            self.sock.connect((gcd_hostname, gcd_port))  # Connecting to the GCD
        except Exception as e:
            print(f"An error occurred trying to connect to the Daemon: {str(e)}")
        else:
            self.sock.send(pickle.dumps('JOIN'))  # Sending a JOIN message
            gcd_member_list = pickle.loads(self.sock.recv(1024))
            print("Here is the list of members returned by the GCD\n", gcd_member_list)
            self.sock.close()

        # Iterating through each member in the list returned by the GCD
        for member in gcd_member_list:
            print("\nCurrent Member --> ", member)
            member_host = member['host']
            member_port = int(member['port'])

            new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_sock.settimeout(1.5)  # Setting the timeout to 1500ms
            try:
                print("Trying to connect to the above member...")
                new_sock.connect((member_host, member_port))  # Trying to connect to the member
            except Exception as e:
                print("Failed to establish a connection with the above member -> ", e)
            else:
                print("Successfully connected to the member. Here is the received message -")
                new_sock.send(pickle.dumps('HELLO'))  # Sending a HELLO message to the member
                print(pickle.loads(new_sock.recv(2048)))
            new_sock.close()

    def main(self, hostname, port):
        self.connect_to_server(hostname, port)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py GCD_HOSTNAME GCD_PORT")
        exit(1)
    client = GCDClient()
    # Arguments 1 & 2 correspond to the host and port via the console
    client.main(sys.argv[1], int(sys.argv[2]))
