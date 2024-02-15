#!/usr/bin/env python3
#
# Usage: task05_client.py -s HOST -p PORT -q QUERY [-tcp|-udp]
#
# Example (using TCP)
# $ task05_client -s 127.0.0.1 -p 3000 -q ic.unicamp.br -tcp
#
# Example (using UDP)
# $ task05_client -s 127.0.0.1 -p 3000 -q ic.unicamp.br -tcp
# ------------------------------------------------------------------------------
import argparse
import socket


def query_tcp(host, port, query):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(str.encode(query))
    data = s.recv(1024)
    s.close()
    return data.decode()


def query_udp(host, port, query):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(str.encode(query), (host, port))
    data, _ = s.recvfrom(1024)
    return data.decode()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Task05 Client")
    parser.add_argument('-s', '--host', type=str, help='Server host IP address', required=True)
    parser.add_argument('-p', '--port', type=int, help='Server port number', required=True)
    parser.add_argument('-q', '--query', type=str, help='Query domain', required=True)
    parser.add_argument('-tcp', action='store_true', help='Use TCP protocol')
    parser.add_argument('-udp', action='store_true', help='Use UDP protocol')

    args = parser.parse_args()

    if args.udp:
        result = query_udp(args.host, args.port, args.query)
        print("[UDP]")
        print(f"Result: {result}")
    else:
        result = query_tcp(args.host, args.port, args.query)
        print("[TCP]")
        print(f"Result: {result}")
